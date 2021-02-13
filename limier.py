#!/usr/bin/env python3

# un fix super chelou Oo
# https://stackoverflow.com/questions/46457179/python3-cannot-import-name-cached-property
import werkzeug 
werkzeug.cached_property = werkzeug.utils.cached_property

from robobrowser import RoboBrowser
from urllib.error import HTTPError
from rich.console import Console as richConsole

# imports custom rich
from rich.progress import track as richTrack
from rich.panel import Panel as richPanel
from rich.table import Table as richTable

import re, time, argparse

#import locaux
import research, utils

#on vérifie qu'on est bien lancé en "main" :
if __name__ == "__main__": 
    #on lance rich 
    console = richConsole()
    
    console.print("Limier par darcosion (https://github.com/darcosion/limier)")
    
    # paramètres de CLI
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--domain", type=str,
                        help="domain to investigate")
    parser.add_argument('-a', "--user-agent", type=str,
                        help="User-agent to use")
    parser.add_argument('-b', "--bruteforce",
                        help="Enable bruteforce for website",
                        action="store_true")
    parser.add_argument('-f', "--frameworks",
                        help="Enable framework identification",
                        action="store_true")
    parser.add_argument('-v', "--verbose",
                        help="Indicate each actions",
                        action="store_true", default=False)
    args = parser.parse_args()
    
    
    if(args.user_agent):
        user_agent = args.user_agent
    else:
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0'
    
    #créaction d'un décorateur rich pour s'assurer que la verbosité est respecté
    def limierLog(*param):
        if(args.verbose):
            return console.log(*param)
        else:
            return

    # Création d'un browser pour les recherches
    browser = RoboBrowser(user_agent=user_agent
                          , history=True
                          , parser='html.parser'
                          , allow_redirects=False)

    # TODO : faire une vérification du domaine pour être sur...)
    args.domain = utils.protocol_remove(args.domain)
    assert utils.tld_check(args.domain), "le paramètre nom de domaine est incorrecte"

    try:
        browser.open("https://" + args.domain)
    except Exception as e:
        #on essaie en http au cas où
        browser.open("http://" + args.domain)

    # vérifie s'il y a une direction.
    if(browser.response.is_redirect):
        if(browser.response.url != browser.url):
            limierLog("Redirection vers " + browser.response.url)
            browser.open(browser.response.url)
        else:
            limierLog("Pas de redirection")
        

    #moulinette, pour le moment locale
    listurl = []
    listResearch = [research.getFluxLink
                    , research.getSiteMapFlux]



    if(args.bruteforce):
        listResearch.append(research.getFluxBruteForce)

    if(args.frameworks):
        listResearch.append(research.frameworkIdentifier)

    for i in richTrack(listResearch, description = 'Researching RSS') if not args.verbose else listResearch:
        listurl = list(set(listurl) | set(i(browser, limierLog)))

    #gestion des résultats
    console.print(richPanel("\n--- Traitement des résultats collectés ---\n\n"))

    #retire tout un bordel...
    for n, i in enumerate(listurl):
        listurl[n] = re.sub("http(s?):(\/?)\/", '', listurl[n])
        #print(args.domain)
        #print(utils.tld_check(listurl[n]))
        #print(listurl[n])
        if(not utils.tld_check(listurl[n])):
            listurl[n] = args.domain + '/' + listurl[n]
        listurl[n] = listurl[n].replace('//', '/')

    listurl = list(set(listurl))
    
    if(len(listurl) > 0):
        #on crée une table pour affichage rich
        table = richTable(show_lines=True)
        
        table.add_column("Liste des fluxs RSS", justify="right", no_wrap=True)
        
        for i in listurl:
            table.add_row(i)
        
        console.print(table)
    else:
        console.print("aucun flux trouvé :disappointed:")
    
