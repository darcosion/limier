#!/usr/bin/env python3

import time, re
from urllib import error as urllibError
from googlesearch import search as search_in_google

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
    print("[~] - Recherche de flux par bruteforce ಠ_ಠ")
    listret = []
    base_url = browser.url
    for i in uri_feed:
        browser.open(base_url + i)
        if(not browser.response.ok):
            pass
        else:
            if((browser.find("feed") != None) or
               (browser.find("rss") != None)):

                listret.append(browser.url)
        time.sleep(1.5)
    return listret

#check le sitemap.xml s'il existe
# TODO, traiter tous les cas de redirection vers xsl...
def getSiteMapFlux(browser):
    print("[~] - Tentative de récupération de flux en sitemap")
    base_url = browser.url
    browser.open(base_url + "/sitemap.xml")
    #check si redirection
    if(browser.response.is_redirect):
        if(browser.response.url != browser.url):
            browser.open(browser.response.url)
        elif('Location' in browser.response.headers):
            browser.open(browser.response.headers['Location'])
        else:
            return []
    
    if(not browser.response.ok):
        return []
    if(utils.sitemap_check(str(browser.parsed))):
        return [browser.url]
    #pour quand on devra traiter le xsl
##    browser.open(base_url + "/sitemap.xsl")
##    if(utils.sitemap_check(str(browser.parsed))):
##        return [browser.url]
    
    # c'est pas juste, tout le monde est sensé avoir un sitemap ! >.<
    return []

#recherche depuis google
def getFluxByGoogle(browser):
    print("[~] - Tentative de récupération de flux depuis google")
    listret = []
    base_domain = re.sub("http(s?)://", '', browser.url).split('/')[0] # isole le domaine
    try:
        for i in search_in_google("rss " + "site:" + base_domain,
                                  num=5,
                                  user_agent=browser.session.headers['User-Agent']):
            if(base_domain in i):
                browser.open(i)
                if(utils.rss_check(str(browser.parsed))):
                    listret.append(i)
    except urllibError.HTTPError:
        print("[x] - google active le blocage de requête car trop de requête d'un coup")
        return listret
    return listret
            
        

#identifier le CMS

#def frameworkIdentifier(browser):
    
        
    
# TODO : faire la "taxonomy de feed" de drupal en fonction
