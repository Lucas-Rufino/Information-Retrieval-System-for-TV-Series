import re
import json as js

def visible(soup):
    [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
    text_page = soup.getText().strip()
    return text_page
    # if element.parent.name in ['style', 'script', 'html', 'head', 'title']: return False
    # elif re.match('<!--.*-->', str(element)): return False
    # elif re.match('\n', str(element)): return False
    # else:
    #     return True

def writeToJson(fileName,path, data):
    filepath = path + '/' + fileName + '.json'
    with open(filepath, 'w') as fp:
        fp.write(js.dumps(data, indent = 2))

                          