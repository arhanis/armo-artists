#This program scrapes the Wikipedia page listing Armenian Artists for a list of their full names.

import urllib3
import certifi
from bs4 import BeautifulSoup

http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
wiki="https://en.wikipedia.org/wiki/List_of_Armenian_artists"

try:
     page = http.urlopen('GET', wiki, preload_content=False)
except urllib3.exceptions.SSLError as e:
     print (e)

def get_names(opened_page):
     soup = BeautifulSoup(opened_page,'html.parser')
     links = soup.findAll('a')
     links = [tag for tag in links if tag.string != None]
     link_text = [a.string for a in links]
     artists = [name for name in link_text if ',' in name]
     return artists

armo_artists = get_names(page)
print(armo_artists)

