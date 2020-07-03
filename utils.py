#!/usr/bin/env python3

import re

# vérifie si il y a bien un nom de domaine
def tld_check(domain):
    check = re.findall("^([aA-zZ\-]*\.)*[aA-zZ]*", domain)
    if(check != None):
        if(len(check) == 1):
            return True
        else:
            return False
    else:
        return False

#vérifie si c'est bien un flux rss
def rss_check(data):
    if(re.match("<\?xml version=\"[0-9\.]*\" encoding=\".*\"\?>", data)):
        return True
    elif(re.match("<rss version=\"[0-9\.]*\" *?>", data)):
        return True # regex à améliorer je pense
    elif(re.match("<feed *?xmlns=\".*\" *?>", data)):
        return True
    else: #on m'a trompé, on m'a floué ! ><
        return False


#vérifie si c'est bien un sitemap (a voir si un sitemap est utile ?)
def sitemap_check(data):
    if(re.match("<\?xml version=\"[0-9\.]*\" encoding=\".*\"\?>", data)):
        return True
    elif(re.match("<urlset xmlns=\".*\">", data)):
        return True
    elif(re.match("<sitemapindex xmlns=\".*\">", data)):
        return True
    else: # bon ben cépala...
        return False
        
