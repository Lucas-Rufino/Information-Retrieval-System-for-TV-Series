import requests
import utils

def get_data(site, count):
    try:
        soup = utils.get_link(site)
        genre = []
        title = ""
        cast_list = {}
        characters_list = {}
        rate = ""
        try:
            title = soup.find("div", {"class":"title"}).text.strip()
            title = title.split("(")[0].strip()
        except AttributeError:
            pass
        try:
            resume = soup.find("div", {"class": "overview"}).text
        except AttributeError:
            pass
        try:
            cast = soup.find("ol",{"class": "people scroller"}).find_all("li")
            cast_l = []
            actor_list = []
            character_list = []
            for item in cast:
                cast_l.append(item.text.strip().split("\n"))
            for item in cast_l:
                actor_list.append(item[0])
                if len(item) == 2:
                    character_list.append(item[1])
            cast_list.update({"actor": actor_list})
            characters_list.update({"characters": character_list})
        except AttributeError:
            pass
        try:
            genres = soup.find("section",{"class": "genres right_column"}).find_all("ul")
            for item in genres:
                gr = item.text.replace("\n", " ").strip().split(" ")
                for i in gr:
                    if len(i) > 2:
                        genre.append(i)
                
        except AttributeError:
            pass
        try:
            rate = soup.find("div", {"class": "percent"}).findChildren().text()
        except AttributeError:
            pass
        data = {}
        all_text = soup.findAll(text = True)
        page_text = " ".join(filter(utils.visible,all_text))
        data = {}
        data['link'] = site
        data['title'] = title.strip()
        data['resume'] = resume.strip()
        data['rate'] = rate
        data['genre'] = genre
        data['cast'] = cast_list
        data['characters'] = characters_list
        data['site_data'] = page_text
        path = "extractor/tvmovidDB"
        fileName = count
        utils.writeToJson(fileName,path, data)
    except ConnectionError:
        print(site)
    except requests.exceptions.HTTPError: 
        pass