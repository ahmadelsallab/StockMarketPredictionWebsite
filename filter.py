'''
Created on Oct 21, 2013

@author: ASALLAB
'''
from TwitterCrawler.TwitterCrawler import TwitterCrawler
from DatasetBuilder.DatasetBuilder import DatasetBuilder
from LanguageModel.LanguageModel import LanguageModel   
from FeaturesExtractor.FeaturesExtractor import FeaturesExtractor
from Classifier.Classifier import Classifier
import pickle
from collections import OrderedDict

# Start the DatasetBuilder
#-------------------------
# Configurations file xml of the dataset builder
configFileDatasetBuilder = ".\\DatasetBuilder\\Configurations\\Configurations.xml"

# The CSV file name for tweets to be manually labeled
csvManualLabelsFileName = ".\\DatasetBuilder\\Output\\ManualLabels"

# The XLSX file name for tweets to be manually labeled
xlsxManualLabelsFileName = ".\\DatasetBuilder\\Output\\Completed\\ManualLabels"

# The serialization file to save the dataset
datasetSerializationFile = ".\\DatasetBuilder\\Output\\dataset.bin"

# Train/Test serialization file
trainTestSerializationFile = ".\\DatasetBuilder\\Output\\train_test_dataset.bin"



# Initialize the DatasetBuilder from serialization file
datasetBuilder = DatasetBuilder(configFileDatasetBuilder, [], datasetSerializationFile)

# Load the dataset
#datasetBuilder.LoadDataset()

# Update the labels
numFiles = 50
for i in range(numFiles):
	print('Updating labels from file ' + xlsxManualLabelsFileName  + "_" + str(i + 1) + '...')
	datasetBuilder.UpdateManualLabelsFromXLSXFile(xlsxManualLabelsFileName  + "_" + str(i + 1), (i + 1)) # This should be done separately when dataset is manually labeled


# Form or load the train/test sets
datasetBuilder.SplitTrainTest()


# Configurations file xml of the language model
configFileLanguageModel = ".\\LanguageModel\\Configurations\\Configurations.xml"
langModelLogFile = ".\\LanguageModel\\Output\\language_model.txt"
langModelTxtLoadFile = ".\\LanguageModel\\Output\\language_model_stocks_mix.txt"
stopWordsFileName = ".\\LanguageModel\\Input\\stop_words.txt"
# The serialization file to save the model
languageModelSerializationFile = ".\\LanguageModel\\Output\\language_model.bin"

# Start the LanguageModel:

# Initialize the LanguageModel
languageModel = LanguageModel(configFileLanguageModel, stopWordsFileName, languageModelSerializationFile, datasetBuilder.dataSet)
languageModel.BuildLanguageModel()
'''
# Extract relevant tweets only
relevantDataSet = []
irrelevantDataSet = []
for case in datasetBuilder.trainSet:
	if case['label'] == 'relevant':
		relevantDataSet.append(case)
	elif case['label'] == 'irrelevant':
		irrelevantDataSet.append(case)
		
# Initialize the LanguageModel
relLanguageModel = LanguageModel(configFileLanguageModel, stopWordsFileName, languageModelSerializationFile, relevantDataSet)
relLanguageModel.BuildLanguageModel()
	
irrelLanguageModel = LanguageModel(configFileLanguageModel, stopWordsFileName, languageModelSerializationFile, irrelevantDataSet)
irrelLanguageModel.BuildLanguageModel()		

# Merge the two models
languageModel = LanguageModel(configFileLanguageModel, stopWordsFileName, languageModelSerializationFile, datasetBuilder.dataSet)
mergedLanguageModel = {}
reqNumRel = 1000
reqNumIrrel = 1000

numRel = 0
numIrrel = 0

rel = {}
irrel = {}

for irrelKey, irrelFreq in irrelLanguageModel.languageModel.items():
	if not irrelKey in relLanguageModel.languageModel:
		if(numIrrel < reqNumIrrel):
			mergedLanguageModel[irrelKey] = irrelFreq
			numIrrel += 1

for relKey, relFreq in relLanguageModel.languageModel.items():
	if not relKey in irrelLanguageModel.languageModel:
		if(numRel < reqNumRel):
			mergedLanguageModel[relKey] = relFreq
			numRel += 1
		
		

languageModel.languageModel = OrderedDict(reversed(sorted(mergedLanguageModel.items(), key=lambda t:t[1])))
'''

# Configurations file xml of the features extractor
configFileFeaturesExtractor = ".\\FeaturesExtractor\\Configurations\\Configurations.xml"
# The serialization file to save the features
trainFeaturesSerializationFile = ".\\FeaturesExtractor\\Output\\train_features.bin"
trainLabelsSerializationFile = ".\\FeaturesExtractor\\Output\\train_labels.bin"
testFeaturesSerializationFile = ".\\FeaturesExtractor\\Output\\test_features.bin"
testLabelsSerializationFile = ".\\FeaturesExtractor\\Output\\test_labels.bin"
# Start the FeaturesExtractor:
#-----------------------------    
# Initialize the FeaturesExtractor
trainFeaturesExtractor = FeaturesExtractor(configFileFeaturesExtractor, trainFeaturesSerializationFile, trainLabelsSerializationFile, languageModel, datasetBuilder.trainSet)
trainFeaturesExtractor.ExtractFeatures()
trainFeaturesExtractor.SaveFeatures()
trainFeaturesExtractor.SaveLabels()

testFeaturesExtractor = FeaturesExtractor(configFileFeaturesExtractor, testFeaturesSerializationFile, testLabelsSerializationFile, languageModel, datasetBuilder.testSet)
testFeaturesExtractor.ExtractFeatures()
testFeaturesExtractor.SaveFeatures()
testFeaturesExtractor.SaveLabels()


# The serialization file to save the features
modelSerializationFile = ".\\Classifier\\Output\classifier_model.bin"

# Start the Classifier:
#---------------------

classifier = Classifier(modelSerializationFile, 'SVM', trainFeaturesExtractor.features, trainFeaturesExtractor.labels, testFeaturesExtractor.features, testFeaturesExtractor.labels)


# Train
classifier.Train()

# Test
labels, acc, val = classifier.Test()

# Build the confusion matrix
mConfusionMatrix, mNormalConfusionMatrix, vNumTrainExamplesPerClass, vAccuracyPerClass, nOverallAccuracy = classifier.BuildConfusionMatrix(testFeaturesExtractor.labels, labels)
print(mConfusionMatrix)

