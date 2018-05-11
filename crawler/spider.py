from bs4 import BeautifulSoup as bs
from selenium import webdriver
import requests as rq 
from urllib import robotparser
import urllib.request 

not_that_bad_words = set()
value_links = set()
bad_words = set()
all_links = set()
bad_words = ('movie', 'ads','about','amazon','privacy', 'apps', 'join', 
			'vip','schedule', 'person','theater','signin', 'facebook', 
			'twitter', 'google', 'register', 'calendar', 'news', 'term', 
			'contact', 'professionals', 'create', 'sport', 'documentar',
			'login', 'game', 'feature', 'music', 'news', 'documentary','watchlist')
not_that_bad_words = ('page','trending', 'popular', 'watch','tv', 'netflix', 'top', 'rate', 'listing')
good_words = ('cast', 'tv', 'show', 'episode', 'season', 'serie')

driver = webdriver.PhantomJS('phantomjs/bin/phantomjs')

def get_full_link(domin, link_name):
    if link_name.find('http') > -1:
        return link_name
    return domin+link_name

def get_links(with_phantom, domin, link_name): 
	lista = []
	retorno = []

	try: 
		link = get_full_link(domin, link_name)
		if with_phantom: 
			driver.get(link)
		else: 
			url = rq.get(link)
		soup = bs(url.content, 'lxml')
		series_links = soup.find_all('a')
		   
		for x in series_links: 
			lista.append(x.attrs['href'] if 'href' in x.attrs else None)
		
		for x in lista:
			if x is not None:
				link = get_full_link(x, domin)
				if link not in all_links:
					retorno.append(link)
					all_links.add(link)
	except rq.exceptions.ConnectionError: 
		pass
	return retorno

'''
Estrategia 1 - Retorna: 
1 - Se o site for importante, i.e, o dominio esta dentro do contexto de serie 
0 - Se o site de possibilidade para encontrar o site do dominio
None - se estiver no conjunto de bad words 
'''
def get_inversed_priority_strategy(domain, link): 
	if link.find('http') > -1 and link.find(domain) < 0:
		return None
	for x in bad_words: 
		if(link.find(x) > -1):
			return None
	for x in not_that_bad_words: 
		if(link.find(x) > -1):
			return 0
	return 1 

'''
Estrategia 2 - Retorna: 
1 - Se o site for importante, i.e, no conjunto de good_words  
0 - Se o site de possibilidade para encontrar o site do dominio
None - se estiver no conjunto de bad words 
'''
def get_priority_link(link_name): 
	for x in not_that_bad_words: 
		if(link_name.find(x) > -1): 
			return 0
	for x in good_words: 
		if(link_name.find(x) > -1):
			return 1
	return None


# Pega o link com a estrategia 
 
def get_priority_links(strategy, domin, link_name): 
	lista = []
	retorno = []
	try: 
		url = rq.get(domin+link_name)
		soup = bs(url.content, 'lxml')
		series_links = soup.find_all('a')

		for x in series_links: 
			lista.append(x.attrs['href'] if 'href' in x.attrs else None)
		retorno = []
		for x in lista:
			if x is not None and domin+x not in all_links:
				priority = get_priority_link(x)
				retorno.append(x)
				all_links.add(domin+x)
				if priority == strategy:
					value_links.add(domin+x)  #adiciona apenas os sites importantes 
	except rq.exceptions.ConnectionError: 
		pass
	return retorno

def bfs(domain, links):
	max_sites = 1500
	while(not (links == []) and len(all_links) < max_sites):
		link =  links.pop(0)
		print(domain,link)
		try: 
			a = get_links(False, domain, link)
			for x in a: 
				links.append(x)
		except AttributeError:
			continue
		print(len(all_links))
	return links

def get_name(directory):
	stop_carac = set()
	aux = ''
	stop_carac = ('*', '?', '/','//', ':','"','|', '>','<' )
	directory = directory.split('/')
	name = directory[-1]
	for x in name: 
		if x in stop_carac: 
			aux += '-'
		else: 
			aux += x
	return aux

def download_vised_sites(fold): 
	for x in value_links:
		name = get_name(x)
		print(name)
		try:
			with open(fold +'/' + name + '.html', 'wb') as f: 
				try: 
					f.write(rq.get(x).content)
				except( rq.ConnectionError): 
					continue
		except (IOError, OSError):
			continue

def bfs_priority(domain, links): 
	max_sites = 1000
	while(not (links == []) and (len(value_links) < max_sites)):
		link =  links.pop(0)
		try: 
			a = get_priority_links(1, domain, link)
			for x in a: 
				links.append(x)
		except AttributeError:
			continue
	return links


#ADD OS LINKS desse jeito 
folder_name = [ 'trakt/strategy2', 'MOVIE DB/strategy2', 'SHOWTIME/strategy2', 'IMDb/strategy2']
links_domain = [['https://trakt.tv', '/shows/'], ['https://www.themoviedb.org', '/tv' ],['http://www.sho.com', '/series'], ['https://www.imdb.com', '/chart/toptv/?ref_=nv_tp_tv250_2']]
for x in range(len(folder_name)):
	fold = folder_name[x]
	linka = links_domain[x]
	l = []
	l = get_priority_links(1, linka[0], linka[1])
	lista = bfs_priority(linka[0], l)
	download_vised_sites(fold)