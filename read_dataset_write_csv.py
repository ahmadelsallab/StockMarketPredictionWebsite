'''
Created on Feb 4, 2014

@author: ASALLAB
'''
from DatasetBuilder.DatasetBuilder import DatasetBuilder
import csv
import pickle
configFileDatasetBuilder = ".\\DatasetBuilder\\Configurations\\Configurations.xml"
csvManualLabelsFileName = ".\\DatasetBuilder\\Output\\ManualLabels_tasi.csv"
datasetSerializationFile = "C:\\Non_valeo\\Guru_Kalam\\Code\\Kalam\\DatasetBuilder\\Output\\dataset_﻿tasi.bin"



serializatoinDatasetFile = open(datasetSerializationFile, 'rb')
dataSet = pickle.load(serializatoinDatasetFile)
serializatoinDatasetFile.close()


# Open the first file
f = open(csvManualLabelsFileName, 'w', encoding='utf-8', newline='')

# Get writer handler, ',' delimited
w = csv.writer(f, delimiter=',')
 
# Fill in the data rows
# Start the heading row
data = []
data.append(['ID', 'Tweet text', 'Relevance label', 'Sentiment label'])

# Fill in each row with the dataset initial labels
for item in dataSet:

    data.append([item['id'], item['text'], item['label'], ' '])
# Dump to the csv file
w.writerows(data)
        
f.close()