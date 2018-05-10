from data import pln
import json

with open("classifier/data/edited/trainX.json") as fl:
    trainX = json.load(fl)
    trainX = map(lambda x: pln.vectorize(x), trainX)
    
with open("classifier/data/edited/trainY.json") as fl:
    trainY = json.load(fl)

def fit(trainX, trainY):
    pass

def hamming(v, t):
    match = zip(v, t)
    total = sum(map(lambda x: 0 if x[0] == x[1] else 1, match))
    return total

_k = 1  
def predict(v):
    dists = map(lambda x, l: [hamming(v, x), l], trainX, trainY)
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