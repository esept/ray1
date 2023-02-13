# Etape 5 : apparition des objets plans et triangles dans la scène, et des ombres sur l'image

## Intersection avec un plan

![plan](plan.png)

Un plan est défini par un point $`q`$ et une normale $`\vec{n}`$.
On cherche un point $`p = o +\vec{d}*t`$ tel que $`(p - q)`$ et $`\vec{n}`$ soient orthogonaux, soit $`(p - q) \cdot \vec{n} = 0`$.

Il faut donc résoudre l'équation $`(o + \vec{d}*t -q)  \cdot \vec{n} = 0`$ soit  $`(o - q + \vec{d}*t)  \cdot \vec{n} = 0`$ soit
$`(o - q) \cdot \vec{n} +  \vec{d}*t \cdot  \vec{n} = 0`$.

On trouve donc $`t = \frac{- (o - q) \cdot \vec{n}}{\vec{d} \cdot  \vec{n}}`$.

Comme $`-(o - q) = (q - o)`$, on peut simplifier en

$`t = \frac{(q - o) \cdot \vec{n}}{\vec{d} \cdot  \vec{n}}`$.

Si $`\vec{d} \cdot  \vec{n} = 0`$, notre équation n'a pas de solution : $`\vec{d}`$ est perpendiculaire à la normale, donc est parallèle au plan.

## Intersection avec un triangle

![triangle](triangle.png)

On dispose de trois points, donnés selon l'ordre anti-horaire : $`a,b,c`$.

On cherche tout d'abord si le point se trouve dans le plan du triange, en utilisant la même technique que pour le plan.

Ensuite, on cherche si le point est à l'intérieur du triangle en recherchant l'expression du point à partir des coordonnées des points.

### Intersection avec le plan

On cherche tout d'abord la normale du triangle $`a,b,c`$ $`\vec{n} = \frac{(b-a)\times(c-a)}{||(b-a)\times(c-a)||}`$.

On applique la technique ci-dessus pour calculer la valeur de $`t`$ si elle existe.

Il s'agit maintenant de vérifier que le point est à l'intérieur du triangle.

### Approche 1 : calcul des normales

Il suffit de vérifier les trois conditions suivantes pour vérifier si le point fait partie du triangle :

+ $`((b - a) \times (p - a)) \cdot \vec{n} \geq 0`$
+ $`((c - b) \times (p - b)) \cdot \vec{n} \geq 0`$
+ $`((a - c) \times (p - c)) \cdot \vec{n} \geq 0`$

Noter que l'on peut arrêter les calculs dès que l'une des conditions n'est pas vérifiée.

### Approche 2 : calcul du barycentre

Si le point fait partie du triangle, alors on peut exprimer $`p`$ en fonction de $`a`$, $`b`$ et $`c`$,
soit $`p = \alpha * a  + \beta * b + \gamma *c`$ tel que

+ $`\alpha \geq 0`$, $`\eta \geq 0`$, $`\gamma \geq 0`$
+ $`\alpha + \beta + \gamma = 1`$

On peut définir $`\alpha = 1 - \beta - \gamma`$ et le remplacer dans la première équation :

```math
p =  (1 - \beta - \gamma)*a + \beta *b + \gamma *c = a + \beta * (b - a) + \gamma * (c - a)
p - a = \beta * (b - a) + \gamma * (c - a)
```

On obtient une équation par composante (x,y et z) pour deux inconnues ($`\beta`$ et $`\gamma`$). On peut utiliser les deux premières pour trouver les valeurs de $`\beta`$ et $`\gamma`$.

## Les ombres

Notre première implémentation de l'illumination diffuse est trop simpliste : elle est en effet locale, 
se calcule sans tenir compte des autres éléments de la scène. Des objets peuvent par exemple cacher
la source de lumière.
Pour déterminer si une source de lumière doit être comptabilisée, il suffit de vérifier si un objet se
trouve entre le point d'intersection et la source de lumière.

Il est possible de réutiliser le calcul d'intersection fait en TP3, en utilisant comme "oeil" le point d'intersection et comme direction $`\vec{d}`$ la direction vers la source de lumière.

**Attention : le point sur lequel vous vous situez sera forcément une intersection qui sera trouvée.
Une solution est de vérifier que la distance de l'intersection est strictement positive (à un epsilon près).**

Afin de pouvoir générer les images du TP4 avec le même code que celui du TP5, nous allons rajouter une option, fausse par défaut, pour activer les ombres.

```
shadow true
```

## Vérification de la génération des scènes

Comme précédemment, ce sont les scripts `raytrace.sh` et `compare.sh` qui sont utilisés pour vérifier que les images générées sont identiques aux images attendues.

Décommenter les tests liés dans le fichier `tests.sh` et le fichier `.gitlab-ci.yml`.

Une fois le travail réalisé, faire un ```commit``` puis un ```push``` de ce travail sur gitlab.

Vous pouvez vérifier sur [sonarqube](https://sonarqube.univ-artois.fr) si l'analyse automatique de votre code a relevé des violations des règles associées à votre langage. Si les remarques sont pertinentes, il faut corriger de manière appropriée votre code.

