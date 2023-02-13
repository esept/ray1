# Etape 6 : Phong et surfaces réfléchissantes

Le but de ce TP est d'introduire de nouvelles façon de calculer l'illumination d'un point, comme la prise en compte des surfaces réfléchissantes. Cette opération nécessite des appels récursifs à la méthode de calcul de la couleur des pixels. Cela va entrainer une augmentation significative du temps de génération des scènes.

## Calcul de l'illumination de Phong

La couleur diffuse ne tient pas compte de l'oeil de l'observateur. C'est le modèle d'illumination de Phong qui permet d'intégrer cela.

La [formule originale](http://fr.wikipedia.org/wiki/Ombrage_Phong) est :

+ $`\vec{r} = -\vec{lightdir}+2 \times (\vec{n} \cdot \vec{lightdir}) \times \vec{n}`$
+ $`l_p =  max(\vec{r} \cdot \vec{eyedir},0)^{shininess} \times  lightcolor \times  couleur_{specular}`$

avec $`\vec{eyedir}=-\vec{d}`$, c'est à dire que $`\vec{eyedir}`$ représente la direction du point vers l'oeil, et non le contraire comme dans les calculs précédents.

En pratique, on utilise un modèle simplifié, plus facile à calculer, le [Blinn-Phong](https://en.wikipedia.org/wiki/Blinn–Phong_shading_model).

+ $`\vec{h} = \frac{\vec{lightdir} + \vec{eyedir}}{||\vec{lightdir} + \vec{eyedir}||}`$
+ $`l_bp =  max(\vec{n}\cdot \vec{h},0)^{shininess} \times  lightcolor \times  couleur_{specular}`$

En obtient donc la formule générale pour le calcul de couleur d'un point :

```math
c = l_a + (\sum_i (max(\vec{n} \cdot \vec{lightdir_i},0) \times  lightcolor_i \times  couleur_{diffuse} + max(\vec{n}\cdot \vec{h_i},0)^{shininess} \times  lightcolor_i \times  couleur_{specular}))
```

où $`i`$ représente la $`ième`$ source de lumière.

## Prise en compte de l'illumination indirecte

Jusqu'à présent, la couleur d'un point était calculée à partir des sources de lumières directes : la lumière d'ambiance et les sources de lumière ponctuelles ou directionnelles.

Nous allons maintenant prendre en compte la lumière réfléchie.

Soit $`c`$ la couleur d'un point $`p`$ comme calculée au TP5 à l'aide des modèles d'illumination de Lambert et Blinn-Phong.

Si la valeur de la couleur $`specular`$ de l'objet est différente de zéro (noir), il s'agit d'une surface réfléchissante.

**Il s'agit d'une convention dans notre représentation des scènes, pour simplifier la description des scènes.
Vous trouverez dans la littérature des couleurs spécifiques pour la lumière réfléchie, différente de la couleur specular.**

Dans ce cas, il est nécessaire d'ajouter à la couleur courante la couleur reçue indirectement via réflexion. On note $`\vec{r}`$ le vecteur qui indique la direction "réfléchie" du regard, c'est à dire ayant le même angle avec la normale que $`\vec{d}`$, sur le même plan que $`\vec{n}`$ et $`\vec{d}`$.

![direction réfléchie](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Ray_optics_diagram_incidence_reflection_and_refraction.svg/500px-Ray_optics_diagram_incidence_reflection_and_refraction.svg.png)

On calcule $`\vec{r}`$ de la manière suivante :

```math
\vec{r} = \vec{d} + 2\times (\vec{n} \cdot (-\vec{d}))\times \vec{n}
```

**Attention : comme toutes les directions, $`\vec{r}`$ doit être unitaire.**

Le calcul de cette contribution se fait en trois étapes :

1. on vérifie tout d'abord qu'il existe un objet renvoyant de la lumière, c'est à dire qu'il existe une intersection avec un objet dans la direction $`\vec{r}`$ de la lumière réfléchie. **Attention cependant à ne pas trouver une intersection avec l'objet lui-même (apparition de "grains" sur les objets).**
2. si c'est le cas, on calcule la couleur $`c'`$ du point $`p'`$ d'intersection avec cet objet à l'aide d'un appel récursif à la méthode de calcul de couleur. **Pour arrêter la récursion, il faut utiliser un paramètre de profondeur `maxdepth` et s'arrêter quand `maxdepth` est atteint.**
3. enfin on ajoute la contribution de la lumière réfléchie en appliquant la couleur de réflexion : $`c = c + specular \times c'`$.

On peut représenter cette approche à l'aide d'une suite arithmétique, en considérant que $`p`$ est le point d'intersection courant et $`p'`$ est le point d'intersection depuis $`p`$ selon $`\vec{r}`$.

+ $`u_i(p) = couleur_{directe}(p)`$ si $`specular_p = (0,0,0)`$ ou pas de point $`p'`$  
+ $`u_i(p) = couleur_{directe}(p) + specular_p \times u_{i+1}(p')`$ sinon
+ $`u_{maxdepth}(p) = (0,0,0)`$


## Attention aux couleurs calculées

Jusqu'à présent, par construction des scènes, les sources de lumière directes ne peuvent pas résulter en une couleur dont une composante dépasse 1 (100%).

En prenant en compte les sources de lumière indirectes, il est possible d'obtenir des couleurs dont l'une des composantes dépasse 1. Si c'est le cas, cette composante sera ramenée à 1.

## Le fichier de description de scènes

Afin de gérer dans le fichier de scène la limite du calcul récursif de la lumière, un nouveau paramètre `maxdepth` est nécessaire.

Si `maxdepth` vaut 1, alors on ne prend pas en compte la lumière réfléchie, on se limite à la contribution des lumières directes.

Quand `maxdepth` augmente, le nombre de reflets dans les objets est susceptible d'évoluer.

Généralement, on utilisera une valeur de `maxdepth` comprise entre 5 et 10.

## Vérification de la génération des scènes

Comme précédemment, ce sont les scripts `raytrace.sh` et `compare.sh` qui sont utilisés pour vérifier que les images générées sont identiques aux images attendues.

Décommenter les tests liés dans le fichier `tests.sh` et le fichier `.gitlab-ci.yml`.

Une fois le travail réalisé, faire un ```commit``` puis un ```push``` de ce travail sur gitlab.

Vous pouvez vérifier sur [sonarqube](https://sonarqube.univ-artois.fr) si l'analyse automatique de votre code a relevé des violations des règles associées à votre langage. Si les remarques sont pertinentes, il faut corriger de manière appropriée votre code.

