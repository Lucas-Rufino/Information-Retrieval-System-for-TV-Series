import reader as r


soup = r.get_link("https://www.themoviedb.org/tv/1418-the-big-bang-theory")
title = soup.find("div", {"class":"title"}).text
resume = soup.find("div", {"class": "overview"}).text
creator = soup.find_all("li",{"class": "profile"})
creator_list = []
for item in creator:
    creator_list.append(item.text.strip())
cast = soup.find("ol",{"class": "people scroller"}).find_all("li")
cast_list = []
for item in cast:
    cast_list.append(item.text.strip().split("\n"))
genre = soup.find("section",{"class": "genres right_column"}).find("li").text
