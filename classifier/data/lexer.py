from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import math
import re

# TESTAR COM E SEM ELES 

#import nltk
#nltk.download('wordnet')

def tokenize(data):
    return data.split()

def normalize(data):
    regex = r'[\\\n\t\"\'\,\.\!\(\)\*\+\-\/\:\;\<\=\>\|\&\@\%\?\[\]\^\_\`\{\|\}\~]'
    data = re.sub(regex, ' ', data)
    data = data.lower()
    return data

_stemmer = None
def stemize(data):
    global _stemmer
    if type(data) == list:
        return map(stemize, data)
    else:
        if _stemmer == None:
            _stemmer = PorterStemmer()
        return _stemmer.stem(data)

_lemma = None
def lemmatize(data):
    global _lemma
    if type(data) == list:
        return map(lemmatize, data)
    else:
        if _lemma == None:
            _lemma = WordNetLemmatizer()
        return _lemma.lemmatize(data)
        
def convertToNumber(s):
    if type(s) == list:
        numbers = map(convertToNumber, s)
        MAX = max(numbers)
        MIN = min(numbers)
        return map(lambda x: (float(x)-MIN)/(MAX - MIN), numbers)
    else:
        ls = [ord(ch) for ch in s]
        num = 0
        for i in ls:
            num <<= 8
            num += i
        return num
        
def preprocess(data):
    data = normalize(data)
    data = tokenize(data)
    #data = lemmatize(data)
    #data = stemize(data)
    #data = convertToNumber(data)
    return data