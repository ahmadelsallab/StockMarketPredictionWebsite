'''
Created on Aug 6, 2014

@author: ASALLAB
'''
from DatasetBuilder.DatasetBuilder import DatasetBuilder
from LanguageModel.LanguageModel import LanguageModel   
from FeaturesExtractor.FeaturesExtractor import FeaturesExtractor
from Classifier.Classifier import Classifier

class Filter(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        # Start the DatasetBuilder
        #-------------------------
        # Configurations file xml of the dataset builder
        configFileDatasetBuilder = ".\\DatasetBuilder\\Configurations\\Configurations.xml"
               
        # The serialization file to save the dataset
        datasetSerializationFile = ".\\DatasetBuilder\\Output\\dataset.bin"
               
        # The XLSX file name for train set
        xlsxTrainFileName = ".\\DatasetBuilder\\Input\\train"
        
        
        # Initialize the DatasetBuilder from serialization file
        datasetBuilder = DatasetBuilder(configFileDatasetBuilder, [], datasetSerializationFile)
        
        datasetBuilder.trainSet = datasetBuilder.GetDatasetFromXLSXFile(xlsxTrainFileName)
                
        
        # Configurations file xml of the language model
        configFileLanguageModel = ".\\LanguageModel\\Configurations\\Configurations.xml"
        stopWordsFileName = ".\\LanguageModel\\Input\\stop_words.txt"
        linksDBFile = ".\\LanguageModel\\Output\\links_database.txt"
        # The serialization file to save the model
        languageModelSerializationFile = ".\\LanguageModel\\Output\\language_model.bin"
        
        # Start the LanguageModel:
        
        # Initialize the LanguageModel
        self.languageModel = LanguageModel(configFileLanguageModel, stopWordsFileName, languageModelSerializationFile, linksDBFile, datasetBuilder.trainSet)
        self.languageModel.BuildLanguageModel()
        
        # Configurations file xml of the features extractor
        configFileFeaturesExtractor = ".\\FeaturesExtractor\\Configurations\\Configurations.xml"
        # The serialization file to save the features
        trainFeaturesSerializationFile = ".\\FeaturesExtractor\\Output\\train_features.bin"
        trainLabelsSerializationFile = ".\\FeaturesExtractor\\Output\\train_labels.bin"
        
        # Start the FeaturesExtractor:
        #-----------------------------    
        # Initialize the FeaturesExtractor
        trainFeaturesExtractor = FeaturesExtractor(configFileFeaturesExtractor, trainFeaturesSerializationFile, trainLabelsSerializationFile, self.languageModel, datasetBuilder.trainSet)
        trainFeaturesExtractor.ExtractNumTfFeatures()       
        
        # The serialization file to save the features
        configFileClassifier = ".\\Classifier\\Configurations\\Configurations.xml"
        modelSerializationFile = ".\\Classifier\\Output\classifier_model.bin"
    
        # Start the Classifier:
        #---------------------
        
        self.classifier = Classifier(configFileClassifier, modelSerializationFile,  trainFeaturesExtractor.features, trainFeaturesExtractor.labels, [], [])
        
        
        # Train
        self.classifier.Train()
        
    def Classify(self, text):
        
        testSet = []
        testSet.append({'label' : '', 'text' : text})

        # Configurations file xml of the features extractor
        configFileFeaturesExtractor = ".\\FeaturesExtractor\\Configurations\\Configurations.xml"
        testFeaturesExtractor = FeaturesExtractor(configFileFeaturesExtractor, None, None, self.languageModel, testSet)
        testFeaturesExtractor.ExtractNumTfFeatures()
        
        self.classifier.testFeatures = testFeaturesExtractor.features
        self.classifier.testTargets = [1]
        
        
        label, acc, val = self.classifier.Test()
        
        return label
        