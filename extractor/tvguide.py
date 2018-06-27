import reader as r
import utils

with open('extractor\sites.txt') as f:
    lines = f.readlines()
    f.close()
for site in lines:
    try:
        soup = r.get_link(site)
        try:
            title = soup.title.text.strip()
        except AttributeError:
            pass
        try:
            resume = soup.find("div", {"class":"tvobject-masthead-wrapper content-wrapper"}).find("div",{"class":"tvobject-masthead-description"}).text.strip()
        except AttributeError:
            pass
        try:
            rating = soup.find("li", {"class": "tvobject-overview-about-line"}).text
        except AttributeError:
            pass
        try:
            cast = soup.find("div", {"data-section-id": "cast"}).find("div",{"class": "row"}).find_all("div")
            cast_list = []
            for item in cast:
                cast_list.append(item.text.strip())
        except AttributeError:
            pass 
            all_text = soup.findAll(text = True)
            page_text = " ".join(filter(utils.visible,all_text))
            data = {}
            data['title'] = title.strip()
            data['resume'] = resume.strip()
            data['rate'] = rating.strip()
            data['cast'] = cast_list
            data['site_data'] = page_text
            path = "extractor/tvguide"
            fileName = title
            utils.writeToJson(fileName,path, data)
    except ConnectionError:
        print(site)

        

