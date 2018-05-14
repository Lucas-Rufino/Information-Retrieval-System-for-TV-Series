from sklearn.model_selection import StratifiedKFold
from classifier.test import validate
from sklearn.naive_bayes import BernoulliNB
from classifier.data import pln
import json
import time

_clf = None
with open("classifier/data/edited/trainX.json") as fl:
    _trainX = json.load(fl)
    _trainX = list(map(lambda x: pln.vectorize(x), _trainX))

with open("classifier/data/edited/trainY.json") as fl:
    _trainY = json.load(fl)

def fit(trainX=_trainX, trainY=_trainY):
    global _clf
    _clf = BernoulliNB()
    _clf.fit(trainX, trainY)

def predict(x):
    return _clf.predict([x])[0]

def validation():
    skf = StratifiedKFold(10, True, 1)
    precision = []
    f_measure = []
    trainTime = []
    accuracy = []
    testTime = []
    recall = []
    
    for train, test in skf.split(_trainX, _trainY):
        trainX = list(map(lambda x: _trainX[x], train))
        trainY = list(map(lambda x: _trainY[x], train))
        testX = list(map(lambda x: _trainX[x], test))
        testY = list(map(lambda x: _trainY[x], test))
        
        t0 = time.time()
        fit(trainX, trainY)
        trainTime.append(time.time() - t0)
        
        t0 = time.time()
        predY = map(lambda x: predict(x), testX)
        testTime.append((time.time() - t0)/len(testX))
        
        m, l = validate.confuseMatrix(predY, testY)
        precision.append(validate.precision(True, m, l))
        recall.append(validate.recall(True, m, l))
        f_measure.append(validate.f_measure(True, m, l))
        accuracy.append(validate.accuracy(m, l))
    
    print("precision: " + str(round(sum(precision)*100/len(precision), 3)) + "%")
    print("recall: " + str(round(sum(recall)*100/len(recall), 3)) + "%")
    print("f-measure: " + str(round(sum(f_measure)*100/len(f_measure), 3)) + "%")
    print("accuracy: " + str(round(sum(accuracy)*100/len(accuracy), 3)) + "%")
    print("train time: " + str(round(sum(trainTime)/len(trainTime), 6)) + " sec")
    print("test time: " + str(round(sum(testTime)/len(testTime), 6)) + " sec")