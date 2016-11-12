import pickle

StockToClassifier = {}

#initialize with Lexicon
'''f_in = open('.\\TwitterCrawler\\stocks_final_16_3_2014.txt', 'r', encoding='utf-8')#
lines = f_in.readlines()
for line in lines:            
    stock = line.strip()
    StockToClassifier[stock] = "Lexicon"
f_in.close()

serializationFile = open('StockToClassifier.bin', 'wb')
pickle.dump(StockToClassifier, serializationFile)'''

#write dic to file
serializationFile = open('StockToClassifier.bin', 'rb')
StockToClassifier = pickle.load(serializationFile) 

import codecs

with codecs.open('STC', 'w', 'utf-8') as writer:
    for k,v in StockToClassifier.items():
        writer.write("%s | %s \n" % (k,v))