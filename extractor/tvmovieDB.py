import requests
import utils

def get_data(site, count):
    try:
        soup = utils.get_link(site)
        genre = []
        title = ""
        cast_list = {}
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
                character_list.append(item[1])
            cast_list.update({"actor": actor_list,"character":character_list})
        except AttributeError:
            pass
        try:
            genres = soup.find("section",{"class": "genres right_column"}).find_all("ul")
            for item in genres:
                genre.append(item.text.replace("\n",""))
                
        except AttributeError:
            pass
        try:
            rating = soup.find("div", {"class": "percent"}).findChildren()
        except AttributeError:
            pass
        data = {}
        all_text = soup.findAll(text = True)
        page_text = " ".join(filter(utils.visible,all_text))
        data = {}
        data['link'] = site
        data['title'] = title.strip()
        data['resume'] = resume.strip()
        data['rate'] = rating[0].text.strip()
        data['genre'] = genre
        data['cast'] = cast_list
        data['site_data'] = page_text
        path = "extractor/tvmovidDB"
        fileName = count
        utils.writeToJson(fileName,path, data)
    except ConnectionError:
        print(site)
    except requests.exceptions.HTTPError: 
        pass