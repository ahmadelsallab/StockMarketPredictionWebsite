'''
Created on Sep 25, 2014

@author: Tarek Abdelhakim
'''
from Filter.Filter import Filter
import pickle

filter = Filter('/srv/www/htdocs/kalam')
serializationFile = open('filter.bin', 'wb')
pickle.dump(filter, serializationFile)
pickle.dump(filter.classifier_Lexicon.labelsNamesMap, serializationFile)
pickle.dump(filter.classifier_Tasi.labelsNamesMap, serializationFile)