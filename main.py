# from indexer import processor
from indexer import index
from indexer import processor
import json
import os

iFile = index.Basic() #Basic() ou Positional()
iFile.load()
# iFile.save(mode='bytecode', serialize=True)
# print(iFile.search({'resume':['event', 'world','friendship']}))

# print(iFile.search({'all':['park', 'android']}))
#
# {
#     'title': processor.text('parque de diversao'),
#     'resume': processor.text('parque de diversao'),
#     'cast': processor.name(''),
#     'rate': processor.number(valor),
#     'genre': ['park', 'android']
# }


# filenames = list(os.walk('database/'))[0][2]
# filenames = sorted([ int(f[:-5]) for f in filenames if f != '.DS_Store' ])
# for i, filename in enumerate(filenames):
#     print(i, '-', filename)
#     with open('database/' + str(filename) + '.json') as fl:
#         item = json.load(fl)
#     for attr in ['title', 'genre', 'rate', 'resume', 'cast']:
#         aux = item.get(attr, None)
#         if aux is not None and aux != []:
#             if attr == 'title' or attr == 'resume':
#                 words = processor.text(aux)
#             elif attr == 'cast':
#                 words = []
#                 for actor in aux:
#                     words.extend(processor.name(actor))
#             elif attr == 'genre':
#                 words = processor.category(aux)
#             elif attr == 'rate':
#                 words = processor.number(aux)
#             iFile.insert(filename, attr, words)
# iFile.save()
print(iFile.meanDocs())
print(iFile.sumDocs())
