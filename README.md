# limier
Limier est un petit outil en CLI permettant de trouver un flux RSS quand il est planqué sur un site.

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## Usage

```bash
$ ./limier.py -h
Limier par darcosion (https://github.com/darcosion/limier)
usage: limier.py [-h] [-d DOMAIN] [-a USER_AGENT]

optional arguments:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        domain to investigate
  -a USER_AGENT, --user-agent USER_AGENT
                        User-agent to use
```

### Exemple : 
```bash
$ ./limier.py -d rsscircus.com
Limier par darcosion (https://github.com/darcosion/limier)
[~] - Tentative de récupération de flux type link.
[~] - Tentative de récupération de flux en sitemap
[~] - Tentative de récupération de flux depuis google
------------------------------------------
--- Traitement des résultats collectés ---
------------------------------------------
[+] - https:/rsscircus.com/comments/feed/
[+] - https:/rsscircus.com/feed/
```

## TODO : 
 - Traiter le http, https, les redirection 302 et 402, etc...
 - Ajouter une option de debug pour visualiser ce que fait limier
 - Exploration d'arborescence de site
 - Identification des CMS
 - Ajouter la recherche de rss avec googlesearch, au cas où...
