# Etape 3 : génération d'images avec des sphères en 2D

## Mise en place de la structure principale du lanceur de rayons

Le but de cette nouvelle étape est de mettre en place la boucle principale du lanceur de rayons, avec la détection des intersections, sans avoir à se préoccuper pour l'instant de la couleur des pixels. On utilisera un pixel noir quand un rayon ne touche aucun objet et un pixel de la couleur de l'objet touché dans le cas contraire.

Dans cette première partie, on se limitera aux spheres.

## Pseudo-code du lanceur de rayon

Le pseudo-code du lanceur de rayons est le suivant :

```
charger la scène

pour chaque pixel (i,j) de l'image à générer faire
    calculer le vecteur unitaire d qui représente
          un rayon allant de l'oeil o au centre du pixel (i,j)
    rechercher le point p = o + d*t  d'intersection
          le plus proche (t minimal) avec un objet de la scène
    si p existe
        alors calculer sa couleur
        sinon utiliser du noir
    peindre le pixel (i,j) avec la couleur adéquat

sauvegarder l'image
```

### Calcul du repère orthonormé $`(\vec{u},\vec{v},\vec{w})`$

Le vecteur réprésentant la direction du rayon de l'oeil au pixel de l'image
doit un représenté dans un repère orthonormé $`(\vec{u},\vec{v},\vec{w})`$.

$`\vec{w}`$ correspond à l'axe passant par l'oeil (_lookFrom_) et le point regardé (_lookAt_).

Il se calcule de la façon suivante :

```math
\vec{w} = \frac{lookFrom - lookAt}{||lookFrom - lookAt||}
```

Il est possible de calculer une normale $`\vec{u}`$ au plan formé par les vecteurs $`\vec{up}`$ et $`\vec{w}`$ à l'aide du produit vectoriel (noté $`\times`$).

```math
\vec{u} = \frac{\vec{up} \times \vec{w}}{||\vec{up} \times \vec{w}||}
```

Enfin, à partir de $`\vec{u}`$ et $`\vec{w}`$, on peut calculer $`\vec{v}`$ :

```math
\vec{v} = \frac{\vec{w} \times \vec{u}}{||\vec{w} \times \vec{u}||}
```

### Calcul des dimensions d'un pixel dans le repère $`(\vec{u},\vec{v},\vec{w})`$

Les dimensions d'un pixel dans la scène varient avec l'angle de vue $`fov`$ (_field of view_) .

On notera $`imgwith`$ et $`imgheight`$ les dimensions de l'image en pixels.

$`fov`$ étant en dégré, il doit être transformé en radians ($`fovr`$) :

```math
fovr = \frac{fov*\pi}{180}
```

**On suppose dans notre cas que l'image en pixels se trouve à une unité de l'oeil sur l'axe $`\vec{w}`$.**

La hauteur d'un pixel dans la scène est donc de

```math
pixelheight = tan(\frac{fovr}{2})
```

La largeur du pixel doit respecter le ratio $`\frac{imgwidth}{imgheight}`$.

```math
pixelwidth = pixelheight * \frac{imgwidth}{imgheight}
```

### Calcul du vecteur direction $`\vec{d}`$ pour un pixel (i,j)

Les coordonnées d'une image vont généralement de (0,0) au coin inférieur gauche à
(imgwidth,imgheight) au coin supérieur droit de l'image.

**Attention, cela peut changer selon les bibliothèques utilisées, en Java par exemple (0,0) se trouve sur le coin supérieur gauche.**

Notre scène est centrée en $`(\frac{imgwidth}{2},\frac{imgheight}{2})`$.

On doit donc traduire de $`(i,j)`$ dans $`(u,v)`$ en les translatant de $`(-\frac{imgwidth}{2},-\frac{imgheight}{2})`$.

De plus, on cherche à viser le centre du pixel, donc on translatera la direction de $`(0.5,0.5)`$.

Enfin, on normalise chaque valeur.

Au final on obtient :

```math
a = \frac{pixelwidth*(i - \frac{imgwidth}{2} + 0.5)}{\frac{imgwidth}{2}}
b = \frac{pixelheight*(j - \frac{imgheight}{2} + 0.5)}{\frac{imgheight}{2}}
```

On obtient $`\vec{d}`$ avec l'équation :

```math
\vec{d} = \frac{\vec{u} * a + \vec{v} * b - \vec{w}}{||\vec{u} * a + \vec{v} * b - \vec{w}||}
```

## Calcul de l'intersection d'un rayon avec une sphère

Pour l'instant, nous supposons que les seuls objets présents sur la
scène sont des sphères. Elles sont définies par un centre $`c`$ et un rayon $`r`$.

Nous cherchons donc un point $`p = o + \vec{d}*t`$ tel que $`||p - c|| = r`$ soit

```math
(p-c)\cdot(p-c) -r^2 = 0
(o-c + \vec{d}*t)\cdot(o-c +\vec{d}*t) -r^2 = 0
```

Il s'agit d'une équation du second degré en $`t`$ de la forme $`a*t^2 + b*t + c = 0`$ avec

* $`a = \vec{d} \cdot \vec{d} = ||\vec{d}||*||vec{d}||*cos(0) = 1`$
* $`b = 2*(o-c)\cdot \vec{d}`$
* $`c = (o-c)\cdot(o-c)-r^2`$

On calcule le discriminant $`\Delta = b^2 -4*a*c`$.

* Si $`\Delta`$ est négatif, pas d'intersection.
* Si $`\Delta`$ est nul, alors il y a une seule intersection avec $`t = \frac{-b}{2*a}`$.
* Si $`\Delta`$ est positif, alors il y a deux intersections
$`t_1 = \frac{-b +\sqrt{\Delta}}{2*a}`$ et $`t_2 = \frac{-b -\sqrt{\Delta}}{2*a}`$.

$`t_2`$ est plus proche (petit) que $`t_1`$ mais $`t_2`$ pourrait être négatif.

Si $`t_2`$ est positif l'intersection la plus proche est $`t_2`$ sinon si $`t_1`$ est positif l'intersection la plus proche est $`t_1`$ sinon il n'y a pas d'intersection dans le champs de l'image.


### Calcul de la couleur du point d'intersection

Cette semaine, on ne se pose pas la question de calculer une valeur
correcte pour la lumière. On utilisera tout simplement la lumière
ambiante de la scène (valeur de l'attribut `ambient` dans le fichier
de description de scène) comme couleur du point d'intersection.

**Attention : le calcul de la couleur peut s'avérer différent selon le type de 
données utilisé pour les composantes RVB. En java, le calcul [0,1] vers [0,255]
s'effectue de la façon suivante dans la classe `java.awt.Color` :**

```java
/**
     * Creates an opaque sRGB color with the specified red, green, and blue
     * values in the range (0.0 - 1.0).  Alpha is defaulted to 1.0.  The
     * actual color used in rendering depends on finding the best
     * match given the color space available for a particular output
     * device.
     *
     * @throws IllegalArgumentException if {@code r}, {@code g}
     *        or {@code b} are outside of the range
     *        0.0 to 1.0, inclusive
     * @param r the red component
     * @param g the green component
     * @param b the blue component
     * @see #getRed
     * @see #getGreen
     * @see #getBlue
     * @see #getRGB
     */
    public Color(float r, float g, float b) {
        this( (int) (r*255+0.5), (int) (g*255+0.5), (int) (b*255+0.5));
        testColorValueRange(r,g,b,1.0f);
        frgbvalue = new float[3];
        frgbvalue[0] = r;
        frgbvalue[1] = g;
        frgbvalue[2] = b;
        falpha = 1.0f;
        fvalue = frgbvalue;
    }
```

## Exemples de scènes

### Une seule sphère

```
size 640 480
camera 0 0 4 0 0 0 0 1 0 45
output tp31.png
ambient 1 0 0

sphere 0 0 0 1
```

![Une sphère rouge, fov à 45 degrés](tp31.png)

En faisant varier la valeur de $`fov`$, on obtient des images différentes.

Par exemple, en augmentant $`fov`$ à 60 degrés, on obtient une sphère plus petite sur l'image.

![Une sphère rouge, fov à 60 degrés](tp3160.png)

En réduisant $`fov`$ à 30 degrés, on obtient une sphère plus grande.

![Une sphère rouge, fov à 30 degrés](tp3130.png)

### Deux sphères l'une à coté de l'autre

```
size 640 480
camera 0 0 4 0 0 0 0 1 0 45
output tp32.png
ambient 1 0 0

sphere -1 0 0 1
sphere 1 0 0 1
```

![tp32](tp32.png)
![]
### Deux sphères l'une derrière l'autre

```
size 640 480
camera 0 0 4 0 0 0 0 1 0 45
output tp33.png
ambient 1 0 0

sphere 0 0 1 1
sphere 0 0 -1 1
```

![tp33](tp33.png)

### Deux sphères sur deux plans différents

```
size 640 480
camera 0 0 4 0 0 0 0 1 0 60
output tp34.png
ambient 1 0 0

sphere 1 0 1 1
sphere -1 0 -1 1
```

![tp34](tp34.png)


### Les oreilles de Mickey

```
size 640 480
camera 0 0 4 0 0 0 0 1 0 45
output tp35.png
ambient .5 .5 .5

sphere 0 0 0 1
sphere .7 .7 0 .6
sphere -.7 .7 0 .6
```

![tp35](tp35.png)

## Vérification des premières images générées

Un script `raytrace.sh` est maintenant attendu pour générer une image à partir d'une description de scène.
Il est nécessaire de le modifier pour l'adapter à votre code.

Ce script prend en paramètre le nom du fichier de scène et génère l'image correspondante. 

Le script `compare.sh` conçu dans la première étape est ensuite utilisé pour vérifier si l'image produite est
identique à l'image attendue.

**Les images générées doivent être identiques, indépendamment du langage utilisé pour écrire le lanceur de rayons.**

Décommenter les tests liés dans le fichier `tests.sh` et le fichier `.gitlab-ci.yml`.

Une fois le travail réalisé, faire un ```commit``` puis un ```push``` de ce travail sur gitlab.

Vous pouvez vérifier sur [sonarqube](https://sonarqube.univ-artois.fr) si l'analyse automatique de votre code a relevé des violations des règles associées à votre langage. Si les remarques sont pertinentes, il faut corriger de manière appropriée votre code.

