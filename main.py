from classifier.data import pln
from classifier import bayes
from classifier import logis
from classifier import tree
from classifier import knn
from classifier import mlp
from classifier import svm

print("BAYES --- --- --- ---")
bayes.validation()
print("\nLOGIS --- --- --- ---")
logis.validation()
print("\nTREE --- --- --- ---")
tree.validation()
print("\nKNN --- --- --- ---")
knn.validation()
print("\nMLP --- --- --- ---")
mlp.validation()
print("\nSVM --- --- --- ---")
svm.validation()