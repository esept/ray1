# Les autres intersections

## Intersection avec un plan

Un plan est défini par un point $q$ et une normale $`\vec{n}`$.
On cherche un point $`p = o +\vec{d}*t`$ tel que $`(p - q)`$ et $`\vec{n}`$ soient orthogonaux, soit $`(p - q) \cdot \vec{n} = 0`$.

Il faut donc résoudre l'équation $`(o + \vec{d}*t -q)  \cdot \vec{n} = 0`$ soit  $`(o - q + \vec{d}*t)  \cdot \vec{n} = 0`$ soit
$(o - q) \cdot \vec{n} +  \vec{d}*t \cdot  \vec{n} = 0`$.

On trouve donc $`t = \frac{- (o - q) \cdot \vec{n}}{\vec{d} \cdot  \vec{n}}`$.

Comme $`-(o - q) = (q - o)`$, on peut simplifier en

$`t = \frac{(q - o) \cdot \vec{n}}{\vec{d} \cdot  \vec{n}}`$.

Si $`\vec{d} \cdot  \vec{n} = 0`$, notre équation n'a pas de solution : $`\vec{d}`$ est perpendiculaire à la normale, donc est parallèle au plan.

## Intersection avec un triange

On dispose de trois points, donnés selon l'ordre anti-horaire : $`a,b,c`$.

On cherche tout d'abord si le point se trouve dans le plan du triange, en utilisant la même technique que pour le plan.
Ensuite, on cherche si le point est à l'intérieur du triangle en recherchant l'expression du point à partir des coordonnées des points.

### Intersection avec le plan

On cherche tout d'abord la normale du triangle $`a,b,c`$ $`\vec{n} = \frac{(b-a)\cdot(c-a)}{||(b-a)\cdot(c-a)||}`$.

On applique la technique ci-dessus pour calculer la valeur de $`t`$ si elle existe.

### Calcul des normales

Il suffit de vérifier les trois conditions suivante :

+ $`((b - a) \times (p - a)) \cdot \vec{n} \geq 0`$
+ $`((c - b) \times (p - b)) \cdot \vec{n} \geq 0`$
+ $`((a - c) \times (p - c)) \cdot \vec{n} \geq 0`$

### Calcul du barycentre

Il s'agit maintenant de vérifier que le point est à l'intérieur du triangle.

Si c'est le cas, alors on peut exprimer $p$ en fonction de $a$, $b$ et $c$,
soit $`p = \alpha * a  + \beta * b + \gamma *c`$ tel que

+ $`\alpha \geq 0$, $\beta \geq 0$, $\gamma \geq 0`$
+ $`\alpha + \beta + \gamma = 1`$

On peut définir $`\alpha = 1 - \beta - \gamma`$ et le remplacer dans la première équation :
```math
p =  (1 - \beta - \gamma)*a + \beta *b + \gamma *c = a + \beta * (b - a) + \gamma * (c - a)
```
```math
p - a = \beta * (b - a) + \gamma * (c - a)
```

### Calcul implémenté

#### Intersection avec le plan

On calcule tout d'abord la normale $`\vec{p}`$ du plan formé par $`\vec{d}`$ et $`(c-a)`$.

```math
\vec{p} = \vec{d} \times (c-a)
```

On vérifie ensuite la valeur du cosinus de l'angle entre $`\vec{p`$ et $`(b-a)`$.

```math
det = (b-a) \cdot \vec{p}
```

Si ce cosinus est proche de 0, alors $`\vec{p}`$ et $`(b-a)`$ sont perpendiculaires,
donc $`\vec{d}`$ est parallèle au plan du triange.

si $`|det|< \epsilon`$ alors pas d'intersection.

#### A l'intérieur du triangle

+ $`\vec{t} = (lookFrom - a)`$
+ $`\beta = \frac{\vec{t} \cdot \vec{p}}{det}`$
+ si $`|\beta|< 0`$ alors pas d'intersection

+ $`\vec{q} = \vec{t} \times (b - a)`$
+ $`\gamma = \frac{\vec{d} \cdot \vec{q}}{det}`$
+ si $`\gamma <0`$ ou $`\beta + \gamma >1`$ alors pas d'intersection

+ $`t = \frac{(c-a) \cdot \vec{q}}{det}`$
+ si $`t< \epsilon`$ alors pas d'intersection

+ retourner $`t`$

# Calcul de la couleur d'un point : la radiance

Le calcul de la couleur d'un point se fait en additionnant toutes les sources de lumière
pour ce point.

## Lumière ambiance : $l_a$

La lumière ambiante est ajoutée à tous les points de la scène.

## La réflexion diffuse (Johann Heinrich Lambert, Photometria 1760)

La réflexion diffuse est un modèle qui considère que la lumière est réfléchie de manière identique dans toutes les directions.

L'intensité de la lumière est donc proportionnelle à l'angle de la normale de la surface et de la direction de la lumière.

Une source de lumière perpendiculaire à la surface sera d'intensité maximale alors qu'une source de lumière // à la surface sera d'intensité nulle.

La couleur d'un point pour une source de lumière en utilisant la formule de Lambert est donc

```math
l_d = max(\vec{n}\cdot \vec{lightdir},0) * lightcolor * couleur_{diffuse}
```

Cette formule ne tient pas compte de l'oeil de l'observateur. C'est le modèle d'illumination de Phong qui permet d'intégrer cela.
En pratique, on utilise un modèle simplifié, plus facile à calculer, le [Blinn-Phong](https://en.wikipedia.org/wiki/Blinn–Phong_shading_model).

+ $`\vec{h} = \frac{lightdir + eyedir}{|lightdir - eyedir|}`$
+ $`l_bp =  max(\vec{n}\cdot \vec{h},0)^{shinyness} * lightcolor * couleur_{specular}`$
