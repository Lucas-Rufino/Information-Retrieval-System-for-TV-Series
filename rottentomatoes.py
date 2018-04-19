import reader as r


soup = r.get_link("https://www.rottentomatoes.com/tv/lost_in_space/")
title = soup.find("h1", {"class":"title"}).text
resume = soup.find("div", {"id": "movieSynopsis"}).text
genre = soup.find("td", text = "Genre:").parent.text
cast = soup.find_all("div",{"class":"cast-item media inlineBlock "})
cast_list = []
for item in cast:
    actor = item.find("div").find("a").text.strip()
    characther = str.replace(item.find("span",{"class": "characters subtle smaller"}).text,"as ","")
    cast_list.append([actor,characther])
rate = soup.find("div",{"class":"critic-score meter"}).span.text


