# Phase initiale : mise en place des outils et utilitaires

> Le but de cette première phase est de mettre en place les outils que vous allez utiliser lors de ce module
> et de concevoir vos deux premiers programmes.
> Le projet s'effectue normalement en binôme, afin de développer des compétences dans l'utilisation d'outils collaboratifs comme gitlab.

## Mise en place du projet sur gitlab

Un outil indispensable pour un développeur est le gestionnaire de code. Il s'agit d'un outil qui permet de gérer les différentes versions des fichiers d'un projet. Dans notre cas, il s'agira avant tout de code source, mais l'on peut aussi gérer des fichiers de configuration, de la documentation, etc.

Nous allons utiliser plus précisément le gestionnaire de version distribué `git`. Cet outil, créé à la base par Linux Torvald pour gérer le code du noyau Linux, est devenu l'outil de choix d'un grand nombre de développeurs de part sa simplicité d'utilisation et sa puissance.

Nous apprendrons le fonctionnement de git au fur et à mesure des semaines. Voici pour l'instant les commandes de base que vous allez utiliser sur votre **dépôt local** : 

* ```git init``` permet de créer un dépôt git local dans le répertoire courant. Cette commande est utilisée pour chaque nouveau projet qui doit être géré par git. Le dépôt est local à votre machine, et ne nécessite ni accès internet ni serveur particulier pour fonctionner.
* ```git add file/dir``` permet d'ajouter un fichier ou un répertoire particulier dans le dépôt local. 
* ```git commit -a``` permet d'enregistrer les modifications courantes dans le dépôt local. 
* ```git stash``` permet de mettre les dernière modifications locales sur une pile et de revenir au dernier état sauvegardé.
* ```git stash apply``` permet d'appliquer les changements qui se trouvent sur le haut de la pile sur la copie de travail courante

L'intérêt d'un gestionnaire de version décentralisé comme ```git``` est que chaque développeur contient une copie complète du dépôt, ce qui lui permet d'être autonome.

Cependant, le travail à plusieurs sur un projet demande une mise en commun du travail accompli régulièrement. Il faut donc aussi un dépôt central qui sera synchronisé avec les dépôts locaux.

A l'université d'Artois, nous disposons d'une instance de l'outil Gitlab pour gérer des dépôts ```git``` centralisés. Il est disponible à l'adresse http://gitlab.univ-artois.fr/. Il est accessible à l'aide de vos identifiants ENT habituels.

![gitlabartois1](gitlabartois1.png)

La première chose à faire est **que l'un des binômes** duplique le projet [lanceurrayon](https://gitlab.univ-artois.fr/lanceurrayons/codelanceurrayons.git).

![lanceurrayons](gitlabartois2.png)


Il faut ensuite inviter l'autre membre du binôme pour ce projet. Cela se fait à l'aide du bouton "Settings" et de l'onglet "Members". **Seules les personnes qui se sont déjà connectées à gitlab apparaissent dans la liste des membres.**

![gitlabartois4](gitlabartois4.png)

Une dernière modification à faire est de demander à gitlab d'utiliser un clone du projet à chaque intégration continue, dans le menu `Paramètres/Paramètres CI CD/Pipelines généraux`.

![clone ci](gitlabclone.png)

La première fois que vous utilisez git, il faut vous identifier auprès du client git en fournissant une adresse email et un nom :

* ```git config --global user.email prenom_nom@ens.univ-artois.fr```
* ```git config --global user.name "Prenom Nom"```

Lorsque vous êtes à la faculté des sciences, il faut indiquer à git que l'on utilise un proxy

* ```git config --global http.proxy http://cache-etu.univ-artois.fr:3128```

De plus, comme nous utilisons une connexion https, il faut augmenter la taille des messages HTTP :

* ```git config --global http.postBuffer 524288000```

Enfin, pour éviter de taper trop souvent votre mot de passe, vous pouvez indiquer à git de garder
vos identifiants dans un cache (pendant 15 minutes).

* ```git config --global credential.helper cache```

## Récupération d'un projet partagé dans Eclipse

Eclipse a un support intégré pour git. Il suffit d'importer votre projet à partir de l'espace de travail pour pouvoir travailler directement sur votre projet à l'aide d'Eclipse.

* Vérifier que le proxy est correctement déclaré sous Eclipse (rechercher "proxy" dans les préférences d'Eclipse).
* Copier l'URI HTTPS de votre projet dans le presse papier
* Faire `Import.../Projects from git/clone URI` : le contenu du presse papier doit être ajouté automatiquement aux champs du formulaire git. Renseigner les champs identifiant et mot de passe.
* Le dépot git doit maintenant se trouver dans votre répertoire personnel dans le répertoire `git`.

La décoration du projet doit être ```[git main]```.


##  Récupération d'un projet partagé "à la console"

Il suffit de se positionner dans le répertoire de travail et de taper la commande ```git clone https://gitlab.univ-artois.fr/<VOTRE.LOGIN>/codelanceurrayons.git```.


## Conventions de codage, vulnérabilités, erreurs de programmation

> L'important quand on travaille en groupe est de respecter des conventions de
> codage pour permettre une meilleure compréhension et appropriation du code.
> L'outil [SonarQube](http://www.sonarqube.org/) est un outil d'analyse statique
> de code multi-langage qui permet de vérifier que le code respecte les 
> préconisations de chaque langage et l'absence de bugs, de maladresses
> ou de vulnérabilités répandus.


Un fichier de configuration `sonar-project.properties` doit apparaître dans votre dépôt git. 
Il s'agit d'un fichier permettant de configurer leur projet pour être analysé par 
[l'instance locale de SonarQube à l'Artois](http://sonarqube.univ-artois.fr/).

Vous vous identifiez via gitlab sur cet outil.

![identification](sonarqube1.png)

Pour permettre à l'intégration continue de nous identifier via l'API de sonar,
il faut créer un jeton (_token_) qui sera utilisé spécifiquement pour cela.
Cela se fait à partir de son compte personnel sur sonarqube :

![moncompte](sonarqube2.png)

Les jetons sont disponibles dans la partie `sécurité`.

![sécurité](sonarqube3.png)

Attention, les jetons ne sont visibles que lorsqu'ils sont créés. Vous devez les
copier pour pouvoir les réutiliser.

![jeton](sonarqube4.png)

Il suffit ensuite de déclarer une variable `SONARTOKEN` dans votre projet gitlab, dans le menu `Paramètres/Paramètres CI CD/Variables`.

![jeton](sonarqube5.png)

Le fichier `sonar.properties` doit indiquer dans quel répertoire se trouve le code source du projet, 
en modifiant la valeur associée à `sonar.sources`. Par défaut, il s'agit du répertoire `src`.

Normalement, le langage utilisé est automatiquement détecté.

Pour lancer l'audit de code avec l'intégration continue, décommenter les lignes suivantes dans le fichier `.gitlab-ci.yml`.

```yaml
 auditcode:
   image: cache-ili.univ-artois.fr/proxy_cache/sonarsource/sonar-scanner-cli
   stage: qa
   script: "sonar-scanner $PROXY $SONARINFO"
```

Lors de votre prochain dépôt sur gitlab, un rapport spécifique sera généré pour votre projet.

Vous devez voir un nouveau job `auditcode` apparaître dans votre projet.

En étudiant son contenu, vous trouverez un lien vers votre projet sur Sonar :
```
...
INFO: Sensor SonarCSS Rules [cssfamily]
INFO: No CSS, PHP, HTML or VueJS files are found in the project. CSS analysis is skipped.
INFO: Sensor SonarCSS Rules [cssfamily] (done) | time=0ms
INFO: Sensor JavaXmlSensor [java]
INFO: Sensor JavaXmlSensor [java] (done) | time=1ms
INFO: Sensor JaCoCo XML Report Importer [jacoco]
INFO: Sensor JaCoCo XML Report Importer [jacoco] (done) | time=1ms
INFO: ------------- Run sensors on project
INFO: Sensor Zero Coverage Sensor
INFO: Sensor Zero Coverage Sensor (done) | time=0ms
INFO: Calculating CPD for 0 files
INFO: CPD calculation finished
INFO: Analysis report generated in 50ms, dir size=104 KB
INFO: Analysis report compressed in 7ms, zip size=13 KB
INFO: Analysis report uploaded in 66ms
INFO: ANALYSIS SUCCESSFUL, you can browse https://sonarqube.univ-artois.fr/dashboard?id=tracer2013
INFO: Note that you will be able to access the updated dashboard once the server has processed the submitted analysis report
```

