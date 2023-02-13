# TP 8 : Pleine lumière sur les transformations, composition de transformations

## Ajout des sources de lumière pour le rendu des scènes

La semaine dernière, les scènes ne comportaient pas de sources de lumière. L'utilisation des matrices de transformation
était donc limité au calcul de l'intersection.

Cette semaine, les mêmes scènes sont illuminées à l'aide d'une lumière directionnelle. Il faudra que le calcul des normales
soit correct pour obtenir le rendu attendu.

## Composition des transformations

La semaine dernière, nous avons intégré une transformation unique par scène.

Cette semaine, nous allons permettre l'utilisation de compositions multiples dans une même scène.

Il n'y a pas de difficultés particulières à gérer des transformations multiples. Il suffit d'appliquer les
règles de transformation dans l'ordre dans lesquelles elles apparaissent dans le fichier de scène.

Par exemple, les transformations suivantes décrites dans le fichier de scène :

```
translate 1 1 1
rotate 0 0 1 45
scale 1 .5 1
```

correspondront à la transformation, soit une multiplication des nouvelles transformations à droite.

```math
M = T(1,1,1) \cdot R((0,0,1),45) \cdot S(1,.5,1)
```

Cependant, cette convention correspond à une lecture inverse des transformations : il faut d'abord appliquer le changement d'échelle, puis la rotation, et enfin la translation.

**Pour que les transformations soient appliquées dans l'ordre naturel de la scène, il suffirait de mutiplier les matrices de transformation à gauche, soit $`M = S(1,.5,1) \cdot R((0,0,1),45) \cdot T(1,1,1)`$. Cependant, nous disposons de scènes du Mooc d'EdX qui utilisent la multiplication à droite donc nous adopterons cette convention.**

Pour le fichier de scène suivant :
```
size 640 480

output TP8ex1.png

camera 0 0 6 0 0 0 0 1 0 45

directional 0 0 1 1 1 1

ambient 0 0 .1

translate 1 1 0
rotate 0 0 1 90
scale 1 .5 1

diffuse 0 0 .9
sphere 0 0 0 1
```

on obtient donc la scène :

![TP8ex1](TP8ex1.png)

Si on inverse les transformations, on obtient un autre résultat :

```
size 640 480

output TP8ex1.png

camera 0 0 6 0 0 0 0 1 0 45

directional 0 0 1 1 1 1

ambient 0 0 .1

scale 1 .5 1
rotate 0 0 1 90 
translate 1 1 0

diffuse 0 0 .9
sphere 0 0 0 1
```

va produire l'image

![TP8ex2](TP8ex2.png)

## Vérification de la génération des scènes

Comme précédemment, ce sont les scripts `raytrace.sh` et `compare.sh` qui sont utilisés pour vérifier que les images générées sont identiques aux images attendues.

Décommenter les tests liés dans le fichier `tests.sh` et le fichier `.gitlab-ci.yml`.

Une fois le travail réalisé, faire un ```commit``` puis un ```push``` de ce travail sur gitlab.

Vous pouvez vérifier sur [sonarqube](https://sonarqube.univ-artois.fr) si l'analyse automatique de votre code a relevé des violations des règles associées à votre langage. Si les remarques sont pertinentes, il faut corriger de manière appropriée votre code.

