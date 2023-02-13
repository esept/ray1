# Phase basique : Lecture des fichiers textes représentant les scènes 3D

> Dans ce travail, il faut récupérer les principaux éléments de la scène
> à partir d'un fichier texte. Les premières images seront produites
> à la prochaine étape. Vous pouvez proposer des
> fichiers de scènes simples en vous basant sur les exemples fournis ci-après.


Les scènes vont être décrites dans un format spécifique de fichier utilisé dans le MOOC [Foundations of Computer Graphics](https://www.edx.org/course/foundations-computer-graphics-uc-berkeleyx-cs184-1x#.VMEvxsY5yQs).

```
# Les lignes qui commencent par # sont des commentaires,
# elles doivent être ignorées.

# La premiere information (obligatoire), est la taille de l'image 
# qui doit être générée, largeur puis hauteur.

size 640 480 

# Ensuite vient le nom du fichier dans lequel l'image est générée
# Si cette information n'est pas donnée, ce sera output.png

output mascene.png

# La position de la caméra.
# camera x y z u v w m n o f
# Les trois premières valeurs correspondent à la position de l'oeil -- look from -- (x,y,z)
# Les trois suivantes correspondent au point visé par l'oeil -- look at -- (u,v,w)
# Les trois suivantes correspondent à la direction vers le haut de l'oeil -- up -- (m,n,o)
# La dernière correspond à l'angle de vue -- field of view, fov -- f, en degrés
#
# La caméra est positionnée en (0,0,4), regarde le centre de la scène (0,0,0),
# la position haute suivant l'axe des y (0,1,0), avec un angle de vue de 45°
camera 0 0 4 0 0 0 0 1 0 45


# ensuite, apparaissent les informations de couleur
# ambient la couleur ambiante, en (r,g,b) 
# diffuse la couleur de l'objet en (r,g,b)
# specular la lumière réfléchie (effet miroir) en (r,g,b)
#
# IMPORTANT : il faut vérifier que (ambiant + diffuse) ne dépasse pas 1 sur chaque composante.
# Si c'est le cas, lancer une exception (entrée incorrecte).
ambient .1 .1 .1
diffuse 0.9 0 0 
specular 0 0 0
shininess 10

# Les couleurs diffuse et specular peuvent être déclarées à tout moment dans le fichier, à de multiples reprises.
# Dans ce cas, la dernière déclaration d'applique à l'objet défini.
# C'est aussi le cas pour shininess qui correspond à un entier positif

# puis viennent les lumières 
# directional (x,y,z) (r,g,b) indique une lumière globale directionnelle
# ou (x,y,z) représente une direction et (r,g,b) une couleur.
directional 0 0 1 .5 .5 .5 
# point (x,y,z) (r,g,b) indique une source de lumière locale, d'origine 
# un point (x,y,z) et de couleur (r,g,b)
point 4 0 4 .5 .5 .5

# Il peut y avoir plusieurs sources de lumières de chaque type, ou aucune.
# IMPORTANT : il faut vérifier que la somme des couleurs des sources de
# lumière ne dépasse pas 1 sur une des composantes. Lancer une exception sinon.


# Ensuite on va décrire les objets dans la scène
# On dispose de deux objets de base : la sphère et le triangle.
# Les triangles sont définis à partir de trois points.
# Pour éviter d'avoir à mettre 3 coordonnées par définition de triangle,
# on va définir en avance des points, et les triangles seront ensuite
# définis par trois points.

# Il faut définir en avance le nom de points (ici 4)
maxverts 4 

# ensuite chaque point est donné par ses coordonnées (pas forcément entières)
# vertex x y z pour un point de coordonnées (x,y,z)

vertex -1 -1 0 
vertex +1 -1 0
vertex +1 +1 0
vertex -1 +1 0

# On peut maintenant définir des formes géométriques à partir des points.
# Les points sont référencés par leur indice de déclaration, à partir de 0.
# Toutes les formes sont créées à partir de triangles.

# On déclare deux triangles pour faire un carré
# un triangle de coordonnées (-1,-1,0), (+1,-1,0) et (+1,+1,0)
tri 0 1 2
tri 0 2 3

# IMPORTANT : il faut vérifier que les indices sont strictement inférieurs
# à maxverts

# 
# On déclare une sphere à partir de son centre et de son rayon
# sphere x y z r 
# pour une sphere de centre (x,y,z) et de rayon r
sphere 0 1 0 0.5

#
# On déclare un plan à partir d'un point de ce plan et d'une normale à ce plan.
# plane x y z u v w
# pour un plan qui passe par le point (x,y,z) et dont la normale est (u,v,w)
plane 0 -1 0 0 1 0
```


Voici quelques exemples de fichiers simples corrects : 

### Une sphère rouge

Une sphère rouge centrée à l'origine, rouge car iluminée par une couleur ambiante rouge.
    
```
size 640 480
output exemple1.png
camera 0 0 4 0 0 0 0 1 0 45

ambient 1 0 0

sphere 0 0 0 1
```

![exemple1](../TP2/exemple1.png)

### Un triangle bleu

Un exemple simple de déclaration d'un triangle à partir de trois points.

```
size 640 480
output exemple2.png
camera 0 0 4 0 0 0 0 1 0 45

ambient 0 0 1

maxverts 3

vertex +1 +1 0
vertex +1 -1 0
vertex -1 -1 0

tri 0 1 2
```

![exemple2](../TP2/exemple2.png)

### Effet de lumière directionnelle

Une source de lumière directionnelle sur la droite de l'image.
Sans source de lumière, l'image serait complètement noire.

```
size 640 480
output exemple3.png
camera 0 0 4 0 0 0 0 1 0 45

diffuse 1 0 0
directional 1 1 1 1 1 1

sphere 0 0 0 1
```

![exemple3](../TP2/exemple3.png)

### Effet de lumière ponctuelle

Une source de lumière ponctuelle, à gauche de l'image.

```
size 640 480
output exemple4.png
camera 0 0 4 0 0 0 0 1 0 45

diffuse 1 0 0
point -1 1 1 1 1 1

sphere 0 0 0 1
```

![exemple4](../TP2/exemple4.png)

### Deux sources de lumière

Dans cet exemple, les deux sources de lumière des exemples précédents illuminent la scène.
Noter bien que les couleurs (1,1,1) sont maintenant (.5,.5,.5) pour éviter que leur somme ne dépasse (1,1,1).

```
size 640 480
output exemple5.png
camera 0 0 4 0 0 0 0 1 0 45

diffuse 1 0 0
directional 1 1 1 .5 .5 .5
point -1 1 1 .5 .5 .5

sphere 0 0 0 1
```

![exemple5](../TP2/exemple5.png)

### Plusieurs couleurs

Dans cet exemple, on utilise une lumière ambiante et une couleur
spécifique pour chaque objet. On note que le plan se comporte comme un miroir.

```
size 640 480
output spheres.png
camera 0 5 6 0 0 0 0 1 0 45

ambient 0.1 0.1 0.1
directional 1 1 1 1 1 1

# sphere rouge
diffuse 0.9 0 0
sphere -3 0 0 1

# sphere orange
diffuse .7 .23 0
sphere -1 0 0 1

# sphere jaune
diffuse .9 .9 0
sphere 1 0 0 1

# sphere verte
diffuse 0 .9 0
sphere 3 0 0 1

# le sol, réfléchissant
diffuse .2 .2 .2 
specular .1 .1 .1 
plane 0 -1 0 0 1 0
```

![spheres](../TP2/spheres.png)

## Vérification de la lecture des scènes

Un script `checkscene.sh` est maintenant attendu pour vérifier la lecture des fichiers de description de scène.

Le format de la sortie de ce script est le suivant :

- Le nom de fichier de sortie indiqué dans la scène
- le nombre de pixels de la scène (hauteur * largeur)
- le nombre d'objets graphiques déclarés
- le nombre de sources de lumières

Pour le fichier de scène suivant :

```
size 640 480
output tp31.png
camera 0 0 4 0 0 0 0 1 0 45
ambient 1 0 0

sphere 0 0 0 1
```

le résultat

```
tp31.png
307200
1
0
```

est attendu.


Vous pouvez ensuite tester votre travail localement (sur une machine unix) en lançant le script `tests.sh`.

Décommenter les tests liés dans le fichier `tests.sh` et le fichier `.gitlab-ci.yml`.

Une fois le travail réalisé, faire un ```commit``` puis un ```push``` de ce travail sur gitlab.


Vous pouvez vérifier sur [sonarqube](https://sonarqube.univ-artois.fr) si l'analyse automatique de votre code a relevé des violations des règles associées à votre langage. Si les remarques sont pertinentes, il faut corriger de manière appropriée votre code.

