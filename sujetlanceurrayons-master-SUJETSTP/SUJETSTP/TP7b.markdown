# Avant d'aller plus loin, il faut du code objet

A la lecture du code de plusieurs groupes, il s'avère que
certains lanceurs de rayon ne sont pas conçus dans les règles
de la programmation orientée objet.

Un programme mal conçu est difficilement maintenable et difficile
à faire évoluer.

Voici quelques règles simples pour corriger votre conception et rendre votre code plus objet.


## Des classes et des objets

En POO, on manipule généralement des objets, c'est à dire des instances de
classes particulières. 

Dans un raytracer, les objets sont les points, vecteurs, couleurs, objets de la scène, etc.

Vous devez vérifier les cas suivants :

+ Les attributs doivent être privés, à moins qu'ils soient non modifiables (final)
+ Les noms des méthodes doivent être normalisés et avoir un sens.


## Polymorphisme

Le lanceur de rayons ne doit pas traiter de manière différente un triangle, une sphère ou un plan : ce sont ces objets qui doivent réagir de manière adaptée aux messages du lanceur de rayon.

Si votre code contient du code spécifique à une forme géométrique en dehors de la classe qui le représente, il faut déplacer ce code dans la classe appropriée.

## Lisibilité du code

Il est important pour pouvoir vérifier les formules utilisées de nommer les
variables d'une façon similaire au support de TP.

## Conventions de codage

+ Les noms des attributs d'une classe doivent commencer par une lettre minuscule.
+ Les noms des méthodes doivent commencer par une minuscule.

## Méthodes d'instance vs méthodes de classe (static)

Si vous avez dans une classe une méthode qui n'utilise que ces paramètres,
cette méthode est indépendante de l'état de l'objet, donc devrait être déclarée
comme une méthode de classe (static).

Exemple :
```
 public Vector moins(Point p1, Point p2) {
        return new Vector(p1.x-p2.x,p1.y-p2.y,p1.z-p2.z);
 }
```

 se transforme en

```
  public static Vector moins(Point p1, Point p2) {
         return new Vector(p1.x-p2.x,p1.y-p2.y,p1.z-p2.z);
  }
```

Pour être plus objet, votre code devrait déplacer cette méthode dans la classe Point.

```
   public Vector moins(Point p) {
         return new Vector(x-p.x,y-p.y,z-p.z);
   }
```
