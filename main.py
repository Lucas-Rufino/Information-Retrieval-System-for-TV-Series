from classifier import tree as clf
from classifier.data import pln

clf.fit()       #sem parametros ele usa automaticamente a base que montei

instance = pln.process("""HTML CONCATENADO COM URL""") # a entrada aqui
print(clf.predict(instance))