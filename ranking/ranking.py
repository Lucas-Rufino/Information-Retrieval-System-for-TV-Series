import numpy as np 
import math

class Ranking(object): 
    def __init__(self): 
        self.tf = {}
        self.idf = {}
        self.tfidf = {}

    # Remove duplicates from query 
    def remove_duplicates(self, query): 
        q = set()
        for x in query: 
            q.add(x)
        return q 
    
    def query_weightless(self, query): 
        result = [1 for i in range(len(query))]
        return result
    
    def document_weightless(self, query, document): 
        result = []
        for x in query: 
            if x in document: result.append(1)
            else: result.append(0)
        return result
    # 
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
    
    # 
    def invertet_document_frequency (self, total_documents):
        for x in self.idf: 
            self.idf[x] = math.log2((1/self.idf[x])* total_documents)
    
    # Calcule TFIDF of the query queryM
    def tfxidf(self): 
        query = []
        for x in self.idf: 
            self.tfidf.update({x: self.idf[x]*self.tf[x]})
            query.append(self.idf[x]*self.tf[x])
        return query 
    
    
    def all_pairs (self, rank): 
        a = set()
        for i in range(len(rank)): 
            for j in range(i+1, len(rank)):
                a.add((rank[i], rank[j]))
        return a 

    # returns kendal tau correlation between two ranks 
    def kendaltau_correlation(self, rank1, rank2 ):
        k = len(rank1)
        npar = k*(k-1)
        pairs1 = self.all_pairs(rank1)
        pairs2 = self.all_pairs(rank2)
        conc = 0 
        disc = 0
        for x in pairs1: 
            if(x in pairs2): conc += 1
            else: disc += 1
        
        result = math.abs(conc - disc)/npar
        return result


        
# TESTE 
r = Ranking() 
query = ['valdemiro', 'falsidade', 'vinganca', 'falsidade', 'a', 'google']
document = ['valdmeiro e muito falso porque ele e muito falso']
a = r.remove_duplicates(query)

print(a)
    # Duvida: 
    # 
    # como monta o vetor da query e documento (calcular o tfidf dentro da query e fazer que fiz antes)
    # como monta o vetor da query sem o tfidf 
    # é pra usar o cosseno? pode usar jaccard? (implementar ambos ) 
    # par importa a ordem que aparece no ranking (importa)
    # 
    # 
    # 
    # 
    #
    # 
