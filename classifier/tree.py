from classifier.data import pln

def fit(trainX=None, trainY=None):
    print("trained")

def predict(x):
    if x[pln._dicws['tvseries']] == 1:
        if x[pln._dicws['full']] == 1:
            return True
        else:
            return False
    else:
        if x[pln._dicws['shows']] == 1:
            return False
        else:
            if x[pln._dicws['o']] == 1:
                if x[pln._dicws['show']] == 1:
                    if x[pln._dicws['end']] == 1:
                        return False
                    else:
                        return True
                else:
                    return False
            else:
                return False