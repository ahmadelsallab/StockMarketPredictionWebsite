# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 02:25:48 2014

@author: Tarek
"""


from DatasetBuilder.DatasetBuilder import DatasetBuilder
from LanguageModel.LanguageModel import LanguageModel
from FeaturesExtractor.FeaturesExtractor import FeaturesExtractor
from Classifier.Classifier import Classifier
import pickle
from collections import OrderedDict

class filter(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        '''
        # Configurations file xml of the dataset builder
        configFileDatasetBuilder = ".\\DatasetBuilder\\Configurations\\Configurations.xml"
        # The serialization file to save the dataset
        datasetSerializationFile = ".\\DatasetBuilder\\Output\\dataset.bin"
        datasetBuilder = DatasetBuilder(configFileDatasetBuilder, [], datasetSerializationFile)
        datasetBuilder.LoadDataset()
        '''
        # Configurations file xml of the language model
        configFileLanguageModel = ".\\LanguageModel\\Configurations\\Configurations.xml"
        langModelLogFile = ".\\LanguageModel\\Output\\language_model.txt"
        langModelTxtLoadFile = ".\\LanguageModel\\Output\\language_model_stocks_mix.txt"
        stopWordsFileName = ".\\LanguageModel\\Input\\stop_words.txt"
        linksDBFile = ".\\LanguageModel\\Output\\links_database.txt"
        # The serialization file to save the model
        languageModelSerializationFile = ".\\LanguageModel\\Output\\language_model.bin"

        # Start the LanguageModel:

        # Initialize the LanguageModel
        self.languageModel = LanguageModel(configFileLanguageModel, stopWordsFileName, languageModelSerializationFile, linksDBFile, [])
        self.languageModel.LoadModel()

    def filter(self, TweetText):
        # Configurations file xml of the features extractor
        configFileFeaturesExtractor = ".\\FeaturesExtractor\\Configurations\\Configurations.xml"
        # The serialization file to save the features
        testFeaturesSerializationFile = ".\\FeaturesExtractor\\Output\\test_features.bin"
        testLabelsSerializationFile = ".\\FeaturesExtractor\\Output\\test_labels.bin"
        testExportFileName = ".\\FeaturesExtractor\\Output\\test_data.txt"

        dataset=[]
        dataset.append(TweetText)
        testFeaturesExtractor = FeaturesExtractor(configFileFeaturesExtractor, testFeaturesSerializationFile, testLabelsSerializationFile, self.languageModel, dataset)
        testFeaturesExtractor.ExtractTFFeatures()
        #testFeaturesExtractor.ExtractTFIDFFeatures()
        #testFeaturesExtractor.ExtractNumTfFeatures()
        #testFeaturesExtractor.ExtractKLFeatures()
        testFeaturesExtractor.SaveFeatures()
        testFeaturesExtractor.SaveLabels()
        testFeaturesExtractor.DumpFeaturesToTxt(testExportFileName)

        # The serialization file to save the features
        configFileClassifier = ".\\Classifier\\Configurations\\Configurations.xml"
        modelSerializationFile = ".\\Classifier\\Output\classifier_model.bin"

        # Start the Classifier:
        #---------------------

        classifier = Classifier(configFileClassifier, modelSerializationFile,  None, None, testFeaturesExtractor.features, testFeaturesExtractor.labels)


        # Test
        classifier.LoadModel()
        labels, acc, val = classifier.Test()

        return labels