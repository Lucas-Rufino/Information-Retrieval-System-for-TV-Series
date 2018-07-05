from indexer import index
import math

_mutual = {}
_unique = {}
_iFile = index.Basic() #Frequency() ou Positional()
_iFile.load()
_occur = _iFile.ocorrences()
_numDocs = _iFile.numDocs()

def getUnique():
    for attr in _occur.keys():
        aux = _unique.setdefault(attr, {})
        for word in _occur[attr].keys():
            aux.setdefault(word, len(_occur[attr][word])/float(_numDocs))

def getMutual(attr):
    letters = set(list('abcdefghijklmnopqrtuvxwyz'))
    aux = _mutual.setdefault(attr, {})
    keys = sorted(_occur[attr].keys())
    for i, w1 in enumerate(keys):
        for w2 in keys[i+1:]:
            if w1[0] in letters and w2[0] in letters:
                value = len(_occur[attr][w1].intersection(_occur[attr][w2]))/float(_numDocs)
                if value > 0:
                    _mutual[attr][(w1, w2)] = value
                    print(w1, w2)

def mutualInformation(attr):
    data = {}
    for pair in _mutual[attr].keys():
        aux = float(_mutual[attr][pair])
        aux /= _unique[attr][pair[0]]*_unique[attr][pair[1]]
        data[pair] = math.log2(aux)
    return data

def wordsOrder(data, attr):
    order = []
    keys = list(_occur[attr].keys())
    for i, w1 in enumerate(keys):
        total = 0.0
        for w2 in keys[i+1:]:
            total += data.get((w1, w2), 0)
        order.append((total/len(keys), w1))
    return sorted(order, reverse=True)

getUnique()
print('ok UNIQUE')
for attr in ['resume']:
    getMutual(attr)
    print('ok MUTUAL')
    data = mutualInformation(attr)
    order = wordsOrder(data, attr)
    keys = sorted(list(data.keys()))
    data = sorted([(data[key], max(_unique[attr][key[0]],_unique[attr][key[1]]), key) for key in keys], reverse=True)
    print(attr, '- - - - - - - - - - -')
    print('\ntuplas com maiores MI:')
    for d in data[:100]:
        print('/t', d)
    print('\npalavras com maiores MI:')
    for o in order[:100]:
        print('/t', o)
