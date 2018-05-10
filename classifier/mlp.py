from sklearn.model_selection import StratifiedKFold
from classifier.test import validate
from classifier.data import pln
import numpy as np
import json
import time

_syn0 = None
_syn1 = None

with open("classifier/data/edited/trainX.json") as fl:
    _trainX = json.load(fl)
    _trainX = map(lambda x: pln.vectorize(x), _trainX)

with open("classifier/data/edited/trainY.json") as fl:
    _trainY = json.load(fl)
    _trainY = map(lambda x: int(x), _trainY)

def dSigmoid(x):
    """
    function to generate a error signal to correct the MLP on backpropagation
    @param X - Numpy array - vector to be transformed using sigmoid derivative
    """
    return x*(1-x)

def sigmoid(x):
    """
    threshold function to infer the activating of a hiperplane according 
    to sigmoid function.
    @param X - Numpy array - vector to be transformed using sigmoid function
    """
    return 1/(1+np.exp(-x))

def fit(trainX=_trainX, trainY=_trainY, learnT=10000):
    global _syn0, _syn1
    # TRAINING EXAMPLES
    X = np.array(map(lambda x: x + [1], trainX))  # problem attribuites + BIAS
    Y = np.array(map(lambda x: [x], trainY))      # Classificator attribuite
    
    # NEURAL NETWORK INITIAL SETUP
    numAtt = 101            # Number of problem attribuites + BIAS
    numMid = 100            # Number of internal perceptrons
    numOut = 1              # Number of out perceptrons
    
    # Random process to init synapses in NN
    np.random.seed(1)
    _syn0 = 2*np.random.random((numAtt, numMid)) - 1
    _syn1 = 2*np.random.random((numMid, numOut)) - 1
    
    # TRAINING PROCESS
    for j in range(learnT):
    
    	# Propagation from input signals to layers 0, 1, and 2
        l0 = X
        l1 = sigmoid(l0.dot(_syn0))
        l2 = sigmoid(l1.dot(_syn1))
    
        # BACKPROPAGATION
        # Calculates the error factor from output signal to the expected output
        l2_error = Y - l2
            
        # It calculates the output error impact in output layer
        l2_delta = l2_error * dSigmoid(l2)
    
        # Calculates the error factor from output layer to the middle layer
        l1_error = l2_delta.dot(_syn1.T)
        
        # It calculates the middle error impact in middle layer
        l1_delta = l1_error * dSigmoid(l1)
        
        # Update all layers
        _syn1 += 0.01*l1.T.dot(l2_delta)
        _syn0 += 0.01*l0.T.dot(l1_delta)
        
        # Show the process of continue learning
    #else:
    #    print "Taxa de acerto:", str(round((1 - np.mean(np.abs(l2_error)))*100, 4)) + "%"

def predict(v):
    l0 = np.array([v + [1]])
    l1 = sigmoid(l0.dot(_syn0))
    l2 = sigmoid(l1.dot(_syn1))
    if l2[0][0] >= 0.5:
        return True
    else: 
        return False

def validation():
    skf = StratifiedKFold(10, True, 1)
    precision = []
    f_measure = []
    trainTime = []
    accuracy = []
    testTime = []
    recall = []
    
    for train, test in skf.split(_trainX, _trainY):
        trainX = map(lambda x: _trainX[x], train)
        trainY = map(lambda x: _trainY[x], train)
        testX = map(lambda x: _trainX[x], test)
        testY = map(lambda x: _trainY[x], test)
        
        t0 = time.time()
        fit(trainX, trainY)
        trainTime.append(time.time() - t0)
        
        t0 = time.time()
        predY = map(lambda x: predict(x), testX)
        testTime.append((time.time() - t0)/len(testX))
        
        m, l = validate.confuseMatrix(predY, testY)
        precision.append(validate.precision(True, m, l))
        recall.append(validate.recall(True, m, l))
        f_measure.append(validate.f_measure(True, m, l))
        accuracy.append(validate.accuracy(m, l))
    
    print("precision: " + str(round(sum(precision)*100/len(precision), 2)) + "%")
    print("recall: " + str(round(sum(recall)*100/len(recall), 2)) + "%")
    print("f-measure: " + str(round(sum(f_measure)*100/len(f_measure), 2)) + "%")
    print("accuracy: " + str(round(sum(accuracy)*100/len(accuracy), 2)) + "%")
    print("train time: " + str(sum(f_measure)*100/len(f_measure)) + "sec")
    print("test time: " + str(sum(accuracy)*100/len(accuracy)) + "sec")