from ranking import vectorial_model
from operator import itemgetter
from indexer import index
from database import *
import numpy as np
import math
import json


class Ranking(object):
    def __init__(self, index):
        self.vec_model = vectorial_model.Vectorial_Model()       # Modelo Vetorial utilizado no cosseno
        self.index = index
        self.zone_score = {'title': 1, 'resume':0.8, 'cast':0.64}

    # Build query's vector without tf
    def query_weightless(self, query):
        query = self.build_vec(query)
        r = [1 for x in query]
        return r

    # Remove duplicates information
    def remove_duplicates (self, query):
        return list(set(query))

    def document_weightless(self, query, document, zone_score=False):
        query_vec = self.query_weightless(query)
        query = self.build_vec(query)
        rank = []
        for doc in document:
            cur_doc = self.build_vec(document[doc], document=True, boolean=True)
            cur_doc = self.remove_duplicates(cur_doc)
            vec = []
            for term in query:
                if not zone_score:
                    if(term in cur_doc): vec.append(1)
                    else: vec.append(0)
                else:
                    t = term.split('.')
                    if term in cur_doc: vec.append(self.zone_score[t[1]])
                    else: vec.append(0)
            cos = self.vec_model.cossine(vec, query_vec)
            rank.append((doc, cos))
        return rank

    def query_weight(self, query):
        r = []
        query = self.build_vec(query)
        for term in query:
            r.append(query.count(term))
        return r

    def build_vec(self, query, document=False, boolean=False):
        result = set()
        for att in query:
            for q in query[att]:
                if att == 'genre' or att == 'rate':
                    continue
                if not document or boolean:
                    result.add(q+'.'+att)
                else:
                    result.add(((q+'.'+att), query[att][q]))
        return list(result)

    def document_weight(self, query, document, BM25=False, b=0.75, k1=1.25, zone_score=False):
        result = {}
        rank = []
        idf = {}
        n_doc = self.index.numDocs()
        mean_docs = self.index.meanDocs()
        query_vec = self.query_weight(query)
        query = self.build_vec(query)

        for doc in document:
            tf = {}
            cur_doc = self.build_vec(document[doc], document=True)
            size_doc = self.index.sizeDoc(doc)
            for term in query:
                vec = 0
                has = [True for x in cur_doc if x[0] == term]
                if(len(has) > 0):
                    q = term.split('.')
                    if not zone_score:
                        vec = document[doc][q[1]][q[0]]
                    else: vec = vec*self.zone_score[q[1]]
                    if(BM25):
                        num = vec*(k1 + 1)
                        freq = b*size_doc/mean_docs
                        den = vec + k1*(1-b + freq)
                        vec = num/den
                    if(term in idf.keys()): idf[term] += 1
                    else: idf.update({term: 1})
                else:
                    vec = 0
                    if(term in idf.keys()): idf[term] += 0
                    else: idf.update({term: 0})
                tf.update({term: vec})
            result.update({doc: tf})
        for x in result:
            r = []
            for term in query:
                if idf[term] != 0:
                    if idf[term] == 0 or n_doc/idf[term] == 0:
                        tfidf = 0
                    else:
                        tfidf = result[x][term]*math.log10(n_doc/idf[term])
                else:
                    tfidf = 0
                r.append(tfidf)
            cos = self.vec_model.cossine(r, query_vec)
            rank.append((int(x), cos))
        return rank #list of index


    def all_pairs (self, rank):
        a = set()
        for i in range(len(rank)):
            for j in range(i+1, len(rank)):
                a.add((rank[i], rank[j]))
        return a

    # returns kendal tau correlation between two ranks
    def kendaltau_correlation(self, rank1, rank2):
        k = min(len(rank1), len(rank2))

        pairs1 = self.all_pairs(rank1)
        pairs2 = self.all_pairs(rank2)
        k = len(pairs1) + len(pairs2)
        conc = 0
        disc = 0
        for x in pairs1:
            if(x in pairs2): conc += 2
            else: disc += 2
        diff = abs(conc - disc)
        return diff/k

    def rank(self, query, document, BM25=False, b=0.75, k1=1.25, boolean=False):
        if(not boolean):
            rank = self.document_weight(query, document, BM25, b, k1)
        else:
            rank = self.document_weightless(query, document)
        sort = sorted(rank, key=itemgetter(1), reverse=True)
        sort = [x[0] for x in sort]
        return sort



# TESTE
# r = Ranking()
# inverted_file = {178: {'resume': ['doctor']}, 57: {'resume': ['doctor']}, 155: {'resume': ['doctor']}, 386: {'resume': ['doctor']}, 67: {'resume': ['doctor']}, 305: {'resume': ['doctor']}, 111: {'resume': ['doctor']}, 52: {'resume': ['doctor']}, 224: {'resume': ['doctor']}, 55: {'resume': ['doctor']}}
# query = {'title':['greys', 'doctor', 'doctor'], 'resume':['doctor', 'hospital','grey', 'greys', 'greys', 'hospital']}
# doc = {67: {'title': ['doctor'], 'resume': ['doctor']}, 224: {'title': ['doctor'], 'resume': ['doctor']}, 178: {'resume': ['doctor']}, 57: {'resume': ['doctor']}, 155: {'resume': ['doctor']}, 386: {'resume': ['doctor']}, 305: {'resume': ['doctor']}, 111: {'resume': ['doctor']}, 52: {'resume': ['doctor']}, 55: {'resume': ['doctor']}}
#
# doc_frec = {'67': {'title': {'doctor': 1}, 'resume': {'doctor': 1}},
# '224': {'title': {'doctor': 1}, 'resume': {'doctor': 1}}, '178': {'resume': {'doctor': 1}},
# '57': {'resume': {'doctor': 1}}, '155': {'resume': {'doctor': 1}}, '386': {'resume': {'doctor': 1}},
# '305': {'resume': {'doctor': 1}}, '111': {'resume': {'doctor': 1}}, '52': {'resume': {'doctor': 1}},
# '55': {'resume': {'doctor': 2}}}
#
# #document = ['valdmeiro e muito falso porque ele e muito falso']
# #a = r.query_weightless(query)
# #a = r.query_weight(query)
# #a = r.build_vec(doc_frec['67'], document=True, boolean=False)
# #b = r.document_weight_BM25(query, doc_frec)
# c = r.document_weightless(query, inverted_file)
# #print(c)
