import requests
import json

for n in xrange(4, 5):
    n += 1
    fl = open("links/" + str(n) + ".json")
    ls = json.load(fl)
    fl.close()
    ds = []
    for l in ls:
        print l[0]
        r = requests.get(l[0])
        if r.status_code == 200:
            ds.append([r.text, l[0], l[1]])
    fl = open("htmls/" + str(n) + ".json", "w")
    json.dump(ds, fl)
    fl.close()