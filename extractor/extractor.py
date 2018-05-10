import reader as r
import re
import operator



cast_temp = {}
def get_cast(element):
    if(element.name is not None):
        for child in element.children:
            if child.name in ["table", "div","td","ul","span", "section"]:
                pos = soup.find_all(["table","div","td"])
                for item in pos:
                    if (hasKey(cast_temp, str(item.parent))):
                        cast_temp[str(item.parent)] = 1 + cast_temp[(str(item.parent))]
                    else:
                        cast_temp[str(item.parent)] = 1
        sorted_x = sorted(cast_temp.items(), key=operator.itemgetter(1))
        return sorted_x

def hasKey(hashMap, key):
    for x in  hashMap:
        if x == key:
            return True
    return False

with open('extractor\sites.txt') as f:
    lines = f.readlines()
    f.close()
for site in lines:
    soup = r.get_link(site)
    a = get_cast(soup.find("body"))
    print(a[-1])