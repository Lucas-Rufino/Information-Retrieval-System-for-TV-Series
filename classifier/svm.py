from sklearn import svm
from data import pln
import json

_clf = None
with open("classifier/data/edited/trainX.json") as fl:
    _trainX = json.load(fl)
    _trainX = map(lambda x: pln.vectorize(x), _trainX)

with open("classifier/data/edited/trainY.json") as fl:
    _trainY = json.load(fl)

def fit(trainX=_trainX, trainY=_trainY):
    global _clf
    _clf = svm.SVC()
    _clf.fit(trainX, trainY)

def predict(x):
    return _clf.predict([x])[0]