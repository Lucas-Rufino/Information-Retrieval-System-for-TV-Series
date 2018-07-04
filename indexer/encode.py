def interval(data, mode):
    code = {}
    if mode == "basic/":
        for attr in data.keys():
            aux = code.setdefault(attr, {})
            for word in data[attr].keys():
                ids = data[attr][word]
                ls = aux.setdefault(word, [ids[0]])
                for i, _ in enumerate(ids[:-1]):
                    ls.append(ids[i+1] - ids[i])
        return code
    elif mode == "frequency/":
        for attr in data.keys():
            aux = code.setdefault(attr, {})
            for word in data[attr].keys():
                ids = data[attr][word]
                pair = aux.setdefault(word, [None, None])
                keys = sorted([ int(x) for x in ids.keys() ])
                pair[1] = [ ids[str(key)] for key in keys ]
                pair[0] = [keys[0]]
                for i, _ in enumerate(keys[:-1]):
                    pair[0].append(keys[i+1] - keys[i])
        return code
    elif mode == "positional/":
        for attr in data.keys():
            aux = code.setdefault(attr, {})
            for word in data[attr].keys():
                ids = data[attr][word]
                pair = aux.setdefault(word, [None, []])
                keys = sorted([ int(x) for x in ids.keys() ])
                pair[0] = [keys[0]]
                for i, _ in enumerate(keys[:-1]):
                    pair[0].append(keys[i+1] - keys[i])
                for key in keys:
                    vls = ids[str(key)]
                    ls = [vls[0]]
                    for i, _ in enumerate(vls[:-1]):
                        ls.append(vls[i+1] - vls[i])
                    pair[1].append(ls)
        return code
    else:
        return data
        
def encodeValue(val):
    ls = []
    if val < 0x80:
        ls.append(val)
    elif val < 0x4000:
        val |= 0x8000
        ls.append(val >> 8)
        ls.append((val) & 0xFF)
    elif val < 0x200000:
        val |= 0xC00000
        ls.append(val >> 16)
        ls.append((val >> 8) & 0xFF)
        ls.append((val) & 0xFF)
    elif val < 0x10000000:
        val |= 0xE0000000
        ls.append(val >> 24)
        ls.append((val >> 16) & 0xFF)
        ls.append((val >> 8) & 0xFF)
        ls.append((val) & 0xFF)
    else:
        ls.append(0xF0)
        ls.append(val >> 24)
        ls.append((val >> 16) & 0xFF)
        ls.append((val >> 8) & 0xFF)
        ls.append((val) & 0xFF)
    return ls

def bytecode(data, mode):
    code = {}
    if mode == "basic/":
        for attr in data.keys():
            aux = code.setdefault(attr, {})
            for word in data[attr].keys():
                ids = data[attr][word]
                ls = aux.setdefault(word, [])
                for i in ids:
                    ls.extend(encodeValue(i))
                aux[word] = bytes(ls)
                
        return code
    elif mode == "frequency/":
        for attr in data.keys():
            aux = code.setdefault(attr, {})
            for word in data[attr].keys():
                ids = data[attr][word]
                pair = aux.setdefault(word, [[], None])
                keys = sorted([ int(x) for x in ids.keys() ])
                pair[1] = [ ids[str(key)] for key in keys ]
                for key in keys:
                    pair[0].extend(encodeValue(key))
                pair[0] = bytes(pair[0])
        return code
    elif mode == "positional/":
        for attr in data.keys():
            aux = code.setdefault(attr, {})
            for word in data[attr].keys():
                ids = data[attr][word]
                pair = aux.setdefault(word, [[], []])
                keys = sorted([ int(x) for x in ids.keys() ])
                for key in keys:
                    pair[0].extend(encodeValue(key))
                    vls = ids[str(key)]
                    ls = []
                    for v in vls:
                        ls.extend(encodeValue(v))
                    pair[1].append(bytes(ls))
                pair[0] = bytes(pair[0])
        return code
    else:
        return data
