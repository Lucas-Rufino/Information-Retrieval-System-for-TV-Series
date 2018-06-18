import reader as r
import utils

with open('extractor\sites.txt') as f:
    lines = f.readlines()
    f.close()

for site in lines:
    try:
        soup = r.get_link(site)
        title = soup.find("div", {"class": "col-md-10 col-md-offset-2 col-sm-9 col-sm-offset-3 mobile-title"}).text
        country = soup.find("li", {"itemprop": "countryOfOrigin"}).text
        language = soup.find("label",text = "Language").parent.text
        language = str.replace(language, "Language","")
        rating = soup.find("div", {"class":"rating"}).text
        genre = str.replace(soup.find("label",text="Genres").parent.text, "Genres","")
        resume = soup.find("div",{"itemprop": "description"}).text
        cast_list = []
        list_actors = soup.find_all("li",{"itemprop": "actor"})
        for item in list_actors:
            name = item.find("h4",itemprop = "name").text
            character = item.find("h4",{"class":"character"}).text
            cast_list.append([name,character])
        numberOfSeasons = soup.find("span",{"class": "season-count"}).text
        data = {}
        all_text = soup.findAll(text = True)
        page_text = " ".join(filter(utils.visible,all_text))
        data = {}
        data['title'] = title.strip()
        data['resume'] = resume.strip()
        data['rate'] = rating.strip()
        data['genre'] = genre
        data['cast'] = cast_list
        data['site_data'] = page_text
        path = "extractor/tracktv"
        fileName = title
        utils.writeToJson(fileName,path, data)
    except AttributeError:
        continue