import os
import utils
import rottentomatoes
import imdb
import tracktv
import tvguide
import tvmovieDB


count = 1;
# with open('extractor\srottentomatoes.txt') as f:
#     lines = f.readlines()
#     f.close()
# for site in lines:
#     rottentomatoes.get_data(site, str(count))
#     count+=1
    
# with open('extractor\stracktv.txt') as f:
#     lines = f.readlines()
#     f.close()
# for site in lines:
#     tracktv.get_data(site,str(count))
#     count+=1

with open('extractor\stvmovieDB.txt') as f:
    lines = f.readlines()
    f.close()
for site in lines:
    tvmovieDB.get_data(site,str(count))
    count+=1
