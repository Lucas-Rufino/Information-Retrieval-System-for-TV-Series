from bs4 import BeautifulSoup as bs
import requests as rq 
from urllib import robotparser

class crawler():
    def __init__(self, domain, max_sites):
        self.domain = domain
        self.all_links = set ()
        self.max_sites = max_sites
    
    def get_link(self, link): 
        lista = []
        retorno = []
        url = rq.get(self.domain+link)
        soup = bs(url.content, 'lxml')
        series_links = soup.find("div", {"class":"frame-wrapper"}).find_all("a") #particular para cada site
        for x in series_links: 
            lista.append(x.attrs['href'] if 'href' in x.attrs else None)
        for x in lista:
            if x is not None and x not in self.all_links:
                retorno.append(x)
                self.all_links.add(x)
        return retorno
    
    def bfs(self):
        count = 0 
        links = self.get_link('/shows') #particular para cada site
        while(not (links == [])) or count > self.max_sites:
            link = links.pop(0)
            try: 
                a = self.get_links(self.domain, link)
                for x in a: 
                    links.append(x)
            except AttributeError:
                count += 1
                continue
            count += 1  
        return links

