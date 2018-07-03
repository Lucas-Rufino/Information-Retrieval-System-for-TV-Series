from indexer import index

def interval(data, idx):
    code = {}
    if type(idx) == index.Basic:
        for attr in data.keys():
            code.setdefault(attr, {})
            for word in data[attr].keys():
                acc = sum(data[attr][word][:1])
                ls = code[attr].setdefault(word, [])
                ls.append(acc)
                for i, id in enumerate(data[attr][word][:-1]):
                    ls.append(data[attr][word][i+1] - acc)
                    acc += ls[-1]
        return code
    elif type(idx) == index.Frequency:
        pass
    elif type(idx) == index.Positional:
        pass
    else:
        return data
