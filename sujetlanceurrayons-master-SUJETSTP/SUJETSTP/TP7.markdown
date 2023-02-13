# Utilisation des transformations

Il est important pour la création de scènes complexes de prendre en compte des transformations de base sur les objets
(translation, changement d'échelle, rotation). Nous allons intégrer cela dans notre lanceur de rayons, à l'aide d'opérations sur des matrices.

## Calcul matriciel

Les scènes seront conçues à l'aide de transformations (translation, rotation, homothétie) qui seront représentées par des matrices 4x4. Ces matrices seront appliquées sur des vecteurs de taille 4 représentant des points (x,y,z,1) ou des vecteurs (u,v,w,0).

Vous devez donc réaliser une implémentation d'une matrice 4x4 permettant :

* d'ajouter, soustraire, multiplier des matrices 4x4
* multiplier une matrice par un vecteur de dimension 4
* transposer une matrice
* calculer le déterminant d'une matrice
* inverser une matrice

### Calcul du déterminant

Le calcul du déterminant peut se faire à l'aide de la matrice des cofacteurs à l'aide de la formule de Laplace.

Les éléments de la matrice des cofacteurs sont les déterminants des sous-matrices obtenues en éliminant la ligne $`i`$ et la colone $`j`$ de la cellule considérée,
multipliés par $`(-1)^{i+j}`$.

```
det | a  b | = a * det(|d |) - b * det(|c|) = ad - bc
    | c  d |

    | a b c |
det | d e f | = a * det( | e f |) - b * det( |d f|) + c * det(|d e|)
    | g h i |            | h i |             |g i|            |g h|


              = a * e * i - a * f * h - b * d * i + b * f * g + c * d * h - c * e * g

     |a b c d|           |f g h|           |e g h|           |e f h|           |e f g|
det  |e f g h| = a * det |j k l| - b * det |i k l| + c * det |i j l| - d * det |i j k|
     |i j k l|           |n o p|           |m o p|           |m n p|           |m n o|
     |m n o p|
```

### Inversion d'une matrice

L'invertion d'une matrice $`inv(A) = \frac{1}{det(A)}*adj(A)`$
avec $`adj(A)`$ la matrice transposée des cofacteurs (comatrice en français, _adjugate matrix_ en anglais).

```
Adj | a  b | = | d -c |t = |d -b|
    | c  d |   | -b a |    |-c a|
```

Voir par exemple [cette page sur wikipedia](https://fr.wikipedia.org/wiki/Comatrice) .

## Les matrices des différentes transformations

Les matrices de transformation sont des matrices 4x4. Il faudra donc transformer nos points et nos vecteurs de dimensions 3 en une structure de dimension 4.
On ajoutera pour cela une quatrième composante $`w`$ aux points et aux vecteurs de telle sorte que :

+ $w = 0$ pour les vecteurs
+ $w = 1$ pour les points

Par exemple, le point $`p = \begin{pmatrix}1\\2\\0\end{pmatrix}`$ sera transformé en $`p'= \begin{pmatrix}1\\2\\0\\1\end{pmatrix}`$ et le vecteur $`\vec{v} = \begin{pmatrix}0\\1\\0\end{pmatrix}`$ sera transformé en $`\vec{v'} = \begin{pmatrix}0\\1\\0\\0\end{pmatrix}`$.

Pour retrouver une structure de dimension 3 à partir d'un résultat en dimension 4, on récupèrera simplement les trois premières composantes du résultat.

Ce passage de dimension 3 à dimension 4 correspond à l'utilisation de [coordonnées homogènes](https://fr.wikipedia.org/wiki/Coordonnées_homogènes).

### Translation

La matrice de translation est simple à définir, **mais nécessite de travailler en dimension 4**. Elle est définie à partir du vecteur $`\vec{t} = \begin{pmatrix}tx\\ty\\tz\end{pmatrix}`$ représentant la translation de la façon suivante :

```math
T(\vec{t}) =
\begin{vmatrix}
1 & 0 & 0 & tx\\
0 & 1 & 0 & ty\\
0 & 0 & 1 & tz\\
0 & 0 & 0 & 1\\
\end{vmatrix}
```

La matrice de translation a pour particularité de ne pas déplacer les vecteurs, car leur composante $`w=0`$.

+ $`T((1,1,1)) . p' = \begin{vmatrix}1 & 0 & 0 & 1\\0 & 1 & 0 & 1\\0 & 0 & 1 & 1\\0 & 0 & 0 & 1\end{vmatrix} \cdot \begin{pmatrix}1\\2\\0\\1\end{pmatrix} = \begin{pmatrix}2\\3\\1\\1\end{pmatrix}`$
+ $`T((1,1,1)) . v' = \begin{vmatrix}1 & 0 & 0 & 1\\0 & 1 & 0 & 1\\0 & 0 & 1 & 1\\0 & 0 & 0 & 1\end{vmatrix} \cdot \begin{pmatrix}0\\1\\0\\0\end{pmatrix}\begin{pmatrix}0\\1\\0\\0\end{pmatrix}`$


### Homothétie (_scaling_)

La matrice d'homothétie n'est pas plus compliquée : il s'agit simplement de multiplier chaque composante par un scalaire spécifique. Ces scalaires seront donnés sous la forme d'un vecteur $`\vec{s} = \begin{pmatrix}sx\\sy\\sz\end{pmatrix}`$.

```math
S(\vec{s}) =
\begin{vmatrix}
sx & 0 & 0 & 0\\
0 & sy & 0 & 0\\
0 & 0 & sz & 0\\
0 & 0 & 0 & 1\\
\end{vmatrix}
```

### Rotation

#### Selon l'axe des $`x`$

```math
R_x(\theta) =
\begin{vmatrix}
1 & 0 & 0 & 0\\
0 & cos(\theta) & -sin(\theta) & 0\\
0 & sin(\theta) & cos(\theta) & 0\\
0 & 0 & 0 & 1\\
\end{vmatrix}
```

#### Selon l'axe des $`y`$

```math
R_y(\theta) =
\begin{vmatrix}
cos(\theta) & 0 & sin(\theta) & 0\\
0 & 1 & 0 & 0\\
-sin(\theta) & 0 & cos(\theta) & 0\\
0 & 0 & 0 & 1\\
\end{vmatrix}
```

#### Selon l'axe des $`z`$

```math
R_z(\theta) =
\begin{vmatrix}
cos(\theta) & -sin(\theta) & 0 & 0\\
sin(\theta) & cos(\theta) & 0 & 0\\
0 & 0 & 1 & 0\\
0 & 0 & 0 & 1\\
\end{vmatrix}
```

#### Selon un axe quelconque $`\vec{v}`$

Le principe de la rotation d'un angle $`\theta`$ à partir d'un axe $`\vec{v}`$ quelconque est basé sur [la formule de rotation de Rodrigues](http://fr.wikipedia.org/wiki/Rotation_vectorielle) :

```math
w_{rotated} = \vec{w} * cos(\theta) + \vec{v} \times \vec{w} * sin(\theta) + \vec{v}*(\vec{v}\cdot \vec{w})*(1 - cos(\theta))
```

Le produit vectoriel $`\vec{v} \times \vec{w}`$ peut être défini par le produit de la matrice $`V`$ avec le vecteur $`\vec{w}`$ avec

```math
V =
\begin{vmatrix}
0 & -v_z & v_y\\
v_z & 0 & -v_x\\
-v_y & v_x & 0
\end{vmatrix}
```


Ces étapes peuvent se résumer dans la matrice suivante :

```math
R(\vec{v},\theta) = I_3*cos(\theta) + M(\vec{v}) \cdot (1-cos(\theta)) + M'(\vec{v}) \cdot sin(\theta)
```

où

```math
M(\vec{v}) = 
\begin{vmatrix}
v_x^2 & v_x \cdot v_y & v_x \cdot v_z \\
v_x \cdot v_y & v_y^2 & v_y \cdot v_z \\
v_x \cdot v_z & v_y\cdot v_z & v_z^2 \\
\end{vmatrix}
```

et

```math
M'(\vec{v}) = 
\begin{vmatrix}
0 & -v_z & v_y \\
v_z & 0 & -v_x \\
-v_y & v_x & 0 \\
\end{vmatrix}
```

Cette matrice 3x3 doit être transformée en matrice 4x4. On obtient au final la matrice :


```math
\begin{vmatrix}
cos(\theta) + v_x^2 \cdot (1 - cos(\theta))              &   v_x \cdot v_y \cdot (1-cos(\theta)) - v_z \cdot sin(\theta) &  v_x \cdot v_z \cdot (1-cos(\theta)) + v_y \cdot sin(\theta)   & 0 \\
v_x \cdot v_y \cdot  (1 - cos(\theta)) + v_z \cdot sin(\theta)   & cos(\theta) + v_y^2 \cdot (1-cos(\theta))             & v_y \cdot v_z \cdot (1 - cos(\theta)) - v_x \cdot sin(\theta)  & 0 \\
v_x \cdot v_z \cdot  (1 - cos(\theta)) - v_y \cdot sin(\theta)   &  v_y \cdot v_z \cdot (1-cos(\theta)) + v_x \cdot sin(\theta)  & cos(\theta) +  v_z^2 \cdot (1 - cos(\theta))                                       & 0\\
 0 & 0 & 0 & 1 \\
\end{vmatrix}
```

## Importance de l'ordre des transformations

L'ordre des transformations donne généralement des résultats différents : ces opérations ne commutent généralement pas.

### Cas commutatifs (ordre indifférent)

+ L'application répétée de $`T`$ ou de $`S`$ commute
+ $`R`$ et $`S`$ commutent ssi $`S`$ est uniforme, i.e. $`S = S(\vec{v})`$ avec $`v= \begin{pmatrix}k\\k\\k\end{pmatrix}`$ .

Exemple :

```math
R_z(90) =
\begin{vmatrix}
0 & -1 & 0 & 0\\
1 & 0 & 0 & 0\\
0 & 0 & 1 & 0\\
0 & 0 & 0 & 1\\
\end{vmatrix}
```

```math
S(2,2,0) =
\begin{vmatrix}
2 & 0 & 0 & 0\\
0 & 2 & 0 & 0\\
0 & 0 & 1 & 0\\
0 & 0 & 0 & 1\\
\end{vmatrix}
```

```math
R_z(90) \cdot S(2,2,0) =
\begin{vmatrix}
0 & -1 & 0 & 0\\
1 & 0 & 0 & 0\\
0 & 0 & 1 & 0\\
0 & 0 & 0 & 1\\
\end{vmatrix}
\cdot
\begin{vmatrix}
2 & 0 & 0 & 0\\
0 & 2 & 0 & 0\\
0 & 0 & 1 & 0\\
0 & 0 & 0 & 1\\
\end{vmatrix}
=
\begin{vmatrix}
0 & -2 & 0 & 0\\
2 & 0 & 0 & 0\\
0 & 0 & 1 & 0\\
0 & 0 & 0 & 1\\
\end{vmatrix}
```

### Cas non commutatifs (ordre important)

+ $`R`$ et $`S`$ ne commutent pas ssi $`S`$ est non uniforme.

+ L'application répétée de $`R`$ ne commute pas.

Exemple : $`R_x(90) \cdot R_y(90) \neq R_y(90) \cdot R_x(90)`$

## Application des transformations sur les objets

### Principes

Les points sont modifiés par la matrice de transformation.

```math
p' = M \cdot p
```

Les normales doivent être traitées spécifiquement

```math
n' = {M^{-1}}^t \cdot n
```

### Cas du triangle

Il suffit de transformer les trois points du triangle pour obtenir un calcul d'intersection correct.

Le calcul de la normale à partir des points transformés est aussi correct.

### Cas de la sphère

Il faut revenir à une sphère non transformée pour faire le calcul d'intersection.

On cherche la valeur $`t'`$ pour le point transformé $`p' = o + t'\cdot\vec{d}`$.

Cela revient à chercher la valeur de $`t`$ dans l'objet non transformé :

```math
p = M^{-1} \cdot p' =  M^{-1} \cdot o + t\cdot M^{-1} \cdot \vec{d}
```

Une fois $`t`$ trouvé, il faut en déduire $`t'`$.

```math
p' = M \cdot p
```

```math
t' = \frac{(p' - o)_x}{\vec{d}_x}
```

**Attention, il faut trouver une composante pour laquelle la division est possible.**

Calcul de la normale

On calcule le point $`p`$ non transformé à partir du point d'intersection $`p'`$ :

```math
p = M^{-1} p'
```

On calcule la normale $`n = \frac{p - c}{||p - c||}`$ où $`c`$ est le centre de la sphère.

On calcule $`n' = {M^{-1}}^t \cdot n`$.

## Ajout des transformations dans le fichier de scènes

Les transformations seront déclarées de la façon suivante dans le fichier de description de scène :

```
# translate <vector>
translate 1 2 3
# scale <vector>
scale .5 .2 3
# rotate <vector> <angle>
rotate 0 1 0 90
```

Pour l'instant, les fichiers de description de scène seront simples : **une seule transformation maximum par fichier.**

*Dans la prochaine étape, nous introduirons la composition de transformations.*

## Vérification de la génération des scènes

Comme précédemment, ce sont les scripts `raytrace.sh` et `compare.sh` qui sont utilisés pour vérifier que les images générées sont identiques aux images attendues.

Décommenter les tests liés dans le fichier `tests.sh` et le fichier `.gitlab-ci.yml`.

Une fois le travail réalisé, faire un ```commit``` puis un ```push``` de ce travail sur gitlab.

Vous pouvez vérifier sur [sonarqube](https://sonarqube.univ-artois.fr) si l'analyse automatique de votre code a relevé des violations des règles associées à votre langage. Si les remarques sont pertinentes, il faut corriger de manière appropriée votre code.

