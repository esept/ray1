# Etape 1 : mise en place des outils et utilitaires

> Le but de cette première étape est de mettre en place les outils que vous allez utiliser lors de ce module
> et de concevoir vos deux premiers programmes.
> Le projet s'effectue normalement en binôme, afin de développer des
compétences dans l'utilisation d'outils collaboratifs comme gitlab.

## Réaliser une bibliothèque mathématique pour manipuler des triplets numériques

La plupart des opérations du lanceur de rayons se font sur des tuples de dimension 3 (des triplets). Les valeurs numériques seront représentées dans des doubles.

Les opérations à réaliser sur ses triplets sont : 

* Addition : $`(x_1, y_1, z_1) + (x_2, y_2, z_2) = (x_1 + x_2, y_1 + y_2, z_1 + z_2)`$
* Soustraction :  $`(x_1, y_1, z_1) - (x_2, y_2, z_2) = (x_1 - x_2, y_1 - y_2, z_1 - z_2`$
* Multiplication par un scalaire : $`d * (x_1, y_1, z_1) = (x_1, y_1, z_1) * d = (d*x_1, d*y_1, d*z_1`$
* Produit scalaire : $`(x_1, y_1, z_1) . (x_2, y_2, z_2) = x_1*x_2 + y_1*y_2 + z_1*z_2`$
* Produit vectoriel : $`(x_1, y_1, z_1) \times (x_2, y_2, z_2) = (y_1*z_2-z_1*y_2, z_1*x_2-x_1*z_2, x_1*y_2-y_1*x_2)`$
* Produit de Schur : $`(x_1, y_1, z_1) * (x_2, y_2, z_2) = (x_1*x_2, y_1*y_2, z_1*z_2)`$
* Longueur : $`||(x_1, y_1, z_1)|| = \sqrt{x_1*x_1 + y_1*y_1 + z_1*z_1}`$
* Normalisation : $`norm((x_1, y_1, z_1)) = \frac{1}{||(x_1, y_1, z_1)||}*(x_1, y_1, z_1)`$

D'un point de vue conception, on essayera de prendre en compte que toutes les opérations n'ont pas forcément de sens dans tous les contextes. Le tableau suivant récapitule les opérations possibles par type de données manipulées, qui correspondent tous à des triplets, mais qui ont
des sémantiques différentes.

| Opération | Point | Vecteur (directions, normales) | Couleur |
|-----------|-------|--------------------------------|---------|
| Addition |  | x | x |
| Soustraction | x | x | |
| Multiplication par un scalaire | x | x | x |
| Produit scalaire |  | x | |
| Produit vectoriel |  | x | |
| Produit de Schur |  |  | x |
| Longueur |  | x | |
| Normalisation |  | x | |


On notera de plus que la soustraction de deux points donne un vecteur et que l'addition d'un point et d'un vecteur donne un point.

1. Réaliser une première classe ```Triplet``` permettant de réaliser toutes les opérations.
2. Chercher un moyen de respecter les opérations par type de données manipulées.

Quand le travail est terminé : 

1. Ajouter la ou les classes au dépôt local.
1. Mettre à jour le dépôt local à l'aide d'un ```git pull```
1. Déposer les modification sur le dépôt distant à l'aide d'un ```git push```

## Test des calculs sur les triplets

Votre code va devoir passer des tests pour vérifier sommairement la réalisation des opérations 
sur les triplets.

Les tests sont basés sur un script exécutable `checktriplet.sh` qui doit se trouver à la racine
de votre projet.

Le testeur fonctionne de la manière suivante : chaque test est une chaîne de caractères de la forme
"OBJET1,opération,OBJET2". En découpant cette chaîne selon les `,`, on récupère facilement l'opération.

Les objets sont eux représentés sous une forme particulière, basée sur un préfixe :

* `P` pour point
* `V` pour vecteur
* `C` pour couleur

On pourra aussi utiliser des doubles pour OBJET2.

On utilisera les noms suivants pour représenter les différentes opérations :

| Opération | Nom |
|-----------|-------|
| Addition | `add` | 
| Soustraction | `sub` |
| Multiplication par un scalaire | `mul` |
| Produit scalaire | `dot` | 
| Produit vectoriel | `cross` | 
| Produit de Schur | `times` |
| Longueur | `len` | 
| Normalisation | `hat` | 


Quand une opération est permise, le résultat est retourné, en typant le résultat.

```
$ checktriplet.sh "P 1 1 1,add,V 3 3 3"
P 4.0 4.0 4.0
```

```
$ checktriplet.sh "P 1 1 1,mul,3"
P 3.0 3.0 3.0
```

Par contre, quand une opération n'est pas permise, on retournera `Interdit`.
```
$ checktriplet.sh "P 1 1 1,add,P 3 3 3"
Interdit
```

On pourra se baser sur le code suivant en Java pour réaliser le vérificateur de manière générique.

```java
    public static void main(String []args) {
        String [] data = args[0].split(",");
        String operation = data[1];
        Object o1 = buildObject(data[0]); // à concevoir
        Object o2 = buildObject(data[2]); // à concevoir
        try {
            Class<?> clazz2 = o2.getClass()==Double.class?double.class:o2.getClass();
            Object o3 = o1.getClass().getMethod(operation,clazz2).invoke(o1,o2);
            System.out.println(display(o3)); // à concevoir
        } catch (Exception e) {
            System.out.println("Interdit");
        }
    }
```

Ce code peut être adapté en C#. Par contre, il n'y a pas à ma connaissance de possibilité d'écrire un code équivalent en C++ (qui ne dispose pas de notion de [métaclasse](https://fr.wikipedia.org/wiki/Métaclasse)). Il faudra nous réaliser un code adhoc.


Vous pouvez ensuite tester votre travail localement (sur une machine unix) en lançant le script `tests.sh`.

Décommenter les lignes suivantes pour activer les tests sur les triplets :

```bash
echo "Tests de la bibliothèque mathématique"

assert "./checktriplet.sh \"P 1 1 1,add,P 2 2 2\"" "Interdit"
assert "./checktriplet.sh \"P 1 1 1,mul,P 2 2 2\"" "Interdit"
assert "./checktriplet.sh \"P 1 1 1,mul,2\"" "P 2.0 2.0 2.0"
assert "./checktriplet.sh \"P 1 1 1,sub,P 2 2 2\"" "V -1.0 -1.0 -1.0"
assert "./checktriplet.sh \"P 1 1 1,add,V 2 2 2\"" "P 3.0 3.0 3.0"
assert "./checktriplet.sh \"P 1 1 1,mul,V 2 2 2\"" "Interdit"
assert "./checktriplet.sh \"V 1 1 1,sub,V 2 2 2\"" "V -1.0 -1.0 -1.0"
assert "./checktriplet.sh \"V 1 1 1,dot,V 2 2 2\"" "6.0"
assert "./checktriplet.sh \"V 1 0 0,cross,V 0 1 0\"" "V 0.0 0.0 1.0"

assert_end regression
```

Pour lancer la vérification de votre travail avec l'intégration continue, décommenter les lignes suivantes dans le fichier `.gitlab-ci.yml`.

```yaml
 vectests:
   stage: initial
   script: "cd tests; ./tests2.sh"
```

Une fois le travail réalisé, faire un ```commit``` puis un ```push``` de ce travail sur gitlab.

Vous devez voir de nouveaux tests apparaître sur votre intégration continue.

Vous pouvez vérifier sur [sonarqube](https://sonarqube.univ-artois.fr) si l'analyse automatique de votre code a relevé des violations des règles associées à votre langage. Si les remarques sont pertinentes, il faut corriger de manière appropriée votre code.

