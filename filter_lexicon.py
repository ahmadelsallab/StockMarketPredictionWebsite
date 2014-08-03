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

# The XLSX file name for train set
xlsxTrainFileName = ".\\DatasetBuilder\\Input\\train"
xlsxTestFileName = ".\\DatasetBuilder\\Input\\test"


# Initialize the DatasetBuilder from serialization file
datasetBuilder = DatasetBuilder(configFileDatasetBuilder, [], datasetSerializationFile)


datasetBuilder.trainSet = datasetBuilder.GetDatasetFromXLSXFile(xlsxTrainFileName)
# Set the dataset to the train set so that the language model is built from train tweets only
datasetBuilder.dataSet  = datasetBuilder.GetDatasetFromXLSXFile(xlsxTrainFileName)
datasetBuilder.testSet  = datasetBuilder.GetDatasetFromXLSXFile(xlsxTestFileName)
#datasetBuilder.dataSet.extend(datasetBuilder.GetDatasetFromXLSXFile(xlsxTestFileName))
#datasetBuilder.trainSet.extend(datasetBuilder.GetDatasetFromXLSXFile(xlsxTestFileName))


# Configurations file xml of the language model
configFileLanguageModel = ".\\LanguageModel\\Configurations\\Configurations.xml"
langModelLogFile = ".\\LanguageModel\\Output\\language_model.txt"
langModelTxtLoadFile = ".\\LanguageModel\\Input\\language_model_lexicon.txt"
stopWordsFileName = ".\\LanguageModel\\Input\\stop_words.txt"
linksDBFile = ".\\LanguageModel\\Output\\links_database.txt"
# The serialization file to save the model
languageModelSerializationFile = ".\\LanguageModel\\Output\\language_model.bin"

# Start the LanguageModel:

# Initialize the LanguageModel
languageModel = LanguageModel(configFileLanguageModel, stopWordsFileName, languageModelSerializationFile, linksDBFile, datasetBuilder.trainSet)
languageModel.BuildLanguageModel()
languageModel.LoadModelFromTxtFile(langModelTxtLoadFile)

# Configurations file xml of the features extractor
configFileFeaturesExtractor = ".\\FeaturesExtractor\\Configurations\\Configurations.xml"
# The serialization file to save the features
trainFeaturesSerializationFile = ".\\FeaturesExtractor\\Output\\train_features.bin"
trainLabelsSerializationFile = ".\\FeaturesExtractor\\Output\\train_labels.bin"
testFeaturesSerializationFile = ".\\FeaturesExtractor\\Output\\test_features.bin"
testLabelsSerializationFile = ".\\FeaturesExtractor\\Output\\test_labels.bin"
testExportFileName = ".\\FeaturesExtractor\\Output\\test_data.txt"
trainExportFileName = ".\\FeaturesExtractor\\Output\\train_data.txt"

# Start the FeaturesExtractor:
#-----------------------------    
# Initialize the FeaturesExtractor
trainFeaturesExtractor = FeaturesExtractor(configFileFeaturesExtractor, trainFeaturesSerializationFile, trainLabelsSerializationFile, languageModel, datasetBuilder.trainSet)
#trainFeaturesExtractor.ExtractTFFeatures()
#trainFeaturesExtractor.ExtractNumTfFeatures()
#trainFeaturesExtractor.ExtractTFIDFFeatures()
#trainFeaturesExtractor.ExtractKLFeatures()
#trainFeaturesExtractor.SaveFeatures()
#trainFeaturesExtractor.SaveLabels()
#trainFeaturesExtractor.DumpFeaturesToTxt(trainExportFileName)

testFeaturesExtractor = FeaturesExtractor(configFileFeaturesExtractor, testFeaturesSerializationFile, testLabelsSerializationFile, languageModel, datasetBuilder.testSet)
#testFeaturesExtractor.ExtractTFFeatures()
#testFeaturesExtractor.ExtractTFIDFFeatures()
#testFeaturesExtractor.ExtractNumTfFeatures()
#testFeaturesExtractor.ExtractKLFeatures()
testFeaturesExtractor.ExtractLexiconFeatures()
#testFeaturesExtractor.SaveFeatures()
#testFeaturesExtractor.SaveLabels()
#testFeaturesExtractor.DumpFeaturesToTxt(testExportFileName)

# The serialization file to save the features
configFileClassifier = ".\\Classifier\\Configurations\\Configurations.xml"
modelSerializationFile = ".\\Classifier\\Output\classifier_model.bin"

# Start the Classifier:
#---------------------

classifier = Classifier(configFileClassifier, modelSerializationFile,  trainFeaturesExtractor.features, trainFeaturesExtractor.labels, testFeaturesExtractor.features, testFeaturesExtractor.labels)


# Train
#classifier.Train()

# Test
labels, acc, val = classifier.Test()

# Build the confusion matrix
mConfusionMatrix, mNormalConfusionMatrix, vNumTrainExamplesPerClass, vAccuracyPerClass, nOverallAccuracy = classifier.BuildConfusionMatrix(testFeaturesExtractor.labels, labels)
print(mConfusionMatrix)