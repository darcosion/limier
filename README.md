(for english people, [I've made a quick README](/README.en.md), but I don't want to do many support in english, so you can improve with pull request if you want)

# limier
Limier is a small utility to crawl a site and discover the rss feeds.

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
$ ./limier.py -d community.mybb.com
Limier by darcosion (https://github.com/darcosion/limier)
[~] - Tentative de récupération de flux type link.
[~] - Attempt to retrieve feed in sitemap
------------------------------------------
---  How to handle the results.  ---
------------------------------------------
[+] - https:/community.mybb.com/syndication.php

```

## TODO : 
 - Add adebug option to visualize what limier is doing. 
 - Explore the site tree. 
 - Recognize which CMS a site is using. 
