from bs4 import BeautifulSoup as bs
import re
import json as js
import requests as rq

def visible(element):
    
    if element.parent.name in ['style', 'script', 'html', 'head', 'title']: return False
    elif re.match('<!--.*-->', str(element)): return False
    elif re.match('\n', str(element)): return False
    else:
        return True

def text_from_html(soup):
    texts = soup.findAll(text=True)
    visible_texts = filter(visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)

def writeToJson(fileName,path, data):
    filepath = path + '/' + fileName + '.json'
    with open(filepath, 'w') as fp:
        fp.write(js.dumps(data, indent = 2))

def readJson(path):
    with open(path) as fr:
        data = js.load(fr)
    return data


def get_link(link):
    r = rq.get(link)
    r.raise_for_status()
    soup = bs(r.content, "lxml")
    return soup
    

                          