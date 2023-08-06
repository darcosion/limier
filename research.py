#!/usr/bin/env python3

import time, re
from urllib import error as urllibError

#import local
import utils, identifier

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
            #wordpress noncontinue
            '/?feed=rss',
            '/?feed=rss2',
            '/?feed=rdf',
            '/?feed=atom',
            # drupal
            '/rss.xml',
            #joomla
            '/index.php?format=feed&type=rss',
            #django, due to doc :
            '/latest/feed/',
            '/sitenews',
            #automn CMS :
            '/rss.php',
            '/rss/rss.php',
            # forum BB
            '/extern.php?action=feed&type=atom',
            '/rss/news/rss.xml',
            '/syndication.php',
            '/posts.rss',
            '/latest.rss',
            '/index.php?action=.xml;type=rss',
            '/external?type=rss2',
            # ouest france blog
            '/index.rss',
            # WIX blog
            '/blog-feed.xml'
            ]

# récupère les fluxs présents en link simple
def getFluxLink(browser, domain, limierLog):
    limierLog("Tentative de récupération de flux type link.")
    listret = []
    fluxlist = browser.find_all('link', attrs={'type':"application/rss+xml"})
    fluxlist += browser.find_all('link', attrs={'type':"application/atom+xml"})
    fluxlist += browser.find_all('link', attrs={'type':"application/rdf+xml"})
    for i in fluxlist:
        if(i.has_attr('href')):
           listret.append(i.attrs['href'])
    return listret

def getPossibleFluxLink(browser, domain, limierLog, depth=0):
    # on s'assure de ne pas faire de boucle infinie :
    if(depth > 3):
        return
    limierLog("Tentative de récupération de flux type href.")
    base_url = domain
    listret = []
    listlink = browser.find_all('a')
    for i in listlink:
        try:
            if(("feed" in i.attrs['href']) or
               ("rss" in i.attrs['href']) or
               ("RSS" in i.attrs['href']) or
               ("atom" in i.attrs['href']) or
               ("syndication" in i.attrs['href'])):
                # on passe les cas déjà traités
                if(i.attrs['href'] in listret):
                    continue
                browser.follow_link(i)
                # on brise la boucle si le lien est identique :
                if(browser.url == base_url):
                    browser.back()
                    continue
                # on vérifie si c'est bien un flux rss
                if(utils.rss_check(browser.response.content)):
                    listret.append(i.attrs['href'])
                # on vérifie qu'il n'y a pas de liste de flux sinon
                elif(base_url in domain and base_url != domain):
                    listret += getPossibleFluxLink(browser, domain, limierLog, depth=depth+1)
                    browser.back()
                else:
                    # l'url n'est pas un flux rss ou ne mène pas vers un flux a priori
                    browser.back()
        except KeyError as e:
            pass
        except Exception as e:
            raise e
    browser.open(base_url)
    return listret

#bruteforce feed
def getFluxBruteForce(browser, domain, limierLog):
    limierLog("Recherche de flux par bruteforce ಠ_ಠ")
    listret = []
    base_url = domain
    for i in uri_feed:
        limierLog("recherche : {}{}".format(base_url, i))
        try:
            browser.open(base_url + i, verify=False)
            if(not browser.response.ok):
                pass
            else:
                if((browser.find("feed") != None) or
                (browser.find("rss") != None)):

                    listret.append(browser.url)
        except Exception as e:
            limierLog(e)
        time.sleep(1.5)
    return listret

#check le sitemap.xml s'il existe
# TODO, traiter tous les cas de redirection vers xsl...
def getSiteMapFlux(browser, domain, limierLog):
    limierLog("Tentative de récupération de flux en sitemap")
    base_url = domain
    browser.open(base_url + "/sitemap.xml", verify=False)
    #check si redirection
    if(browser.response.is_redirect):
        if(browser.response.url != browser.url):
            browser.open(browser.response.url)
        elif('Location' in browser.response.headers):
            if(utils.url_check(browser.response.headers['Location'])):
                browser.open(browser.response.headers['Location'], verify=False)
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



#identifier le CMS
def frameworkIdentifier(browser, limierLog):
    limierLog("Identification framework")
    socnet = identifier.SocialNetwork(limierLog)
    snrss = socnet.getRSS(browser)
    if(snrss != False):
        return [snrss]
    del socnet, snrss
    spipnet = identifier.spip(limierLog)
    spiprss = spipnet.getRSS(browser)
    if(spiprss != []):
        return spiprss
    del spipnet, spiprss
    return []
