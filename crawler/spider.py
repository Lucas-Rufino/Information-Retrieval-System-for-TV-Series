from bs4 import BeautifulSoup as bs
import requests as rq 
from urllib import robotparser


url = rq.get('https://trakt.tv/shows/trending?page=2')
soup = bs(url.content, 'lxml')
series_links = soup.find("div", {"class":"frame-wrapper"}).find_all("a")
lista = []
a = []
 
all_links = set()
def get_links(domin, link_name): 
    url = rq.get(domin+link_name)
    soup = bs(url.content, 'lxml')
    series_links = soup.find("div", {"class":"frame-wrapper"}).find_all("a")
    for x in series_links: 
        lista.append(x.attrs['href'] if 'href' in x.attrs else None)
    retorno = []
    for x in lista:
        if x is not None and x not in all_links:
            retorno.append(x)
            all_links.add(x)
    return retorno

#filter(lambda x: x not None, lista)

def bfs(domain, links):
    max_sites = 5000
    while(not (links == [])) or max_sites == 0:
        link =  links.pop(0)
        
        print(domain, link[0])
        try: 
            a = get_links(domain, link)
            for x in a: 
                links.append(x)
        except AttributeError:
            max_sites -= 1
            continue
        max_sites -= 1  
        print(max_sites)
    return links


l = []
l = get_links('https://trakt.tv', '/shows')
lista = bfs('https://trakt.tv', l)
print(len(lista))
print(all_links)
