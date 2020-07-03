#!/usr/bin/env python3

import time

#import local
import utils

#list URI feeds
uri_feed = [
            #default
            '/feed',
            '/feed.xml',
            '/feed.rss',
            '/feed/rss.xml',
            '/feed/atom.xml',
            '/atom.xml',
            '/atom.rss',
            #wordpress
            '/feed/',
            '/feed/rss/',
            '/feed/rss2/',
            '/feed/rdf/',
            '/feed/atom/'
            # drupal
            '/rss.xml',
            # SPIP
            '/spip.php?page=backend',
            '/spip.php?page=backend-breve',
            '/spip.php?page=backend-sites',
            #django, due to doc :
            '/latest/feed/',
            '/sitenews',
            #automn CMS :
            '/rss.php',
            '/rss/rss.php',
            # forum BB
            '/extern.php?action=feed&type=atom',
            'rss/news/rss.xml',
            '/syndication.php',
            '/posts.rss',
            '/latest.rss',
            '/index.php?action=.xml;type=rss',
            '/external?type=rss2'
            ]

identifiers = [
    ""

    ]

# récupère les fluxs présents en link simple
# TODO : investiguer le format RDF pour RSS ? 
def getFluxLink(browser):
    print("[~] - Tentative de récupération de flux type link.")
    listret = []
    fluxlist = browser.find_all('link', attrs={'type':"application/rss+xml"})
    for i in fluxlist:
        if(i.has_attr('href')):
           listret.append(i.attrs['href'])
    return listret

#bruteforce feed
def getFluxBruteForce(browser):
    print("[~] - Recherche de flux par bruteforce")
    listret = []
    base_url = browser.url
    for i in uri_feed:
        browser.open(base_url + i)
        if((browser.find("feed") != None) or
           (browser.find("rss") != None)):
            listret.append(browser.url)
        time.sleep(1.5)
    return listret

#check le sitemap.xml s'il existe
def getSiteMapFlux(browser):
    print("[~] - Tentative de récupération de flux en sitemap.xml")
    base_url = browser.url
    browser.open(base_url + "/sitemap.xml")
    if(utils.sitemap_check(str(browser.parsed))):
        return [browser.url]
    else:
        return []

#identifier le CMS

#def frameworkIdentifier(browser):
    
        
    
# TODO : faire la "taxonomy de feed" de drupal en fonction
