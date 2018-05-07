import numpy as np
import json
import pln

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

with open("dataset/edited/trainX.json") as fl:
    trainX = json.load(fl)
    trainX = map(lambda x: pln.vectorize(x) + [1], trainX)
    

with open("dataset/edited/trainY.json") as fl:
    trainY = json.load(fl)
    trainY = map(lambda x: [int(x)], trainY)

# TRAINING EXAMPLES
# problem attribuites + BIAS
X = np.array(trainX)

# Classificator attribuite
Y = np.array(trainY)

# NEURAL NETWORK INITIAL SETUP
numAtt = 101              # Number of problem attribuites + BIAS
numMid = 100              # Number of internal perceptrons
numOut = 1              # Number of out perceptrons
learnT = 60000          # Learning Time

# Random process to init synapses in NN
np.random.seed(1)
syn0 = 2*np.random.random((numAtt, numMid)) - 1
syn1 = 2*np.random.random((numMid, numOut)) - 1

# TRAINING PROCESS
epoch = 1
for j in xrange(learnT):

	# Propagation from input signals to layers 0, 1, and 2
    l0 = X
    l1 = sigmoid(l0.dot(syn0))
    l2 = sigmoid(l1.dot(syn1))

    # BACKPROPAGATION
    # Calculates the error factor from output signal to the expected output
    l2_error = Y - l2
        
    # It calculates the output error impact in output layer
    l2_delta = l2_error * dSigmoid(l2)

    # Calculates the error factor from output layer to the middle layer
    l1_error = l2_delta.dot(syn1.T)
    
    # It calculates the middle error impact in middle layer
    l1_delta = l1_error * dSigmoid(l1)
    
    # Update all layers
    syn1 += 0.01*l1.T.dot(l2_delta)
    syn0 += 0.01*l0.T.dot(l1_delta)
    
    # Show the process of continue learning
    if (j% 10000) == 0:
        print "epoca:", epoch, "- Taxa de acerto:", str(round((1 - np.mean(np.abs(l2_error)))*100, 4)) + "%"
        epoch += 1

def predict(v):
    l0 = np.array([v + [1]])
    l1 = sigmoid(l0.dot(syn0))
    l2 = sigmoid(l1.dot(syn1))
    if l2[0][0] >= 0.5:
        return True
    else: 
        return False
