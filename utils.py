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
#enlève le protocol donné devant un domaine
def protocol_remove(domain):
    return domain.replace('/', '').replace(':', '').replace('https', '').replace('http', '')

#vérifie si c'est bien un flux rss
def rss_check(data):
    if(re.match("<\?xml[ \n\r\t]*?version=(\"|\')[0-9\.]*(\"|\')[ \n\r\t]*?encoding=(\"|\').*(\"|\')\?>", data)):
        return True
    elif(re.match("<rss[ \n\r\t]*?version=(\"|\')[0-9\.]*(\"|\')[ \n\r\t]*?>", data)):
        return True # regex à améliorer je pense
    elif(re.match("<feed[ \n\r\t]*?xmlns=(\"|\').*(\"|\')[ \n\r\t]*?>", data)):
        return True
    else: #on m'a trompé, on m'a floué ! ><
        return False


#vérifie si c'est bien un sitemap (a voir si un sitemap est utile ?)
def sitemap_check(data):
    if(re.match("<\?xml[ \n\r\t]*?version=(\"|\')[0-9\.]*(\"|\')[ \n\r\t]*?encoding=(\"|\').*(\"|\')[ \n\r\t]*?\?>", data)):
        return True
    elif(re.match("<urlset[ \n\r\t]*?xmlns=(\"|\').*(\"|\')[ \n\r\t]*?>", data)):
        return True
    elif(re.match("<sitemapindex[ \n\r\t]*?xmlns=(\"|\').*(\"|\')[ \n\r\t]*?>", data)):
        return True
    # Quelle est cet étrange objet à la dérive que l'on appelle "terre" ?
    elif(re.match("<xsl\:stylesheet( |\n)*?version=(\"|\')[0-9\.]*(\"|\')[ \n\r\t]*?xmlns\:html=(\"|\').*(\"|\')[ \n\r\t]*?xmlns\:sitemap=(\"|\').*(\"|\')[ \n\r\t]*?xmlns\:xsl=(\"|\').*(\"|\')>", data)):
        return True
    elif(re.match("XML Sitemap Index", data)):
        return True
    else: # bon ben cépala...
        return False
        
