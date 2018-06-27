import reader as r
import utils

with open('extractor\sites.txt') as f:
    lines = f.readlines()
    f.close()
for site in lines:
    try:
        soup = r.get_link(site)
    
        try:
            title = soup.find("h1",{"itemprop": "name"}).text
        except AttributeError:
            pass
        try:
            rating = soup.find("span",{"itemprop": "ratingValue" }).text
        except AttributeError:
            pass
        try:
            cast_table = soup.find("table", {"class" : "cast_list"}).find_all("span",{"class": "itemprop"})
        except AttributeError:
            pass
        actors = []
        for item in cast_table:
            actors.append(item.text)
            
        characters = []
        try:
            character_list = soup.find("table", {"class": "cast_list"}).find_all("td",{"class": "character"})
        except AttributeError:
            pass
        for item in character_list:
            characters.append(item.find("div").a.text)
            
        cast = zip(actors,characters)
        try:    
            resume = soup.find("div", {"itemprop": "description"}).text
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
        data['cast'] = cast
        data['site_data'] = page_text
        path = "extractor/imdb"
        fileName = title
        utils.writeToJson(fileName,path, data)
    except ConnectionError:
        print(site)
 