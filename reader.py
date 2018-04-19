import requests as rq
from bs4 import BeautifulSoup as bs
import json as js

def get_link(link):
    
    r = rq.get(link)
    soup = bs(r.content)
    return soup