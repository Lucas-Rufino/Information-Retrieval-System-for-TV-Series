import requests
import json

def getSite(link):
    r = requests.get(link, verify=False)
    if r.status_code == 200:
        return r.text

def main():
    for n in xrange(10):
        n += 1
        ds = []
        
        print "Getting site:", n
        with open("links/" + str(n) + ".json") as fl:
            ls = json.load(fl)
            fl.close()
        
        for l in ls:
            site = getSite(l[0])
            ds.append([site, l[0], l[1]])
        
        with open("htmls/" + str(n) + ".json", "w") as fl:
            json.dump(ds, fl)
            fl.close()

if __name__ == "__main__":
    main()