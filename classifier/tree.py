import pln

def predict(v):
    if v[pln._dicws['tvseries']] == 1:
        if v[pln._dicws['full']] == 1:
            return True
        else:
            return False
    else:
        if v[pln._dicws['shows']] == 1:
            return False
        else:
            if v[pln._dicws['o']] == 1:
                if v[pln._dicws['show']] == 1:
                    if v[pln._dicws['end']] == 1:
                        return False
                    else:
                        return True
                else:
                    return False
            else:
                return False