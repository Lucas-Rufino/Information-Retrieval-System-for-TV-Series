
import re
import xml.dom as xml

with open('extractor\sites.txt') as f:
    lines = f.readlines()

def get_resume(element):
    #the synopsis information is in a div for all sites 
    tag = element.find(attrs = {"itemprop" : "description"})
    if tag != [] and tag is not None:
        return tag
    else:
        tag = element.find(attrs = {"id": "movieSynopsis"})
        if tag != [] and tag is not None:
            return tag
        else:
            tag = element.find(attrs = {"class": "summary-class"})
            if tag != [] and tag is not None:
                return tag
            else:
                tag = element.find(attrs = {"class": "tvobject-masthead-description"})
                if tag != [] and tag is not None:
                    return tag
                else:
                    tag = element.find(attrs = {"class": "overview"})
                    if tag != [] and tag is not None:
                        return tag
                    else:
                        tag = element.find(attrs = {"class":"about-the-series block-container"})
                        if tag != [] and tag is not None:
                            return tag
                        else:
                            return None
def get_cast():
    if(element.name is not None):
        for child in element.child:
            if child.name in ["table","td","div", "li","span"]:
                print(child)                  
       
map_series_info = {}
resume = "None"
def walk(element, title):
    if(element.name is not None):
        for child in element.children:
            if(child.name in ["div","h1","td", "span","label", "li","h4","ol","section","p","main","ul"]):
                tag = get_resume(child)
                resume = tag
                map_series_info[title] = resume
        walk(child,title)

    
for site in lines:
    soup = utils.get_link(site)
    walk(soup.find("body"),soup.title.text)
print(map_series_info)




    
    

    
    
    

