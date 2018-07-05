from nltk.stem.porter import PorterStemmer
try:
    from nltk.corpus import stopwords
    stopwords.words('english')
except Exception:
    import nltk
    nltk.download('wordnet')
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    stopwords.words('english')
import math, re

def tokenize(data):
    return data.split()

def normalize(data):
    if type(data) == list:
        return list(map(normalize, data))
    else:
        rx = r'[\\\"\'\,\.\!\(\)\*\+\-\/\:\;\<\=\>\|\&\@\%\?\[\]\^\_\`\{\|\}\~\$\#\t\n]'
        data = re.sub(rx, ' ', data)
        data = re.sub(r'[ÀÁÂÄÅàáâãäåāăą]', 'a', data)
        data = re.sub(r'[ÈÉèéêëēėęě]', 'e', data)
        data = re.sub(r'[Íìíîï]', 'i', data)
        data = re.sub(r'[ÓÔÕÖðòóôõöŌōŏő]', 'o', data)
        data = re.sub(r'[ÚÜùúûüùúûü]', 'o', data)
        data = re.sub(r'[ÇçĆćČč]', 'c', data)
        data = re.sub(r'[ý]', 'y', data)
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
    return data

def name(data):
    data = normalize(data)
    data = tokenize(data)
    return data

# ['action', 'adventure', 'animation', 'anime', 'biography', 'comedy', 'crime',
# 'documentary', 'drama', 'erotic', 'family', 'fantasy', 'fiction', 'gameshow',
# 'history', 'homeandgarden', 'horror', 'kids', 'movie', 'music', 'musical',
# 'mystery', 'news', 'politics', 'reality', 'romance', 'scifi', 'soap',
# 'specialinterest', 'sport', 'superhero', 'suspense', 'talkshow', 'thriller',
# 'war', 'western']
_categories = { 'children': 'kids', 'realitytv': 'reality', 'science': 'scifi',
    'sciencefiction': 'scifi', 'talk': 'talkshow'}
def category(data):
    data = normalize(data)
    data = [ x.replace(' ', '') for x in data ]
    return [ _categories.get(x, x) for x in data ]

_numbers = [0, 43, 53, 60, 62, 65, 69, 70, 72, 75, 77, 79, 80, 82, 86, 91, 100]
def number(data):
    for i, num in enumerate(_numbers):
        if data <= num:
            return [str([i, i+1])]
    return "[]"
