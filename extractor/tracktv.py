
import utils
import requests


def get_data(site,count):
    try:
        soup = utils.get_link(site)
        try:
            title = soup.find("div", {"class": "col-md-10 col-md-offset-2 col-sm-9 col-sm-offset-3 mobile-title"}).text
        except AttributeError:
            pass
        try:
            rating = soup.find("div", {"class":"rating"}).text
        except AttributeError:
            pass
        try:
            genre = str.replace(soup.find("label",text="Genres").parent.text, "Genres","")
        except AttributeError:
            pass
        try:
            resume = soup.find("div",{"itemprop": "description"}).text
            cast_list = []
        except AttributeError:
            pass
        try:
            list_actors = soup.find_all("li",{"itemprop": "actor"})
            for item in list_actors:
                name = item.find("h4",itemprop = "name").text
                character = item.find("h4",{"class":"character"}).text
                cast_list.append([name,character])
        except AttributeError:
            pass   
            data = {}
            all_text = soup.findAll(text = True)
            page_text = " ".join(filter(utils.visible,all_text))
            data = {}
            data['link'] = site
            data['title'] = title.strip()
            data['resume'] = resume.strip()
            data['rate'] = rating.strip()
            data['genre'] = genre
            data['cast'] = cast_list
            data['site_data'] = page_text
            path = "extractor/tracktv"
            fileName = count
            utils.writeToJson(fileName,path, data)
    except ConnectionError:
        pass
    except requests.exceptions.HTTPError: 
        pass