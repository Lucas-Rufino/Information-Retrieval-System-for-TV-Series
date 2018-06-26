import numpy as np 
import math

class Ranking(object): 
    def __init__(self): 
        self.tf = {}
        self.idf = {}
        self.tfidf = {}

    def term_frequency (self, query, document): 
        size = len(document)
        tf = 0
        for x in query.split(): 
            tf += document.count(x)
            if(x not in self.tf.keys()): self.tf.update({x: tf})
            else: self.tf[x] += 1
            if(tf != 0): 
                if(x not in self.idf.keys()): self.idf.update({x: 1})
                else: self.idf[x] += 1
        self.tf = self.tf/size 
    
    def invertet_document_frequency (self, total_documents):
        for x in self.idf: 
            self.idf[x] = math.log2((1/self.idf[x])* total_documents)
    
    def tfxidf(self): 
        for x in self.idf: 
            self.tfidf.update({x: self.idf[x]*self.tf[x]})
    

