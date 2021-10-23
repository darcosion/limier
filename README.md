(for english people, [I've made a quick README](/README.en.md), but I don't want to do many support in english, so you can improve with pull request if you want)

# limier
Limier est un petit outil en CLI permettant de trouver un flux RSS quand il est planqué sur un site.

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## fonctionnalités

 - obtention de flux rss visuellement caché mais dont le lien existe
 - bruteforce de chemins possible de flux rss
 - détection de framework et énumération de flux possible par framework (drupal, spip, RS, etc...)
 - recherche de flux rss via sitemap

## installation

```
git clone  https://github.com/darcosion/limier
cd limier 
pip3 install -r requirements.txt
```

## Usage

![example help image](limierhelp.png)

### Exemple : 

![Example image](limier.png)

## TODO : 
 - Identification des forums
 - Vérification de cohérence des feed rss
