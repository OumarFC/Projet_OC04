# Projet 4 : Développez un programme logiciel en Python

![logo.png](logo.png)

**Installation en ligne de commande pour l'execution du projet**
  
1- Telecharger et installer la dernière version de Python.
Pour ma part j'ai installé la version python 3.10.6
		 
2 - Depuis votre terminal sous windows ( cmd )  

verifier que vous avez pip installer sur la machine
pour cela lancer la commande 

```pip --help```

3- Créer votre dossier projet sous windows
	     
```mkdir < MyProject04 > ``` où MyProject04 est le nom de votre projet

```cd < monProjet4 > ```	

4- Créer votre environnement virtuel
	  
```pip -m venv < myenv > ``` où myenv est le nom pour votre environnemet virtuel
		
5- Activer votre environnement virtuel
	    
Sous windows avec la commande :  

```~\MyProject04\Scripts\activate.bat```
		
6 - Installer les packages depuis le fichier requirements.txt
	 
sous windows avec la commande :

```pip install -r requirements.txt```

7 - Verifier l'installation des packages 
	 
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
     
8 - Exclure l'environnement virtuel des commits sur le serveur distant 
	
Ajouter le fichier .gitignore à la racine de votre projet:   

```~\MyProject04\.gitignore ```

Editer le fichier gitignore et ajouter les fichiers et repertoire que vous souhaitez exclure

9 - Ajouter dans votre projet, les codes du projet 4 que vous avez recuperer dans Github :
        
Le package comprend des repertoires et les fichiers

11 - Lancement 
	
Sous windows, lancer le fichier main.py pour executer le projet
Ouvrer le cmd et taper : 

```python main.py```

12 - Execution du Flake8

Le projet contient un rapport flake8 qui n'affiche aucune violation des directives de style de code PEP 8.
Pour executer un autre rapport :
Depuis windows, activer l'envrionnement virtuel et taper dans le terminal

```flake8 "~\MyProject04" --format=html --htmldir="~\MyProject04\\flake8_rapport"```