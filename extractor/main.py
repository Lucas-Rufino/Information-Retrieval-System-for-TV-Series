import os
import utils
import rottentomatoes
import imdb
import tracktv
import tvguide
import tvmovieDB


# count = 1;
# with open('extractor\srottentomatoes.txt') as f:
#     lines = f.readlines()
#     f.close()
# for site in lines:
#     rottentomatoes.get_data(site, str(count))
#     count+=1
    
# data = utils.readJson('extractor\stvMovieDB2.json')
# for site in data:
#     tvmovieDB.get_data(site[1],str(site[0]))
    

# with open('extractor\stvmovieDB.txt') as f:
#     lines = f.readlines()
#     f.close()
# for site in lines:
#     tvmovieDB.get_data(site,str(count))
#     count+=1
path = "extractor/tvmovidDB"
name_series = []
for filename in os.listdir(path):
    fullpath = os.path.join(path, filename)
    data = utils.readJson(fullpath)
    for i in data['cast']:
        if i not in name_series:
            name_series.append(i)
data = {}
data['cast_names'] = name_series
utils.writeToJson("cast_series", "extractor/",data)