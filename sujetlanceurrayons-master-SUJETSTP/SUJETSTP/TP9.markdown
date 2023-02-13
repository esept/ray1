# Etape 9 : transformations multiples avec contexte

Nous ajoutons maintenant la dernière touche à notre support des transformations.

Afin de pouvoir appliquer des transformations différentes aux divers objets de la scène,
il faut pouvoir effacer les transformations courantes. On utilisera pour cela une notion de contexte.
Les transformations vont être stockées sous forme d'une pile de matrices 4x4.
Chaque matrice correspond à un contexte. On utilisera les opérations classiques d'empilement (push) et dépilement (pop) pour changer de contexte.
La pile doit être initialisée à la matrice identité. 
Les transformations lues dans le fichier de description de scène sont appliquées à la matrice qui se trouve dans le contexte courant, sur le dessus de la pile.
Lors de la création d'un nouveau contexte (commande `pushTranform`), une copie de la matrice de transformation courante est ajoutée sur la pile.
Lors de la destruction d'un contexte (commande `popTransform`), la matrice courante est dépilée, la matrice suivante sur la pile devient la matrice courante.

Exemple :

```
size 640 480

camera 2 2 8 2 2 2 0 1 0 45

directional 1 1 1 1 1 1

diffuse .3 .3 .3
plane 0 0 -2 0 0 1

diffuse 0 1 1


translate 1 1 1
pushTransform
rotate 0 1 0 45
scale 1 1 2
sphere 0 0 0 1
popTransform
pushTransform
translate 2 2 2
scale .5 .5 .5
sphere 0 0 0 1
popTransform
```

La scène ci-dessus utilise une translation (1,1,1) qui est partagée pour les deux sphères.
La première sphère subit en plus une rotation et un changement d'échelle. La seconde sphère
subit une seconde translation et un passage à l'échelle. On obtient l'image suivante :

![exemplepush](exemplepush.png)

Voici l'évolution de la pile de contexte :
```
T(1,1,1)

pushTransform

T(1,1,1) * R(0,1,0,45) * S(1,1,2)
T(1,1,1)

popTransform

T(1,1,1)

pushTransform

T(1,1,1) * T(2,2,2) * S(.5,.5,.5)
T(1,1,1)

popTransform

T(1,1,1)
```

## Vérification de la génération des scènes

Comme précédemment, ce sont les scripts `raytrace.sh` et `compare.sh` qui sont utilisés pour vérifier que les images générées sont identiques aux images attendues.

Décommenter les tests liés dans le fichier `tests.sh` et le fichier `.gitlab-ci.yml`.

Une fois le travail réalisé, faire un ```commit``` puis un ```push``` de ce travail sur gitlab.

Vous pouvez vérifier sur [sonarqube](https://sonarqube.univ-artois.fr) si l'analyse automatique de votre code a relevé des violations des règles associées à votre langage. Si les remarques sont pertinentes, il faut corriger de manière appropriée votre code.

