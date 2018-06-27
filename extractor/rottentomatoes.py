import reader as r
import utils as utils

with open('extractor\sites.txt') as f:
    lines = f.readlines()
    f.close()
    
for site in lines:
    try:
        soup = r.get_link(site)
        genre = ""
        title = ""
        cast_list = {}
        rate = ""
        try:
            title = soup.title.text.strip()
            title = title.split("-")[0]
        except AttributeError:
            pass
        try:
            resume = soup.find("div", {"id": "movieSynopsis"}).text.strip()
        except AttributeError:
            pass
        try:
            genre = soup.find("td", text = "Genre:").parent.text.split("\n")[2];
        except AttributeError:
            pass
        try:
            cast = soup.find_all("div",{"class":"cast-item media inlineBlock "})
            actors_list = []
            characters_list = []
            for item in cast:
                actor = item.find("div").find("a").text.strip()
                actors_list.append(actor)
                character = str.replace(item.find("span",{"class": "characters subtle smaller"}).text,"as ","")
                characters_list.append(character)
            cast_list.update({"actor": actors_list,"character":characters_list})
        except AttributeError:
            pass
        try:
            rate = soup.find("span",{"class":"meter-value superPageFontColor"}).span.text.strip()
        except AttributeError:
            pass
        page_text = utils.visible(soup)
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
    except ConnectionError:
        print(site)




