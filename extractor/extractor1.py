import utils
import operator
from bs4 import BeautifulSoup as bs
import re


def get_element(node):
  length = len(list(node.previous_siblings)) + 1
  if (length) > 1:
    return '%s:nth-child()' % (node.name)
  else:
    return node.name

def get_css_path(node):
  path = [get_element(node)]
  for parent in node.parents:
    if parent.name == 'body':
      break
    path.insert(0, get_element(parent))
  return ' > '.join(path)

#Ranquear os elementos de acordo com o numero de filhos contidos
def ranking_elements(element):
    if(element.name is not None):
        count = 0
        for child in element.descendants:
            name = get_css_path(child.parent)
            if child.name in ["table", "div","td","ul","span", "section","td"]:
                count+=1
        ranking.append([name,child.parent,count])
        ranking_elements(child)
#Gera um path para cada node da arvore, para possível clusterização, podendo ser usado como 
#metodo de juntar em cluster os paths mais parecidos
def get_tree(element):
    if(element.name is not None):
        for child in element.descendants:
            name = get_css_path(child.parent)
            if (name not in ranking):
                ranking.append([name, child.parent])
        get_tree(child)
    
#Aqui a ideia é limpar o html, tentar remover estruturas que são consideradas noise        
def clean_page(element,removed):
    empty_tags = [tag for tag in soup.body.find_all() if len(tag.contents) == 0]
    blank_lines = [tag for tag in soup.html.find_all() if tag.text == '\n']
    for i in blank_lines:
        i.decompose()
        removed+=1
    for i in empty_tags:
        i.decompose()
        removed+=1
    for i in soup.find_all("script"):
        i.decompose()
        removed+=1
    for i in soup.find_all("style"):
        i.decompose()
        removed+=1
    for i in soup.find_all("noscript"):
        i.decompose()
        removed+=1
    for i in soup.find_all("img"):
        i.decompose()
        removed+=1
    for i in soup.find_all("link"):
        i.decompose()
        removed+=1
    for i in soup.find_all("button"):
        i.decompose()
        removed+=1
    return removed

def clean_text(text):
    lines = [line.strip() for line in text.splitlines()]
    lines = [l for l in lines if l != '']
    return lines

#A ideia aqui é que os resumes possuem o maior texto da pagina, logo eu utilizo essa heuristica para
#tentar pegar os resumes.

def get_sinopses(element, max_size):
    list_ = []
    for tag in element:
        ap = True
        path = get_css_path(tag.parent)
        path_size = len(path)
        noise = ["critics","review","movies","news","inbox","tv"]
        text = str(tag)
        text.lower()
        for i in noise:
            if i in text:
                ap = False
        if ap:
            list_.append([tag,path_size])
    return sorted(list_, key=chave)

def chave(pair):
    return (len(pair[0]), pair[1]*-1)
def get_cast(soup):
    if soup.name is not None:
        tags = soup.find_all(["div","table","span","ol","td"])
        for item in tags:
            children = item.findChildren()
            if len(children) >= 2 and len(children) <= 3:
                cast_temp.append(item)
        cast = rank_element(cast_temp)
    return clean_text(cast.text)

def rank_element(list_to_rank):
    for item in list_to_rank:
        parent = item.parent.parent
        parent_path = get_css_path(parent)
        aux[parent_path] = parent
        if has_key(parent_path,ranked_element):
            ranked_element[parent_path] = 1 + ranked_element[parent_path]
        else:
            ranked_element[parent_path]= 1
    return aux[get_max(ranked_element)]

def has_key(key, hash_element):
    for i in hash_element:
        if i == key:
            return True
    return False

def get_max(mapList):
    maxKey = ""
    maxValue = 0
    for key in mapList:
        if maxValue < mapList[key]:
            maxValue = mapList[key]
            maxKey = key
    return maxKey

with open('extractor\sites.txt') as f:
    lines = f.readlines()
    f.close()
    
for site in lines:
    soup = utils.get_link(site)
    removed = 0
    print(clean_page(soup,0))
    ranked_element = {}
    cast_temp = []
    aux = {}
    cast = get_cast(soup)
    ranking = []
    title = soup.title.text
    resume = get_sinopses(soup.html.find_all(text = True), 0)
    print(title)
    print(clean_text(resume[-1][0]))
    print(cast)

    
    # bodyArray = body.text.strip()
    # print(bodyArray)
    # bodyArray = bodyArray.strip().split("\n")
    # print(bodyArray)


    
