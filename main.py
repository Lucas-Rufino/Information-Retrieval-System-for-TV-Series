# from indexer import processor
from indexer import index
from indexer import processor
import json
import os

iFile = index.Frequency() #Basic() ou Positional()
iFile.load()
print(iFile.search({'resume':['event', 'world','friendship']}))

# print(iFile.search({'all':['park', 'android']}))
#
# {
#     'title': processor.text('parque de diversão'),
#     'resume': processor.text('parque de diversão'),
#     'cast': processor.name(''),
#     'rate': processor.number(valor),
#     'genre': ['park', 'android']
# }


# filenames = list(os.walk('database/'))[0][2]
# for filename in filenames:
#     print(filename)
#     with open('database/' + filename) as fl:
#         item = json.load(fl)
#     for attr in ['title', 'genre', 'rate', 'resume', 'cast']:
#         aux = item.get(attr, None)
#         if aux is not None or aux != []:
#             if attr == 'title' or attr == 'resume':
#                 words = processor.text(aux)
#             elif attr == 'cast':
#                 words = []
#                 for actor in aux:
#                     words.extend(processor.text(actor))
#             elif attr == 'genre':
#                 words = processor.category(aux)
#             elif attr == 'rate':
#                 words = processor.number(aux)
#             iFile.insert(int(filename[:-5]), attr, words)
# iFile.save()
