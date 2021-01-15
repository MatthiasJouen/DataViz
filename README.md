# DataViz

version 1.0
#                                                                           Rapport d'analyse

### Sujet : 
Notre sujet traite des données liées à la Covid19. 
Le but étant de récupérer des informations ouvertes à tous, de les récupérer via une API opendata et d’ensuite les traiter.
Notre objectif est de récupérer des informations sur le nombre de cas, de décès et de guérisons en fonction d’une date et d’un lieu.

Les histogrammes affichent des informations sur le nombre de nouveaux cas, de guérisons et de morts en fonction d'un lieu.
La carte quant à elle permet d'avoir une vision plus globale sur la densité de cas en fonction des régions du monde.

### Ce qu'on peut en tirer :

D'après les résultats observés, on peut voir que l'est et le centre de la France sont les régions avec le plus d'hospitalisations (voir carte ci-dessous) : 
* ![Carte France Hospi](https://github.com/MatthiasJouen/DataViz/tree/main/images/france_hospi.PNG?raw=true)
On observe également que les régions montrant un nombre élevé de guérison à la Covid sont également celles présentant un nombre de décès très important. Les données montrent également que le nombre total de décès est supérieur au nombre total d'hospitalisation montrant bien le manque de lits d'hôpital observé au printemps 2020.
Les Bouches-du-Rhône ont encore Paris ont été très touché par la pandémie, en démontre l'histogramme des décès :
* ![Décès à Paris](https://github.com/MatthiasJouen/DataViz/tree/main/images/paris_deces.PNG?raw=true)



#                                                                           User Guide

Afin de faire fonctionner le projet sur sa machine, vous aurez besoin de plusieurs pré-requis.

#### Installation de python :
Tout d’abord il vous faudra une version de python supérieure à la version 3.
Voici le lien de téléchargement pour installer Python, attention à bien choisir le bon système d'exploitation et si vous êtes sur Windows, veuillez à bien choisir la version 32 ou 64 bits en fonction de votre machine : <https://www.python.org/downloads/>

Pour vérifier que Python est bien installé, vous pouvez taper cette commande dans votre invite de commande : “python”, la réponse dans ce cas sera la version de python que vous possédez.

#### Télécharger notre projet :
Afin de pouvoir accéder à notre projet, il vous faudra le télécharger. Voici le lien du projet sur Git : https://github.com/MatthiasJouen/DataViz.git

#### Avoir un éditeur de code :
Pour accéder au projet en détail, il vous faudra un éditeur de code. Celui que nous conseillons est Visual Studio Code, qui est gratuit et très simple d'utilisation. Voici le lien de téléchargement : <https://code.visualstudio.com/>
Pareil que pour python, attention à bien choisir la version correspondante à votre machine.

Une fois téléchargé, l’ouvrir et cliquer sur **“File”** → **“Open Folder”** → et sélectionnez le dossier de notre projet.

Faites ensuite **“CTRL+SHIFT+P”** puis **“Python : Select Interpreter”**. Sélectionnez ensuite la version de python que vous avez installée. Elle se trouve dans la plupart des cas dans : \AppData\Local\Programs\Python\…\python.exe 

L’avant-dernière étape avant de lancer le programme consiste à installer des bibliothèques ou des extensions du langage Python. Nous en utilisons 3 dans notre projet. Afin de vous faciliter la tâche, nous avons préparé un fichier nommé “requirement.txt” qui regroupe les bibliothèques nécessaires. 
pour les installer, il faut faudra ouvrir un terminal sur votre éditeur de Code : **“Terminal”** → **“New Terminal”** ou **“CTRL+SHIFT+ù”**
Vous serez normalement directement dans le bon dossier, écrivez alors :
 **“pip install -r requirement.txt”**. 
Cette commande installera alors tous les requis. 

#### Lancer le projet :
La dernière étape est la plus simple. Il vous suffit de vous placer dans le fichier **“main.py”** et de cliquer sur la petite flèche verte en haut à droite Visual Studio ou alors de faire **“CTRL+F5”**. Le projet s’est alors lancé sur votre navigateur.
Il vous manque plus qu’à ouvrir votre navigateur et copier cette adresse : <http://127.0.0.1:8050/>



(Attention les commandes précisés pour les configurations de l’éditeur de code ne sont valables que pour Visual Studio Code.)

#                                                                           Developper guide

### Organisation du projet :
Afin de faciliter les modification de code et différentes versions d'avancement du projet, un dépôt github a été mis en place. On a utilisé une branche chacun, une pour récupérer les datas et une autre pour mettre en place les histogrammes et les cartes (dans un premier avec de fausses données puis avec celles récupérées de l'API).
Tous les scripts python nécessaire au bon fonctionnement du projet se trouve dans le dossier src/, les fichiers html générés pour l'affichage des cartes sont sauvegardés sous le dossier html de la racine du projet.
#
