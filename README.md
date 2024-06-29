# Projet Django Multilingue

## Description

Ce projet est une application web simple développée avec Django. L'objectif principal est de créer une application multilingue, intégrant éventuellement des fonctionnalités utilisant des modèles de langage (LLM).

## Fonctionnalités

- Gestion des articles de blog avec les champs `title`, `content`, et `publication_date`.
- Affichage d'une liste d'articles.
- Support de l'internationalisation (i18n) avec au moins deux langues (français et anglais).
- Interface utilisateur permettant de changer la langue de l'interface.

## Prérequis

- Python 3.8 ou supérieur
- pip (Python package installer)
- git
- Un compte sur [Render.com](https://render.com/) pour le déploiement

## Installation

### 1. Cloner le dépôt

Clonez le dépôt GitHub sur votre machine locale :

```bash
git clone https://github.com/your-username/multilang_site.git
cd multilang_site
```
Créez et activez un environnement virtuel pour le projet :
```
python -m venv env
source env/bin/activate  # Sur macOS/Linux
env\Scripts\activate  # Sur Windows
```
Installez les dépendances listées dans requirements.txt :
```
bash
pip install -r requirements.txt
```
Appliquez les migrations pour configurer la base de données SQLite par défaut :

```bash
python manage.py migrate

```
Collectez les fichiers statiques pour les servir correctement :

```bash
python manage.py collectstatic
```
Créez un superutilisateur pour accéder à l'admin Django :

```bash
python manage.py createsuperuser
```
Lancez le serveur de développement pour vérifier que tout fonctionne correctement :

```bash
python manage.py runserver
Accédez à l'application dans votre navigateur à l'adresse http://127.0.0.1:8000/.
```

Accéder à l'admin Django
```
Accédez à l'interface d'administration à l'adresse http://127.0.0.1:8000/admin/ et connectez-vous avec les informations du superutilisateur que vous avez créé.
```
Vous pouvez changer la langue de l'interface utilisateur en utilisant le sélecteur de langue disponible sur le site.

Déploiement
Assurez-vous que toutes les modifications nécessaires sont commitées et poussées vers GitHub :

```bash
git add .
git commit -m "Préparation pour le déploiement"
git push
```
9. Déployer sur Render.com
```
2.1. Créer un nouveau service
Connectez-vous à votre compte Render.com.
Cliquez sur "New" et sélectionnez "Web Service".

Connectez Render à votre dépôt GitHub et sélectionnez le dépôt multilang_site.
Configurez le service avec les paramètres suivants :
Build Command : pip install -r requirements.txt

Start Command : gunicorn multilang_site.wsgi:application --log-file -
Environment : Python 3
Branch : main (ou la branche que vous souhaitez déployer)
Cliquez sur "Create Web Service".

```
Une fois le déploiement terminé, Render.com fournira une URL pour accéder à votre application. Visitez cette URL pour vérifier que tout fonctionne comme prévu.

Auteur : Dylan

Juin 2024.



