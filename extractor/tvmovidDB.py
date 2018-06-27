import reader as r
import utils

with open('extractor\sites.txt') as f:
    lines = f.readlines()
    f.close()

for site in lines:
    try:
        soup = r.get_link(site)
        try:
            title = soup.find("div", {"class":"title"}).text.strip()
        except AttributeError:
            pass
        try:
            resume = soup.find("div", {"class": "overview"}).text
        except AttributeError:
            pass
        try:
            cast = soup.find("ol",{"class": "people scroller"}).find_all("li")
            cast_list = []
            for item in cast:
                cast_list.append(item.text.strip().split("\n"))
        except AttributeError:
            pass
        try:
            genre = soup.find("section",{"class": "genres right_column"}).find("li").text
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
        data['title'] = title.strip()
        data['resume'] = resume.strip()
        data['rate'] = rating[0].text.strip()
        data['genre'] = genre
        data['cast'] = cast_list
        data['site_data'] = page_text
        path = "extractor/tvmovidDB"
        fileName = title
        utils.writeToJson(fileName,path, data)
    except ConnectionError:
        print(site)