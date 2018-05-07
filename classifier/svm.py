from sklearn import svm
from data import pln
import json

with open("data/edited/trainX.json") as fl:
    trainX = json.load(fl)
    trainX = map(lambda x: pln.vectorize(x), trainX)
    
with open("data/edited/trainY.json") as fl:
    trainY = json.load(fl)

clf = svm.SVC()
clf.fit(trainX, trainY)

def predict(v):
    return clf.predict([v])[0]