# Phase initiale : mise en place des outils et utilitaires

> Le but de cette première phase est de mettre en place les outils que vous allez utiliser lors de ce module
> et de concevoir vos deux premiers programmes.
> Le projet s'effectue normalement en binôme, afin de développer des compétences dans l'utilisation d'outils collaboratifs comme gitlab.

## Réaliser un comparateur d'images pixel par pixel

Le premier travail à réaliser est un comparateur d'image. Notre lanceur de rayons va générer des images.
Elles seront comparées à des images de référence pour vérifier son 
bon fonctionnement.

Nous utiliserons un format d'image ouvert, non destructeur, le [PNG](http://en.wikipedia.org/wiki/Portable_Network_Graphics).

La plupart des langages disposent de bibliothèques pour gérer des images dans ce format.

La comparaison de deux images est aisée : il suffit de comparer les deux images pixel par pixel, et de compter les pixels différents.
Si les deux images diffèrent de moins de 1000 pixels, alors elles seront considérées comme identiques. En effet, dans certains modèle d'illumination, selon le langage utilisé, et la manière d'effectuer les calculs, la couleur des points peut varier d'une unité sur l'une des composantes. On affichera le nombre de pixels différents comme information complémentaire.

Pour rendre la comparaison des deux images plus simple, on générera une image qui représente la différence entre les deux images si elles diffèrent d'au moins un pixel. Un pixel noir représentera un pixel identique dans les deux images. La couleur des autres pixel dépendra de la différence de couleur entre deux pixels.

Par exemple, si l'on compare les deux images suivantes :

![image1](image1.png)

et

![image2](image2.png)

le comparateur doit permettre d'obtenir l'image suivante :

![diff](diff.png)

Le comparateur doit afficher deux lignes : la première doit contenir OK si les deux images sont identiques et KO sinon. La deuxième ligne doit expliciter combien de pixels différents sont observés.

Pour que l'utilisation du comparateur soit identique quelque soit le langage choisi, on créera un script shell `compare.sh` pour lancer la comparaison.

Voici deux exemples d'utilisation du script :

Si l'on considère les deux images précédentes, on obtient ceci :

```
./compare.sh image1.png image2.png 
OK
879
```
Les images ne sont pas identiques mais diffèrent de moins de 1000 pixels. On considère qu'elles sont proches.

Si maintenant on compare la première image à celle-ci : 

![image3](image3.png)

alors on obtient la sortie suivante :
```
./compare.sh image1.png image3.png 
KO
307200
```

Les images sont considérées comme différentes.

Voici l'image de différence `diff.png` qui doit être générée par le comparateur :

![diff2](diff2.png)

Vous disposez d'un script de test local, nommé `tests.sh`, qui vous permet d'exécuter en local des tests similaires 
à ceux utilisés lors de l'intégration continue.

Les tests sont commentés, il faut les décommenter pour chaque étape du projet.

Décommenter les lignes suivantes dans le fichier `tests.sh` :

```bash
echo "Tests du comparateur d'images"

assert "./compare.sh TEST1/image1.png TEST1/image1.png" "OK\n0\n"
assert "./compare.sh TEST1/image2.png TEST1/image2.png" "OK\n0\n"
assert "./compare.sh TEST1/image1.png TEST1/image2.png" "OK\n879\n"
assert "cp diff.png localdiff.png"
assert "./compare.sh TEST1/diff.png localdiff.png" "OK\n0\n"

assert_end regression
```

Pour lancer la vérification de votre travail avec l'intégration continue, décommenter les lignes suivantes dans le fichier `.gitlab-ci.yml`.

```yaml
 comparateur:
   stage: initial
   script: "cd tests; ./tests1.sh"
```

Lancer les tests locaux à l'aide de la commande `./tests.sh`.
Ici, il va faire des vérifications des comparaisons des images 1 et 2.


Lorsque les tests locaux passent, faire un ```commit``` puis un ```push``` de ce travail sur gitlab.

**Votre projet est configuré pour exécuter automatiquement des tests appelant le script `compare.sh` : c'est ce que l'on nomme [intégration continue](https://fr.wikipedia.org/wiki/Intégration_continue).**

L'intégration continue est similaire à votre script de test et il comporte aussi la vérification du résultat avec l'image 3.

**Les tests de l'intégration continue sont donc généralement plus complets que les tests que vous avez localement.**

Vous pouvez vérifier sur [sonarqube](https://sonarqube.univ-artois.fr) si l'analyse automatique de votre code a relevé des violations des règles associées à votre langage. Si les remarques sont pertinentes, il faut corriger de manière appropriée votre code.

Voici quelques liens pour vous aider à réaliser ce programme.

### Java

La gestion des images est intégrée à la bibliothèque standard. Vous pouvez consulter la section 
[Manipulation des images en Java](https://docs.oracle.com/javase/tutorial/2d/images/) du tutoriel officiel du langage pour obtenir des informations sur la manipulation des images à l'aide de Java2D.

### C/C++

Il existe de nombreux outils de gestion d'images en C/C++. La bibliothèque 
* [Free Image](http://freeimage.sourceforge.net) est libre et assez simple à utiliser.

 
### Python

A priori, la bibliothèque la plus simple pour manipuler des images en python serait [Pillow](http://python-pillow.github.io).

