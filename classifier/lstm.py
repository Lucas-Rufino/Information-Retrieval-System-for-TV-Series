from keras.utils.np_utils import to_categorical
from keras.layers.embeddings import Embedding
from keras.layers import Dropout
from keras.models import Sequential
from keras.preprocessing import sequence
from keras.layers import Dense
from keras.layers import LSTM
import numpy as np
from classifier.data import lexer
import json

trainX = []
trainY = []

for i in xrange(10):
    i += 1
    with open("classifier/data/htmls/" + str(i) + ".json") as fl:
        ls = json.load(fl)
        fl.close()
    
    func = lambda x: np.array(lexer.preprocess(x[1]) + lexer.preprocess(x[0]))
    trainY.extend(map(lambda x: x[2], ls))
    trainX.extend(map(func, ls))
    print "get data file:", i

top_words = 5000
max_html_length = 10000
embedding_vecor_length = 32

trainX = sequence.pad_sequences(np.array(trainX), maxlen=max_html_length)
trainY = to_categorical(np.array(trainY))

model = Sequential()
model.add(Embedding(top_words, embedding_vecor_length, input_length=max_html_length))
model.add(Dropout(0.2))
model.add(LSTM(100))
model.add(Dropout(0.2))
model.add(Dense(2, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(trainX, trainY, epochs=10, batch_size=1) #validation_data=(X_test, y_test)