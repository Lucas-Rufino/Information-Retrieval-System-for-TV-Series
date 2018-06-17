import reader as r
import json as js

with open('extractor\sites.txt') as f:
    lines = f.readlines()
    f.close()
    
def writeToJson(fileName,path, data):
    filepath = path + '/' + fileName + '.json'
    with open(filepath, 'w') as fp:
        js.dump(data, fp)

for site in lines:
    try:
        soup = r.get_link(site)
        title = soup.find("h1", {"class":"title"}).text.strip()
        resume = soup.find("div", {"id": "movieSynopsis"}).text.strip()
        genre = soup.find("td", text = "Genre:").parent.text.strip();
        cast = soup.find_all("div",{"class":"cast-item media inlineBlock "})
        cast_list = []
        for item in cast:
            actor = item.find("div").find("a").text.strip()
            characther = str.replace(item.find("span",{"class": "characters subtle smaller"}).text,"as ","")
            cast_list.append([actor,characther])
        rate = soup.find("div",{"class":"critic-score meter"}).span.text.strip()
        data = {}
        data['title'] = title
        data['resume'] = resume
        data['rate'] = rate
        data['genre'] = genre
        data['cast'] = cast_list
        path = 'extractor/rottentomatoes'
        fileName = title
        writeToJson(fileName,path,data)
    except AttributeError:
        continue




