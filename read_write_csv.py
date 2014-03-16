'''
Created on Feb 4, 2014

@author: ASALLAB
'''
from DatasetBuilder.DatasetBuilder import DatasetBuilder
import csv
configFileDatasetBuilder = ".\\DatasetBuilder\\Configurations\\Configurations.xml"
xlsxManualLabelsFileName = ".\\DatasetBuilder\\Output\\ManualLabels_1.csv"
datasetSerializationFile = ".\\DatasetBuilder\\Output\\dataset_1.bin"


# Open csv for reading
f = open(xlsxManualLabelsFileName, 'r', encoding='UTF-8', newline='')

# Get reader handler
r = csv.reader(f, delimiter=',')

# Start at the first entry of the dataset
# By default, the rows are ordered similar to the order of the original dataset
index = 0
dataSet = []
# Skip the first row
skip = True
# Read the label from each row
for row in r:
    if(not skip):
        # Update the label from the manual updated labels
        dataSet[index]['label'] = row[2]
        dataSet[index]['text'] = row[1]
        index += 1
    else:
        skip = False
# Close the file   
f.close()



# Open the first file
f = open(xlsxManualLabelsFileName, 'w', encoding='utf-8', newline='')

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
        
    # Close the old file
    f.close()
