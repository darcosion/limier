import time

#list URI feeds
uri_feed = [
            #default
            '/feed',
            '/feed/',
            '/feed.xml',
            '/feed.rss',
            '/feed/rss',
            '/feed/atom',
            '/feed/rss.xml',
            '/feed/atom.xml',
            '/atom.xml',
            '/atom.rss',
            # drupal
            '/rss.xml',
            # SPIP
            '/spip.php?page=backend',
            '/spip.php?page=backend-breve',
            '/spip.php?page=backend-sites',
            #django, due to doc :
            '/latest/feed/',
            '/sitenews',
            
            ]

# récupère les fluxs présents en link simple
# TODO : investiguer le format RDF pour RSS ? 
def getFluxLink(browser):
    listret = []
    fluxlist = browser.find_all('link', attrs={'type':"application/rss+xml"})
    for i in fluxlist:
        if(i.has_attr('href')):
           listret.append(i.attrs['href'])
    return listret

#bruteforce feed
def getFluxBruteForce(browser):
    listret = []
    base_url = browser.url
    for i in uri_feed:
        browser.open(base_url + i)
        if(browser.find("feed") != None):
            listret.append(browser.url)
        time.sleep(1.5)
    return listret
        
    
# TODO : faire la "taxonomy de feed" de drupal en fonction
