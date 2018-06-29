import json

with open('edited/trainX.json') as fl:
    trainX = json.load(fl)

with open('edited/trainY.json') as fl:
    trainY = json.load(fl)

attrs = []
attrsSET = set()
attrsDICT = dict()
for i in xrange(len(trainY)):
    if trainY[i] == True:
        for w in trainX[i]:
            if w not in attrsSET:
                attrsSET.add(w)
                attrs.append(w)
                attrsDICT[w] = len(attrs) - 1

ds = []
for i in xrange(len(trainY)):
    ds.append([0]*len(attrs))
    for w in trainX[i]:
        try:
            ds[-1][attrsDICT[w]] = 1
        except Exception:
            pass

with open('words.arff', 'w') as fl:
    fl.write("@relation words\n\n")
    for a in attrs:
        fl.write("@attribute " + a.encode('utf-8') + " {" + str(1) + ", " + str(0) + "}\n")
    fl.write("@attribute CLASS {" + str(True) + ", " + str(False) + "}\n")
    fl.write("\n@data\n")
    
    
    for i in xrange(len(ds)):
        fl.write(str(ds[i])[1:-1])
        fl.write(", ")
        fl.write(str(trainY[i]))
        fl.write("\n")