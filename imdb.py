import reader as r


soup = r.get_link("http://www.imdb.com/title/tt0413573/?ref_=nv_sr_1")
title = soup.find("h1",{"itemprop": "name"}).text
creator = soup.find("span",{"itemprop": "creator"}).text
print(title)
rating = soup.find("span",{"itemprop": "ratingValue" }).text
print (rating)
cast_table = soup.find("table", {"class" : "cast_list"}).find_all("span",{"class": "itemprop"})
for item in cast_table:
    actor = item.text
    print(actor)

character_list = soup.find("table", {"class": "cast_list"}).find_all("td",{"class": "character"})
for item in character_list:
    actor_name = item.find("div").a.text
    print(actor_name)
    
resume = soup.find("div", {"itemprop": "description"}).text
print(resume)
genres = soup.find("div", {"itemprop": "genre"}).find_all("a")
genre = []
for item in genres:
    genre.append(item.text);
print(genre)

details = soup.find("div", {"id": "titleDetails"}).find_all("div")

country = details[1].a.text
language = details[2].a.text
