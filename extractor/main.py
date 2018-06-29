import os
import utils
import rottentomatoes
import imdb
import tracktv


count = 1;
with open('extractor\srottentomatoes.txt') as f:
    lines = f.readlines()
    f.close()
for site in lines:
    rottentomatoes.get_data(site, count)
    count+=1
    
with open('extractor\stracktv.txt') as f:
    lines = f.readlines()
    f.close()
for site in lines:
    tracktv.get_data(site,count)
    count+=1
