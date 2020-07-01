# limier
Limier est un petit outil en CLI permettant de trouver un flux RSS quand il est planqué sur un site.

## Usage

```bash
$ ./limier.py -h
Limier par darcosion (https://github.com/darcosion/limier)
usage: limier.py [-h] [-d DOMAIN]
optional arguments:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        domain to investigate
```

### Exemple : 
```bash
$ ./limier.py -d rsscircus.com
Limier par darcosion (https://github.com/darcosion)
[+] - https://rsscircus.com/feed/
[+] - https://rsscircus.com/feed/atom/
[+] - https://rsscircus.com/comments/feed/
```

## TODO : 
 - Ajouter une option de debug pour visualiser ce que fait limier
 - Exploration d'arborescence de site
 - Identification des CMS
