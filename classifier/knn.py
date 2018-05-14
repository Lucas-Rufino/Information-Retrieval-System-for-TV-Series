from sklearn.model_selection import StratifiedKFold
from classifier.test import validate
from classifier.data import pln
import json
import time

with open("classifier/data/edited/trainX.json") as fl:
    _trainX = json.load(fl)
    _trainX = list(map(lambda x: pln.vectorize(x), _trainX))
    
with open("classifier/data/edited/trainY.json") as fl:
    _trainY = json.load(fl)

def fit(trainX=None, trainY=None):
    return None

def hamming(v, t):
    match = zip(v, t)
    total = sum(map(lambda x: 0 if x[0] == x[1] else 1, match))
    return total

_k = 1  
def predict(v):
    dists = list(map(lambda x, l: [hamming(v, x), l], _trainX, _trainY))
    dists.sort()
    neighbors = dists[:_k]
    
    result = None
    ls = [(0,), (0,)]
    while len(ls) > 1 and ls[-1][0] == ls[-2][0]:   # criteiro de desempate
        ls = []
        count = {}
        for i in neighbors:                         # para as classes do prob.
            count[i[1]] = count.get(i[1], 0) + 1    # conte a freguencia de cada
        for key in count.keys():                    # para cada classe
            ls.append((count[key], key))            # adicione o total na lista
        ls.sort()                                   # ordena a lista
        result = ls[-1][-1]                         # pega o maior valor
        neighbors.pop()                             # remove um K para desempate
    return result

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