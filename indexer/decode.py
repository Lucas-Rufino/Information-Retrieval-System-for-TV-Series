from indexer import index

def interval(data, idx):
    code = {}
    if type(idx) == index.Basic:
        for attr in data.keys():
            code.setdefault(attr, {})
            for word in data[attr].keys():
                acc = 0
                ls = code[attr].setdefault(word, [])
                for i, id in enumerate(data[attr][word]):
                    ls.append(id + acc)
                    acc += ls[-1]
        return code
    elif type(idx) == index.Frequency:
        pass
    elif type(idx) == index.Positional:
        pass
    else:
        return data
