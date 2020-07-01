#!/bin/python3

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
