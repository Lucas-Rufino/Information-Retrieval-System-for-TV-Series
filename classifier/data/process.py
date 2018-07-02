from classifier.data import lexer
import json

trainX = []
trainY = []

for i in xrange(10):
    i += 1
    with open("htmls/" + str(i) + ".json") as fl:
        ls = json.load(fl)
        fl.close()
    
    print "processing site:", i
    func = lambda x: lexer.preprocess(x[1]) + lexer.preprocess(x[0])
    trainY.extend(map(lambda x: x[2], ls))
    trainX.extend(map(func, ls))

with open("edited/trainX.json", 'w') as fl:
    json.dump(trainX, fl)

with open("edited/trainY.json", 'w') as fl:
    json.dump(trainY, fl)