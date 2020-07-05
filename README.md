# limier
Limier est un petit outil en CLI permettant de trouver un flux RSS quand il est planqué sur un site.

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## Usage

```bash
$ ./limier.py -h
Limier par darcosion (https://github.com/darcosion/limier)
usage: limier.py [-h] [-d DOMAIN] [-a USER_AGENT] [-b] [-s]

optional arguments:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        domain to investigate
  -a USER_AGENT, --user-agent USER_AGENT
                        User-agent to use
  -b, --bruteforce      Enable bruteforce for website
  -s, --search-engine   Enable search engine research

```

### Exemple : 
```bash
$ ./limier.py -d community.mybb.com
Limier par darcosion (https://github.com/darcosion/limier)
[~] - Tentative de récupération de flux type link.
[~] - Tentative de récupération de flux en sitemap
------------------------------------------
--- Traitement des résultats collectés ---
------------------------------------------
[+] - https:/community.mybb.com/syndication.php

```

## TODO : 
 - Ajouter une option de debug pour visualiser ce que fait limier
 - Exploration d'arborescence de site
 - Identification des CMS
