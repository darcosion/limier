from robobrowser import RoboBrowser
import re, time, argparse

#import locaux
import research

print("Limier par darcosion (https://github.com/darcosion)")

# paramètres de CLI
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--domain", type=str,
                    help="domain to investigate")
args = parser.parse_args()


# Création d'un browser pour les recherches
browser = RoboBrowser(user_agent='Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0'
                      , history=True
                      , parser='html.parser')

# TODO : faire une vérification du domaine pour être sur...)
# une fonction réutilisable sera donc un plus, dans utils.py
browser.open("http://" + args.domain)

#moulinette, pour le moment locale
listurl = []
listResearch = [research.getFluxLink, research.getFluxBruteForce]

for i in listResearch:
    listurl = list(set(listurl) | set(i(browser)))

for i in listurl:
    print("[+] - " + i )
                   
