import reader as r


soup = r.get_link("https://trakt.tv/shows/the-big-bang-theory")
title = soup.find("div", {"class": "col-md-10 col-md-offset-2 col-sm-9 col-sm-offset-3 mobile-title"}).text
country = soup.find("li", {"itemprop": "countryOfOrigin"}).text
language = soup.find("label",text = "Language").parent.text
language = str.replace(language, "Language","")
genre = str.replace(soup.find("label",text="Genres").parent.text, "Genres","")
print(genre)
description = soup.find("div",{"itemprop": "description"}).text
cast_list = []
list_actors = soup.find_all("li",{"itemprop": "actor"})
for item in list_actors:
    name = item.find("h4",itemprop = "name").text
    character = item.find("h4",{"class":"character"}).text
    cast_list.append([name,character])
numberOfSeasons = soup.find("span",{"class": "season-count"}).text
