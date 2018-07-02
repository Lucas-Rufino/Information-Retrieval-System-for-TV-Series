from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
stopwords.words('english')
import math, re

# import nltk
# nltk.download('wordnet')
# nltk.download('stopwords')

def tokenize(data):
    return data.split()

def normalize(data):
    if type(data) == list:
        return list(map(normalize, data))
    else:
        rx = r'[\\\"\'\,\.\!\(\)\*\+\-\/\:\;\<\=\>\|\&\@\%\?\[\]\^\_\`\{\|\}\~]'
        data = re.sub(rx, ' ', data)
        data = data.lower()
        return data

_stemmer = None
def stemize(data):
    global _stemmer
    if type(data) == list:
        return list(map(stemize, data))
    else:
        if _stemmer == None:
            _stemmer = PorterStemmer()
        return _stemmer.stem(data)

_stopword = None
def stopword(data):
    global _stopword
    if type(data) == list:
        return list(filter(stopword, data))
    else:
        if _stopword == None:
            _stopword = set(stopwords.words('english'))
        return data not in _stopword

_lemma = None
def lemmatize(data):
    global _lemma
    if type(data) == list:
        return list(map(lemmatize, data))
    else:
        if _lemma == None:
            _lemma = WordNetLemmatizer()
        return _lemma.lemmatize(data)

def text(data):
    data = normalize(data)
    data = tokenize(data)
    data = stopword(data)
    data = stemize(data)
    # data = lemmatize(data)
    return data

_categories = {}
def category(data):
    return [ _categories.get(x, x) for x in data]

_numbers = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
def number(data):
    for i, num in enumerate(_numbers):
        if data <= num:
            return str([i, i+1])
    return "[]"
