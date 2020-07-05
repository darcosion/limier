#!/usr/bin/env python3

# un fix super chelou Oo
# https://stackoverflow.com/questions/46457179/python3-cannot-import-name-cached-property
import werkzeug 
werkzeug.cached_property = werkzeug.utils.cached_property

from robobrowser import RoboBrowser
import re, time, argparse

#import locaux
import research, utils

print("Limier par darcosion (https://github.com/darcosion/limier)")

# paramètres de CLI
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--domain", type=str,
                    help="domain to investigate")
parser.add_argument('-a', "--user-agent", type=str,
                    help="User-agent to use")
parser.add_argument('-b', "--bruteforce",
                    help="Enable bruteforce for website",
                    action="store_true")
parser.add_argument('-s', "--search-engine",
                    help="Enable search engine research",
                    action="store_true")

args = parser.parse_args()

if(args.user_agent):
    user_agent = args.user_agent
else:
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'

# Création d'un browser pour les recherches
browser = RoboBrowser(user_agent=user_agent
                      , history=True
                      , parser='html.parser'
                      , allow_redirects=False)

# TODO : faire une vérification du domaine pour être sur...)
# une fonction réutilisable sera donc un plus, dans utils.py
assert utils.tld_check(args.domain), "le paramètre nom de domaine est incorrecte"
browser.open("https://" + args.domain)

#moulinette, pour le moment locale
listurl = []
listResearch = [research.getFluxLink
                , research.getSiteMapFlux]

if(args.bruteforce):
    listResearch.append(research.getFluxBruteForce)

if(args.search_engine):
    listResearch.append(research.getFluxByGoogle)

for i in listResearch:
    listurl = list(set(listurl) | set(i(browser)))

#gestion des résultats
print('------------------------------------------')
print("--- Traitement des résultats collectés ---")
print('------------------------------------------')

#retire tout un bordel...
for n, i in enumerate(listurl):
    listurl[n] = re.sub("http(s?)://", '', i)
    listurl[n] = i.replace('//', '/')

listurl = list(set(listurl))

for i in listurl:
    print("[+] - " + i )
                   
