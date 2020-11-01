# limier
Limier is a little tool in CLI for finding RSS feed on a website event when it's broken or hidden.

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## Install

```
git clone https://github.com/darcosion/limier
cd limier
pip3 install requirements.txt
```

## Usage

```bash
$ ./limier.py -h
Limier by darcosion (https://github.com/darcosion/limier)
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

### Example : 
```bash
$ ./limier.py -d community.mybb.com
Limier by darcosion (https://github.com/darcosion/limier)
[~] - Trying recovery flux type link.
[~] - Trying recovery flux type sitemap
------------------------------------------
--- Gathering results collected ----------
------------------------------------------
[+] - https:/community.mybb.com/syndication.php

```
