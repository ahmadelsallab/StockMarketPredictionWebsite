'''
Created on Sep 25, 2014

@author: Tarek Abdelhakim
'''
from Filter.Filter import Filter
import pickle

serializationFile = open('/root/kalam/filter.bin', 'rb')
filter = pickle.load(serializationFile)
filter.classifier_Lexicon.labelsNamesMap = pickle.load(serializationFile)
filter.classifier_Tasi.labelsNamesMap = pickle.load(serializationFile)
serializationFile.close()

def Classify(text, stockName):
    result = filter.Classify(text,stockName)
    return result
        