def confuseMatrix(predY, testY):
    labels = dict()
    classes = sorted(list(set(testY)))
    matrix = list(map(lambda _: [0]*len(classes), range(len(classes))))
    for i, c in enumerate(classes):
        labels[c] = i
    for y in zip(predY, testY):
        matrix[y[0]][y[1]] += 1
    return matrix, labels

def precision(label, matrix, labels):
    i = labels[label]
    return float(matrix[i][i])/sum(matrix[i])

def recall(label, matrix, labels):
    i = labels[label]
    return float(matrix[i][i])/sum(map(lambda x: x[i], matrix))

def f_measure(label, matrix, labels):
    p = precision(label, matrix, labels)
    r = recall(label, matrix, labels)
    return (2.0*p*r)/(p+r)

def accuracy(matrix, labels):
    total = sum(map(lambda x: matrix[x][x], labels.keys()))
    return float(total)/sum(map(lambda x: sum(x), matrix))