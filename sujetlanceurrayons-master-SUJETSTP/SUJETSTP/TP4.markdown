# TP4 : Avec les couleurs, c'est mieux

On va maintenant prendre en compte une première façon de calculer la couleur des points de notre image.
Les rendus, sans être réalistes, seront déjà plus jolis.

## Prise en compte de la lumière diffuse

### Lumière d'ambiance : $`l_a`$

La lumière ambiante (`ambient` dans le fichier de description de scène) est ajoutée à tous les points de la scène.

### La réflexion diffuse (Johann Heinrich Lambert, Photometria 1760)

![Lambert](lambert.png)

La réflexion diffuse est un modèle qui considère que la lumière est réfléchie de manière identique dans toutes les directions.

L'intensité de la lumière est donc proportionnelle au cosinus de l'angle de la normale de la surface $`\vec{n}`$ et de la direction de la lumière $`\vec{ldir}`$.

Une source de lumière $`l`$ perpendiculaire à la surface sera d'intensité maximale alors qu'une source de lumière parallèle à la surface sera d'intensité nulle.

Si ce cosinus est négatif, sa valeur sera considérée comme nulle (utilisation d'un max).

La couleur diffuse d'un objet (`diffuse` dans le fichier de description de scène) est révélée par les différentes sources de lumières.

La couleur d'un point pour une source de lumière en utilisant la formule de Lambert est donc

```math
l_d = max(\vec{n}\cdot \vec{ldir},0) * lightcolor * couleur_{diffuse}
```

**Rappel : la normale d'un point d'intersection $`p = o + \vec{d}*t`$ avec une sphère de centre $`cc`$ est $`\vec{n}=\frac{p-cc}{||p-cc||}`$.**

## Couleur du point

La couleur finale $`coul`$ d'un point est donc de la forme

```math
coul = l_a + (\sum_i max(\vec{n}\cdot \vec{ldir_i},0) * lightcolor_i) * couleur_{diffuse}
```

où $`i`$ représente la $`ième`$ source de lumière.

## Les types de lumière

Les sources de lumière sont de deux types dans le fichier de description de scènes.

### Lumière directionnelle

Ces sources de lumière sont définies à partir d'un vecteur direction et d'une couleur (qui correspond en fait à la couleur et à la participation de la source à l'illumination globale).

```
directional 1 1 1 .6 .7 .7
```

représente une source de lumière directionnelle avec comme vecteur direction $`(1,1,1)`$ et comme couleur $`(.6,.7,.7)`$.

**Pour simplifier la conception du lanceur de rayon, la direction donnée dans la description est la direction du point à la source de lumière, soit l'opposé de la direction de la lumière.**

**Il ne faut pas oublier de normaliser ce vecteur direction.**

Le vecteur $`\vec{ldir}`$ est donc constant à  chaque point $`p`$ pour une lumière directionnelle, c'est le cas le plus simple.

### Lumière ponctuelle

Ces sources sont définies à partir d'un point origine et  d'une couleur (qui correspond en fait à la couleur et à la participation de la source à l'illumination globale).

```
point 1 1 1 .6 .7 .7
```

représente une source de lumière ponctuelle avec comme origine $`l = (1,1,1)`$ et comme couleur $`(.6,.7,.7)`$.

Le vecteur $`\vec{ldir}`$ pour une lumière ponctuelle doit donc être calculé pour chaque point $`p`$ : $`ldir = \frac{l-p}{||l-p||}`$. 

### Sources de lumière multiples

Dans nos scènes, les sources de lumière peuvent être multiples. Cependant, la somme des couleurs des sources de lumières ne peut pas dépasser $1$ sur les composantes.

```
directional 1 1 1 .6 .7 .7
point 1 1 1 .4 .3 .3
```

représente une source de lumière correcte car la somme des composantes des couleurs est toujours inférieure ou égale à 1.

```
directional 1 1 1 .6 .7 .7
point 1 1 1 .4 .1 .1
point -1 1 1 .2 .2 .2
```

est une déclaration incorrecte car la composante rouge de la somme des sources vaut $`1.2`$.

## Exemples de scènes

Les fichiers tests et les images [sont disponibles](../TP4).

### Une sphère simple

![Source directionnelle](tp41-dir.png)

![Source ponctuelle](tp41-point.png)

### Deux sphères sur un même plan

![Source directionnelle](tp42-dir.png)

![Source ponctuelle](tp42-point.png)

### Deux sources de lumière

![Sources multiples](tp43.png)

### Effet de profondeur

![Far far away](tp44.png)

### Deux couleurs

![Les oreilles bleues](tp45.png)

## Vérification de la génération des scènes

Comme précédemment, ce sont les scripts `raytrace.sh` et `compare.sh` qui sont utilisés pour vérifier que les images générées sont identiques aux images attendues.

Décommenter les tests liés dans le fichier `tests.sh` et le fichier `.gitlab-ci.yml`.

Une fois le travail réalisé, faire un ```commit``` puis un ```push``` de ce travail sur gitlab.

Vous pouvez vérifier sur [sonarqube](https://sonarqube.univ-artois.fr) si l'analyse automatique de votre code a relevé des violations des règles associées à votre langage. Si les remarques sont pertinentes, il faut corriger de manière appropriée votre code.

