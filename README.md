# MSPR Big Data

Ce projet a été réalisé par Eliot RACINE, Yann ROPARS, Valentin SALMON et Hugo TOMASI. Le but de ce dernier est de produire un modèle de machine learning appliqué aux parking afin de prevoir des taux de remplissage en fonctin de facteurs.

Ce projet a été conçu dans une approche Cloud Native et est à la fois créer pour fonctionner depuis une infrastructure Docker ou Kubernetes (on premises ou cloud) ou encore des service FaaS dans le cas d'une approche Serverless.

## Prérequis

Une base de données MySQL ayant un schéma adéquat est requise.

## Utilisation

### Build

Afin de construire cette image, il vous faut cloner ce repository puis exécuter (remplacer `docker` par `podman` si nécessaire):

```bash
docker build -t big_data:latest .
```

### Configuration

| Variable      | Description       |
|---------------|-------------------|
| `DB_URL`       | L'URL de la base MySQL (FQDN or IP)            |
| `DB_NAME`       | Le nom de la base MySQL           |
| `DB_USER`       | Le nom d'utilisateur MySQL            |
| `DB_PASSWORD`       | Le mot de passe MySQL            |
| `DB_PORT`       | Le port utilisé par MySQL           |

### Run

Afin de lancer le conteneur, vous pouvez exécuter la commande suivante (chaque variable d'environnement doit être précédé de l'option `-e`):

```bash
docker run -d --name big_data -e DB_URL=database.exemple.com big_data:latest
```
