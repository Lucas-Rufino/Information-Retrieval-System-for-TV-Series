import re
import json as js

def visible(element):
    if element.parent.name in ['style', 'script', 'document', 'head', 'title']: return False
    elif re.match('<!--.*-->', str(element)): return False
    elif re.match('\n', str(element)): return False
    else:
        return True

def writeToJson(fileName,path, data):
    filepath = path + '/' + fileName + '.json'
    with open(filepath, 'w') as fp:
        js.dump(data, fp)

                          