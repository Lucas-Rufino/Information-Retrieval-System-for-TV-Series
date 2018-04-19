import reader as r


soup = r.get_link("http://www.tvguide.com/tvshows/the-flash/644014/")
title = soup.find("div", {"class":"tvobject-masthead-wrapper content-wrapper"}).find("h1").text.strip()
resume = soup.find("div", {"class":"tvobject-masthead-wrapper content-wrapper"}).find("div",{"class":"tvobject-masthead-description"}).text.strip()
cast = soup.find("div", {"data-section-id": "cast"}).find("div",{"class": "row"}).find_all("div")
cast_list = []
for item in cast:
    cast_list.append(item.text.strip())
  
   

