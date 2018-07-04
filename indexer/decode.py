def interval(data, mode):
    code = {}
    if mode == "basic/":
        for attr in data.keys():
            aux = code.setdefault(attr, {})
            for word in data[attr].keys():
                ids = data[attr][word]
                ls = aux.setdefault(word, [ids[0]])
                for i, id in enumerate(ids[:-1]):
                    ls.append(ids[i+1] - ids[i])
    elif mode == "frequency/":
        for attr in data.keys():
            aux = code.setdefault(attr, {})
            for word in data[attr].keys():
                ids = data[attr][word]
                pair = aux.setdefault(word, [None, None])
                keys = [ int(x) for x in ids.keys() ]
                pair[1] = [ ids[key] for key in keys ]
                pair[0] = [ids[keys[0]]]
                for i, id in enumerate(keys[:-1]):
                    pair[0].append(ids[keys[i+1]] - ids[keys[i]])
    elif mode == "positional/":
        pass
    else:
        return data
