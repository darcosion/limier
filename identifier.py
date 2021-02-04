#!/usr/bin/env python3



# on ne veut identifier que les frameworks pour lesquels les flux rss
#sont vraiment bizarres à capter
# TODO : faire la "taxonomy de feed" de drupal en fonction

class spip:
    def __init__(self, console):
        self.console = console
        self.id_spip = range(0, 3000)

    def spipIden(self, browser):
        base_url = browser.url
        #on vérifie l'existence d'un login spip : *
        if(browser.open(base_url + "/spip.php?page=login") != None):
            return True
        if(browser.open(base_url + "/spip.php") != None):
            return True
        if(browser.open(base_url + "/spip.php?page=backend") != None):
            return True
        #bon ben c'est pas du spip...
        return False

    def spipGetRSS(self, browser):
        base_url = browser.url
        rss = ["/spip.php?page=backend",
               "/spip.php?page=backend-breves",
               "/spip.php?page=backend-sites"
               ]
        for i in self.id_spip:
            if(browser.open(base_url + "/spip.php?page=backend&id_rubrique=" + str(i)) != None):
                rss.append(browser.url)
            if(browser.open(base_url + "/spip.php?page=backend&id_mot=" + str(i)) != None):
                rss.append(browser.url)
            if(browser.open(base_url + "/spip.php?page=backend&id_auteur=" + str(i)) != None):
                rss.append(browser.url)
        return rss
    
    def getRSS(self, browser):
        if(self.spipIden(browser)):
            return self.spipGetRSS(browser)
        else:
            return []


class SocialNetwork():
    def __init__(self, console):
        self.console = console
        return

    def identifyWix(self, browser):
        if(browser.find("meta", attrs={"content":'Wix.com Website Builder'})):
           console.limierLog("Identification Wix")
           return True
        if(browser.find("meta", attrs={"http-equiv":"X-Wix-Meta-Site-Id"})):
           console.limierLog("Identification Wix")
           return True
        if(browser.find("meta", attrs={"http-equiv":"X-Wix-Published-Version"})):
           console.limierLog("Identification Wix")
           return True
        return False

    def identifyPinterest(self, browser):
        if(browser.find("meta", attrs={"property":'og:site_name',
                                       "content":'Pinterest'})):
           console.limierLog("Identification Pinterest")
           return True
        return False

    def identifyReddit(self, browser):
        if("://reddit.com" in browser.url):
            return True
        else:
            return False

    def identifyBlogspot(self, browser):
        if(browser.find("meta", attrs={"content":"blogger",
                                       "name":"generator"})):
            console.limierLog("Identification Blogspot")
            return True
        return False

    def getRSS(self, browser):
        base_url = browser.url
        # identify wix
        if(self.identifyWix(browser)):
            return "/blog-feed.xml"
        #identify pinterest by pinterest.fr/user/feed.rss
        if(self.identifyPinterest(browser)):
            return "/feed.rss"
        #identify reddit by url string
        if(self.identifyReddit(browser)):
            return ".rss"
        #identify blogspot
        if(self.identifyBlogspot(browser)):
            return "/feed/posts/default"
        return False
