# Mini-projet - Autodoc

Ce projet est un petit morceau de code qui automatise la création de lettres de motivation (notamment pour des candidatures spontanés).

## Fonctionnement
Le programme utilise 3 paramètres :
- Le chemin vers le template de lettre de motivation à utiliser
- Le chemin vers le fichier contenant la liste des entreprises à contacter (au format .txt)
- Le dossier de sauvegarde des lettres de motivation générées

Le programme passe ensuite par deux étapes :

### 1) Lecture des paramètres
Le programme lit dans un premier temps le fichier de template de lettre de motivations et la stocke dans une variable. 
Il lit ensuite le fichier de liste d'entreprises et la mémorise dans une liste.


### 2) Préparation du résultat
Le programme crée ensuite un dossier de sauvegarde dans lequel il va stocker les lettres de motivations générées.
Le dossier est crée dans le dossier de sauvegarde spécifié en paramètre.

### 3) Génération des lettres de motivation
Le programme parcourt ensuite la liste des entreprises et génère une lettre de motivation pour chacune d'entre elles.
Pour cela, elle utilise le template de lettre de motivation et remplace les informations suivantes :
- Nom de l'entreprise
- Adresse de l'entreprise

## Contexte de création
Durant ma recherche de stages durant ma seconde année d'études, j'ai été mené à réaliser une grande vague de candidatures spontanées dans un grand nombre d'entreprises.

Comme tout étudiant à cet époque et par manque de temps, j'ai décidé de réaliser une lettre de motivation "par défaut" et de la distribuer à toutes les entreprises que je devais voir.
Il me suffisait ensuite de réaliser à la main les informations que je souhaitais ajouter pour les entreprises dont je souhaitais de meilleurs chances de mon côté.

Cependant, j'ai constaté qu'ajouter le nom de l'entreprise et son adresse à la main était une tâche assez fastidieuse.

J'ai donc créé ce petit script pour m'aider à créer des lettres de motivation personnalisées, en me servant d'un template au format .docx.
