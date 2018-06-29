import utils
import requests

def getData_imdb(path):
    soup = utils.get_link(path)
    genre = ""
    title = ""
    cast_list = {}
    rating = ""
    resume = ""

    try:
        title = soup.title.text.strip()
        title = title.split("(")[0].strip()
    except AttributeError:
        pass
    try:
        rating = soup.find("span",{"itemprop": "ratingValue" }).text
        rating = str(float(rating) * 10)
    except AttributeError:
        pass
    try:
        cast_table = soup.find("table", {"class" : "cast_list"}).find_all("span",{"class": "itemprop"})
        actors = []
        for item in cast_table:
            actors.append(item.text)
        characters = []
        character_list = soup.find("table", {"class": "cast_list"}).find_all("td",{"class": "character"})
        for item in character_list:
                characters.append(item.a.text)
        cast_list.update({"actor": actors,"character":characters})
    except AttributeError:
        pass

    try:    
        resume = soup.find("span", {"itemprop": "description"}).text
    except AttributeError:
        pass
    try:
        genres = soup.find("div", {"itemprop": "genre"}).find_all("a")
        genre = []
        for item in genres:
            genre.append(item.text.strip());
    except AttributeError:
        pass
    
    all_text = soup.findAll(text = True)
    page_text = " ".join(filter(utils.visible,all_text))
    data = {}
    data['title'] = title.strip()
    data['resume'] = resume.strip()
    data['rate'] = rating.strip()
    data['genre'] = genre
    data['cast'] = cast_list
    data['site_data'] = page_text
    path = "extractor/imdb"
    fileName = title
    utils.writeToJson(fileName,path, data)
    
 