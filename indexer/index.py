from indexer import encode, decode
import pickle
import json

class Inverted(object):
    def __init__(self, local):
        self._attrs = set(['title', 'genre', 'rate', 'resume', 'cast'])
        self._local = local
        self._db = {}

    def load(self, mode='normal', serialize=False):
        s = 'serialized/db' if serialize else 'db'
        path = 'indexer/database/' + self._local + mode + '/' + s
        with open(path) as fl:
            data = pickle.load(fl) if serialize else json.load(fl)
        if mode ==  'normal':
            self._db = data
        elif mode ==  'interval':
            self._db = decode.interval(data)
        elif mode ==  'bytecode':
            self._db = decode.bytecode(data)

    def save(self, mode='normal', serialize=False):
        data = None
        s = 'serialized/db' if serialize else 'db'
        path = 'indexer/database/' + self._local + mode + '/' + s
        if mode ==  'normal':
            data = self._db
        elif mode ==  'interval':
            data = encode.interval(self._db)
        elif mode ==  'bytecode':
            data = encode.bytecode(self._db)
        with open(path, 'w') as fl:
            pickle.dump(data, fl) if serialize else json.dump(data, fl)

    def covertAll(self, by):
        all = by.get('all', None)
        if all is not None:
            by = { attr:all for attr in self._attrs }
        return by

class Basic(Inverted):
    def __init__(self):
        super().__init__("basic/")

    def insert(self, id, attr, words):
        if type(words) == str:
            words = [words]
        for word in words:
            aux = self._db.setdefault(attr, {})
            aux = aux.setdefault(word, [])
            if id not in aux:
                aux.append(id)

    def search(self, by):
        result = {}
        by = self.covertAll(by)
        for attr in by.keys():
            if attr in self._attrs:
                aux = self._db.get(attr, None)
                if aux is not None:
                    for word in by[attr]:
                        aux2 = aux.get(word, None)
                        if aux2 is not None:
                            for id in aux2:
                                i = result.setdefault(id, {})
                                i = i.setdefault(attr, [])
                                i.append(word)
        return result

class Frequency(Inverted):
    def __init__(self):
        super().__init__("frequency/")

    def insert(self, id, attr, words):
        if type(words) == str:
            words = [words]
        for word in words:
            aux = self._db.setdefault(attr, {})
            aux = aux.setdefault(word, {})
            aux.setdefault(id, 0)
            aux[id] += 1

    def search(self, by):
        result = {}
        by = self.covertAll(by)
        for attr in by.keys():
            if attr in self._attrs:
                aux = self._db.get(attr, None)
                if aux is not None:
                    for word in by[attr]:
                        aux2 = aux.get(word, None)
                        if aux2 is not None:
                            for id in aux2.keys():
                                i = result.setdefault(id, {})
                                i = i.setdefault(attr, {})
                                i.setdefault(word, aux2[id])
        return result

class Positional(Inverted):
    def __init__(self):
        super().__init__("positional/")

    def insert(self, id, attr, words):
        if type(words) == str:
            words = [words]
        for i, word in enumerate(words):
            aux = self._db.setdefault(attr, {})
            aux = aux.setdefault(word, {})
            aux = aux.setdefault(id, [])
            aux.append(i)

    def search(self, by):
        result = {}
        by = self.covertAll(by)
        for attr in by.keys():
            if attr in self._attrs:
                aux = self._db.get(attr, None)
                if aux is not None:
                    for word in by[attr]:
                        aux2 = aux.get(word, None)
                        if aux2 is not None:
                            for id in aux2.keys():
                                i = result.setdefault(id, {})
                                i = i.setdefault(attr, {})
                                i.setdefault(word, aux2[id])
        return result
