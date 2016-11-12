'''
Created on Aug 6, 2014

@author: ASALLAB
'''
from DatasetBuilder.DatasetBuilder import DatasetBuilder
from LanguageModel.LanguageModel import LanguageModel   
from FeaturesExtractor.FeaturesExtractor import FeaturesExtractor
from Classifier.Classifier import Classifier
import os
import pickle

class Filter(object):
    '''
    classdocs
    '''


    def __init__(self, basePath, stockName , Retrain):
        '''
        Constructor
        :type self:
        '''
        
        if(basePath == None):
            self.basePath = self.basePath
        else:
            self.basePath = basePath
            
        self.stockName = stockName    
        serializationFile = open(os.path.join(self.basePath,'StockToClassifier.bin'),'rb')
        self.StockToClassifier = pickle.load(serializationFile) 
        #import pdb; pdb.set_trace()   
        self.usedClassifier = self.StockToClassifier[self.stockName]
        # Start the DatasetBuilder
        #-------------------------
        # Configurations file xml of the dataset builder
        configFileDatasetBuilder = os.path.join(self.basePath, "DatasetBuilder", "Configurations", "Configurations.xml")
               
        # The serialization file to save the dataset
        datasetSerializationFile = os.path.join(self.basePath, "DatasetBuilder", "Output", "dataset.bin")
        
        if Retrain == False:       
            # The XLSX file name for train set
            xlsxTrainFileName = os.path.join(self.basePath, "DatasetBuilder" ,"Input", "train")
        
        
            # Initialize the DatasetBuilder from serialization file
            datasetBuilder = DatasetBuilder(configFileDatasetBuilder, [], datasetSerializationFile)
        
         
            datasetBuilder.trainSet = datasetBuilder.GetDatasetFromXLSXFile(xlsxTrainFileName)
                    
        

            self.RunLanguageModel(self.usedClassifier,datasetBuilder.trainSet)
        
        
        
            trainFeaturesExtractor = self.RunFeatureExtractor(self.usedClassifier,datasetBuilder.trainSet)
            self.Train(self.usedClassifier,trainFeaturesExtractor,True)
        else:
            # Initialize the DatasetBuilder from serialization file
            datasetBuilder = DatasetBuilder(configFileDatasetBuilder, [], datasetSerializationFile)
        
    def Classify(self, text):
    
        testSet = []
        for t in text:
            testSet.append({'label' : '', 'text' : t})


        # Configurations file xml of the features extractor
        configFileFeaturesExtractor = os.path.join(self.basePath, "FeaturesExtractor", "Configurations", "Configurations-"+self.usedClassifier+".xml")
        testFeaturesExtractor = FeaturesExtractor(configFileFeaturesExtractor, None, None, self.languageModel, testSet)
        if self.usedClassifier == "Lexicon":
            testFeaturesExtractor.ExtractLexiconFeatures()
        else:
            testFeaturesExtractor.ExtractNumTfFeatures()
        self.classifier.testFeatures = testFeaturesExtractor.features
        self.classifier.testTargets = []
        for i in range(len(self.classifier.testFeatures)):        
            self.classifier.testTargets.append(1)
        label, acc, val = self.classifier.Test()

        
        return label

        
    def RunLanguageModel(self,_Classifier,trainSet):
        # Configurations file xml of the language model
        configFileLanguageModel = os.path.join(self.basePath, "LanguageModel", "Configurations", "Configurations-"+_Classifier+".xml")
        stopWordsFileName = os.path.join(self.basePath, "LanguageModel", "Input", "stop_words.txt")
        linksDBFile = os.path.join(self.basePath, "LanguageModel", "Output", "links_database.txt")
        # The serialization file to save the model
        languageModelSerializationFile = os.path.join(self.basePath, "LanguageModel" ,"Output" ,"language_model.bin")
        if _Classifier == "Lexicon":
            langModelTxtLoadFile = os.path.join(self.basePath, "LanguageModel", "Input", "language_model_lexicon_synonyms.txt")
        
        # Start the LanguageModel:
        
        # Initialize the LanguageModel_Lexicon
        self.languageModel = LanguageModel(configFileLanguageModel, stopWordsFileName, languageModelSerializationFile, linksDBFile, trainSet)
        self.languageModel.BuildLanguageModel()
        if _Classifier == "Lexicon":
            self.languageModel.LoadModelFromTxtFile(langModelTxtLoadFile)   
                 
    def RunFeatureExtractor(self,_Classifier,trainSet):        
        # Configurations file xml of the features extractor
        configFileFeaturesExtractor = os.path.join(self.basePath, "FeaturesExtractor", "Configurations", "Configurations-"+_Classifier+".xml")
        # The serialization file to save the features
        trainFeaturesSerializationFile = os.path.join(self.basePath, "FeaturesExtractor", "Output", "train_features.bin")
        trainLabelsSerializationFile = os.path.join(self.basePath, "FeaturesExtractor", "Output", "train_labels.bin")
        
        # Start the FeaturesExtractor:
        #-----------------------------    
        # Initialize the FeaturesExtractor 
        trainFeaturesExtractor = FeaturesExtractor(configFileFeaturesExtractor, trainFeaturesSerializationFile, trainLabelsSerializationFile, self.languageModel, trainSet)
        if _Classifier == "Lexicon":
            trainFeaturesExtractor.ExtractLexiconFeatures()
        else:
            trainFeaturesExtractor.ExtractNumTfFeatures()
        return trainFeaturesExtractor
            
    def Train(self,_Classifier,trainFeaturesExtractor,Full):        
        # The serialization file to save the features
        configFileClassifier = os.path.join(self.basePath, "Classifier", "Configurations", "Configurations-"+_Classifier+".xml")
        modelSerializationFile = os.path.join(self.basePath, "Classifier", "Output", "classifier_model.bin")
    
        # Start the Classifier:
        #---------------------
        
        self.classifier = Classifier(configFileClassifier, modelSerializationFile,  trainFeaturesExtractor.features, trainFeaturesExtractor.labels, [], [])
        
        if Full == True:
            self.classifier.Train()
        
    def GetBestClassifier(self,trainSet):
        #import pdb; pdb.set_trace()
        self.RunLanguageModel("Lexicon",trainSet)
        trainFeaturesExtractor=self.RunFeatureExtractor("Lexicon",trainSet)
        self.Train("Lexicon",trainFeaturesExtractor,False)
        LexiconAcc=self.classifier.getCrossValidationAccuarcy()
        
        self.RunLanguageModel("DT",trainSet)
        trainFeaturesExtractor = self.RunFeatureExtractor("DT",trainSet)
        self.Train("DT",trainFeaturesExtractor,False)
        DTAcc=self.classifier.getCrossValidationAccuarcy()
        
        self.RunLanguageModel("SVM",trainSet)
        trainFeaturesExtractor=self.RunFeatureExtractor("SVM",trainSet)
        self.Train("SVM",trainFeaturesExtractor,False)
        SVMAcc=self.classifier.getCrossValidationAccuarcy()
        bestClassifier = max(LexiconAcc,DTAcc,SVMAcc)
        if bestClassifier== LexiconAcc:
            self.StockToClassifier[self.stockName]="Lexicon"
        elif bestClassifier == DTAcc:
            self.StockToClassifier[self.stockName]="DT"
        else:
            self.StockToClassifier[self.stockName]="SVM"
#        serializationFile = open('./StockToClassifier.bin', 'wb')
#        pickle.dump(self.StockToClassifier, serializationFile)
