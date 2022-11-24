# Projet 4 : Développez un programme logiciel en Python

![logo.png](logo.png)


## Sommaire

+ [Installation du projet](#Installation)
+ [Installation des packages](#Packages)
+ [Le fichier .gitignore](#gitignore)
+ [Lancement des traitements](#Traitement)
+ [Execution de flak8](#Flake8)

## Installation
  
  1- Telecharger et installer la dernière version de Python.
  Pour ma part j'ai installé la version python 3.10.6
		 
2 - Depuis votre terminal sous windows ( cmd )  

Verifiez que vous avez pip installer sur la machine
pour cela lancer la commande 

```pip --help```

- Créer votre dossier projet sous windows
	     
```
mkdir < MyProject04 > 
```
où MyProject04 est le nom de votre projet
Placez vous dans le repertoire projet
```
cd < MyProject04 > 
```
Créer votre environnement virtuel
```
pip -m venv < myenv > 
```
Où myenv est le nom pour votre environnemet virtuel.
Activez votre environnement virtuel.
```
cd < myenv\scripts> 
activate.bat
```
## Packages
 - Installez les packages depuis le fichier requirements.txt
	 
sous windows avec la commande :

```pip install -r requirements.txt```

- Verifier l'installation des packages 
	 
 Sous windows avec la commande : pip freeze
 vous avez la liste ci-dessous affichées

     flake8==4.0.1
     flake8-html==0.4.2
     Jinja2==3.1.2
     MarkupSafe==2.1.1
     mccabe==0.6.1
     nump==0.1
     numpy==1.23.4
     pycodestyle==2.8.0
     pyflakes==2.4.0
     Pygments==2.13.0
     tinydb==4.7.0  	
  
## gitignore

- Exclure l'environnement virtuel des commits sur le serveur distant 
	
Créez le fichier .gitignore à la racine de votre projet:   

```~\MyProject04\.gitignore ```

Editez le fichier .gitignore et ajouter les fichiers et repertoire que vous souhaitez exclure

## Traitement 

- Ajouter dans votre projet, les codes du projet 4 que vous avez recuperer dans Github :
        
Le package comprend des repertoires et les fichiers

- Execution du traitement
Assurez-vous que votre environnement virtuel est activé.
Sous windows, à la racine du projet, lancer le fichier main.py pour exécuter le projet.

```
cd < MyProject04 > 
main.py
```
## Flake8

Le projet contient un rapport flake8 qui n'affiche aucune violation des directives de style de code PEP 8.
Pour executer un autre rapport depuis windows
Toujours à la racine du projet:

```
cd < MyProject04 > 
flake8 --format=html --htmldir=flake8_rapport
```

Le fichier setup.cfg contient d'autres parametres pour le traitement flake8