import reader as r
import utils as utils

with open('extractor\sites.txt') as f:
    lines = f.readlines()
    f.close()
    
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
        all_text = soup.findAll(text = True)
        page_text = "".join(filter(utils.visible,all_text) + "")
        print(page_text)
        data = {}
        data['title'] = title
        data['resume'] = resume
        data['rate'] = rate
        data['genre'] = genre
        data['cast'] = cast_list
        data['site_data'] = page_text
        path = 'extractor/rottentomatoes'
        fileName = title
        utils.writeToJson(fileName,path,data)
    except AttributeError:
        continue




