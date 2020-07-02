#!/bin/python3

# Il va falloir sérieusement réfléchir au design
# un identifier et un crawler me semblent foireux...

def wordpressIden(browser):
    base_url = browser.url
    # on vérifie l'existence de directory wordpress
    if(browser.open(base_url + "/wp-admin/") != None):
        return True
    if(browser.open(base_url + "/wp-content/") != None):
        return True
    if(browser.open(base_url + "/wp-includes/") != None):
        return True
    # on cherche sur l'url de base des templates de base de wordpress...
    browser.open(base_url)

    if(browser.select('.wp-blocks') != None):
        return True
    if(browser.select('.wp-dom-ready') != None):
        return True
    if(browser.select('.wp-edit-post') != None):
        return True
    if(browser.select('.wp-smiley') != None):
        return True
    if(browser.select('.wp-block-button') != None):
        return True
    if(browser.select('.wp-block-table') != None):
        return True
    # bon ben c'est pas du wordpress
    return False
    

