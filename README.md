(for english people, [I've made a quick README](/README.en.md), but I don't want to do many support in english, so you can improve with pull request if you want)

# limier
Limier est un petit outil en CLI permettant de trouver un flux RSS quand il est planqué sur un site.

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## installation

```
git clone  https://github.com/darcosion/limier
cd limier 
pip3 install requirements.txt
```

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
$ python3 limier.py -d armadito.com -b -f
Limier par darcosion (https://github.com/darcosion/limier)
Researching RSS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
╭────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                        │
│ --- Traitement des résultats collectés ---                                             │
│                                                                                        │
│                                                                                        │
╰────────────────────────────────────────────────────────────────────────────────────────╯
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                              Liste des fluxs RSS ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│        https:/www.armadito.com/sitemap.xml/feed/ │
├──────────────────────────────────────────────────┤
│ https:/www.armadito.com/sitemap.xml/latest/feed/ │
└──────────────────────────────────────────────────┘

```

## TODO : 
 - Identification des forums
 - Exploration d'arborescence de site
 - Vérification de cohérence des feed rss
