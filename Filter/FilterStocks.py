'''
Created on Aug 6, 2014

@author: ASALLAB
'''
from DatasetBuilder.DatasetBuilder import DatasetBuilder
from LanguageModel.LanguageModel import LanguageModel   
from FeaturesExtractor.FeaturesExtractor import FeaturesExtractor
from Classifier.Classifier import Classifier
import os
from Filter.Stocks import stocks
import pickle


def file_exists(file_path):
    if not file_path:
        return False
    elif not os.path.isfile(file_path):
        return False
    else:
        return True


NVALID = 40
NMIN_SET = 50
class Filter(object):
    '''
    classdocs
    '''

    @classmethod
    def init(cls, save_path, use_backend=True, pre_stocks=None):
        '''
        Constructor
        :type self:
        '''
        global stocks
        if pre_stocks:
            stocks = pre_stocks

        for stock in stocks:
            print('Buildind model for %s' % stock)
            stock_model = {}
            # Start the DatasetBuilder
            #-------------------------
            # Configurations file xml of the dataset builder
            configFileDatasetBuilder = os.path.join('DatasetBuilder','Configurations','Configurations.xml')
                   
            # The serialization file to save the dataset
            datasetSerializationFile = os.path.join('DatasetBuilder','Output', 'dataset.bin')
                   
            # The XLSX file name for train set
            xlsxTrainFileName = os.path.join('DatasetBuilder','Input','train')
            
            
            # Initialize the DatasetBuilder from serialization file
            datasetBuilder = DatasetBuilder(configFileDatasetBuilder, [], datasetSerializationFile)
            if use_backend:
                datasetBuilder.trainSet = datasetBuilder.GetDatasetFromBackend(stock)
            else:
                datasetBuilder.trainSet = datasetBuilder.GetDatasetFromXLSXFile(xlsxTrainFileName, stock)
            if len(datasetBuilder.trainSet) < NMIN_SET:
                print("Not enough data: ", len(datasetBuilder.trainSet))
                continue
            datasetBuilder.trainSet = datasetBuilder.trainSet[NVALID:]
            # Configurations file xml of the language model
            configFileLanguageModel_lexicon = os.path.join('LanguageModel', 'Configurations', 'Configurations-Tasi.xml')
            stopWordsFileName = os.path.join('LanguageModel', 'Input', 'stop_words.txt')
            linksDBFile = os.path.join('LanguageModel', 'Output', 'links_database.txt')
            # The serialization file to save the model
            languageModelSerializationFile = os.path.join('LanguageModel', 'Output', 'language_model.bin')
            
            # Start the LanguageModel:
            
            # Initialize the LanguageModel_Lexicon
            stock_model['languageModel_lexicon'] = LanguageModel(configFileLanguageModel_lexicon, stopWordsFileName, languageModelSerializationFile, linksDBFile, datasetBuilder.trainSet)
            stock_model['languageModel_lexicon'].BuildLanguageModel()

            
            # Configurations file xml of the features extractor
            configFileFeaturesExtractor_Lexicon = os.path.join('FeaturesExtractor', 'Configurations', 'Configurations-Tasi.xml')
            # The serialization file to save the features
            trainFeaturesSerializationFile = os.path.join('FeaturesExtractor', 'Output', 'train_features.bin')
            trainLabelsSerializationFile = os.path.join('FeaturesExtractor', 'Output', 'train_labels.bin')
            
            # Start the FeaturesExtractor:
            #-----------------------------    
            # Initialize the FeaturesExtractor _ Lexicon
            trainFeaturesExtractor_Lexicon = FeaturesExtractor(configFileFeaturesExtractor_Lexicon, trainFeaturesSerializationFile, trainLabelsSerializationFile, stock_model['languageModel_lexicon'], datasetBuilder.trainSet)
            trainFeaturesExtractor_Lexicon.ExtractNumTfFeatures(sparse=True)
            #print(trainFeaturesExtractor_Lexicon.features[0])
            # The serialization file to save the features
            configFileClassifier_Lexicon = os.path.join('Classifier', 'Configurations', 'Configurations-Tasi.xml')
            modelSerializationFile = os.path.join('Classifier', 'Output', 'classifier_model.bin')
        
            # Start the Classifier:
            #---------------------
            stock_model['classifier_Lexicon'] = Classifier(configFileClassifier_Lexicon, modelSerializationFile,  trainFeaturesExtractor_Lexicon.sparse_features, trainFeaturesExtractor_Lexicon.labels, [], [])
            #stock_model['classifier_Lexicon'] = Classifier(configFileClassifier_Lexicon, modelSerializationFile,  trainFeaturesExtractor_Lexicon.features, trainFeaturesExtractor_Lexicon.labels, [], [])
            #print(trainFeaturesExtractor_Lexicon.labels[:4])
            #print([i['label'] for i in trainFeaturesExtractor_Lexicon.dataSet[:4]])
            # Train
            stock_model['classifier_Lexicon'].Train()
            stock_model['training_samples'] = len(datasetBuilder.trainSet)
            cls.save(save_path, stock, stock_model)
            
            print("----------------------------------------------------")

    @classmethod
    def save(cls, path, stockName, model):
        modelPath = os.path.join(path, str(stockName) + '.bin')
        pickle.dump(model, open(modelPath, 'wb'), protocol=pickle.HIGHEST_PROTOCOL)


    @classmethod
    def load(cls, path, stockName):
        modelPath = os.path.join(path, str(stockName) + '.bin')
        if not file_exists(modelPath):
            return None
        return pickle.load(open(modelPath, 'rb'))


    @classmethod
    def classify(cls, text, stockName, path):
        model = cls.load(path, stockName)
        if not model:
            return Exception('Stock wasn\'t found')
            
        testSet = []
        for t in text:
            testSet.append({'label' : '', 'text' : t})

        print('Using model for %s' % stockName)
        configFileFeaturesExtractor = os.path.join('FeaturesExtractor', 'Configurations', 'Configurations-Tasi.xml')
        testFeaturesExtractor = FeaturesExtractor(configFileFeaturesExtractor, None, None, model['languageModel_lexicon'], testSet)
        #testFeaturesExtractor.ExtractLexiconFeatures()
        testFeaturesExtractor.ExtractNumTfFeatures(sparse=True)
        model['classifier_Lexicon'].testFeatures = testFeaturesExtractor.sparse_features
        model['classifier_Lexicon'].testTargets = []
        for i in range(model['classifier_Lexicon'].testFeatures.shape[0]):      
            model['classifier_Lexicon'].testTargets.append(1)
        probs = model['classifier_Lexicon'].predict_propa()
        label = []
        for prob in probs:
            print(prob)
            prob = prob[0]
            if abs(prob[0] - prob[1]) < 0.2:
                label.append(0)
            elif max(prob) < 0.4:
                label.append(0)
            elif prob[0] > prob[1]:
                 label.append(1)
            elif prob[0] <= prob[1]:
                 label.append(2)
        return label
        

    @classmethod
    def evaluate(cls, path, use_backend=True, pre_stocks=None):
        validation_accuracy = {}
        global stocks
        if pre_stocks:
            stocks = pre_stocks

        for stockName in stocks:
            model = cls.load(path, stockName)
            if not model:
                continue

            configFileDatasetBuilder = os.path.join('DatasetBuilder','Configurations','Configurations.xml')
                   
            # The serialization file to save the dataset
            datasetSerializationFile = os.path.join('DatasetBuilder','Output', 'dataset.bin')
                   
            # The XLSX file name for train set
            xlsxTrainFileName = os.path.join('DatasetBuilder','Input','train')
            
            
            # Initialize the DatasetBuilder from serialization file
            datasetBuilder = DatasetBuilder(configFileDatasetBuilder, [], datasetSerializationFile)
            if use_backend:
                testSet = datasetBuilder.GetDatasetFromBackend(stockName)
            else:
                testSet = datasetBuilder.GetDatasetFromXLSXFile(xlsxTrainFileName, stockName)

            if len(testSet) < NMIN_SET:
                continue

            testSet = testSet[:NVALID]

            print('Using model for %s' % stockName)
            configFileFeaturesExtractor = os.path.join('FeaturesExtractor', 'Configurations', 'Configurations-Tasi.xml')
            testFeaturesExtractor = FeaturesExtractor(configFileFeaturesExtractor, None, None, model['languageModel_lexicon'], testSet)
            #testFeaturesExtractor.ExtractLexiconFeatures()
            testFeaturesExtractor.ExtractNumTfFeatures(sparse=True)
            model['classifier_Lexicon'].testFeatures = testFeaturesExtractor.sparse_features
            model['classifier_Lexicon'].testTargets = testFeaturesExtractor.labels
            label, acc, val = model['classifier_Lexicon'].Test()
            print(acc, val)
            validation_accuracy[stockName] = {'accuracy': acc, 'training_samples': model['training_samples']}
        return validation_accuracy
