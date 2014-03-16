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

DEBUG_LIMIT_IRRELEVANT_TRAIN_AND_TEST = False
# Flags to decide which action is required
#------------------------------------------
# Set if a crawler is required to run
CRAWLER = False

# Set if each stock to be crawled separately
CRAWLER_STOCK_BY_STOCK = True

# Set if a dataset is required to be built and labeled
DATASET_BUILDER = True

# Set if single stock to be tested per run
DATASET_BUILDER_SINGLE_STOCK_PER_TIME = False

# Set if dataset already exists and we just load it
LOAD_DATASET_FROM_SERIALIZATION_FILE = False
# The following flags are only valid in case of DATASET_BUILDER is True
# Set if a dumping is needed to csv file to update labels manually
DUMP_TO_MANUAL_CSV = False
DUMP_TO_MANUAL_XLSX = True
# Set to true if the loaded dataset is to be saved
DATASET_BUILDER_SAVE_DATASET = True
# Set if manual labels are ready and needs to be parsed
UPDATE_LABELS_FROM_CSV = False
UPDATE_LABELS_FROM_XLSX = False


# Set if spliting the dataset into train and test is required
SPLIT_DATASET_TRAIN_TEST = True
# Set if already test/train sets are available
LOAD_TRAIN_TEST = False # THIS IS NOT NEEDED WHILE 'LOAD_FEATURES' exists

# Set if language model is required to be built
LANGUAGE_MODEL = False
# The following flags are only valid in case of LANGUAGE_MODEL is True
LOAD_LANGUAGE_MODEL = False
#Set if you want to include uni-gram
MERGE_UNI_GRAM = True
#Set if you want to include bi-gram
MERGE_BI_GRAM = False
#Set if you want to include tri-gram
MERGE_TRI_GRAM = False

# Set if features extraction is desired for the dataset
FEATURES_EXTRACTION = False
# The following flags are only valid in case of FEATURES_EXTRACTION is True
LOAD_FEATURES = False
LOAD_LABELS = False

# Set to true if Classifier is required to run
CLASSIFIER = False

# The following flags are only valid in case of CLASSIFIER is True
SVM_CLASSIFIER = True
LOAD_MODEL = False
# Set if query classifier is needed
CLASSIFIER_TWO_STAGE_FILTER_BY_QUERY_RELEVANCE = True

# A COLLECTIVE FLAG TO USE EXISTING MODEL TO REPLICATE PREVIOUS RESULT: Same svmModel, train and test features and labels
FREEZE_RESULTS = False
if(FREEZE_RESULTS):
    LOAD_FEATURES = True
    LOAD_LABELS = True
    LOAD_MODEL = True

f_in = open('.\\TwitterCrawler\\stocks.txt', 'r', encoding='utf-8')
lines = f_in.readlines()
for line in lines:            
    stock = line.strip()
    #print(stock+"\n")
        
    # General settings:
    #------------------
    
    # Serialization binary file name
    serializatoinFileName = ".\\TwitterCrawler\\Output\\results_" + stock + ".bin"
    if(CRAWLER):
        
        # Crawl for irrel.
        #----------------
        # Configurations file xml of the crawler
        configFileCrawler = ".\\TwitterCrawler\\Configurations\\Configurations_Stock_By_Stock.xml"
        
        # Feeds file log
        feedsLogFile = ".\\TwitterCrawler\\Output\\feeds_" + stock + ".xml"
        
        # Update rate log file
        updateRateLogFile = ".\\TwitterCrawler\\Output\\update_rate_log_" + stock + "_irrel.log"
        
        # Start the TwitterCrawler
        #-------------------------
        twitterCrawler = TwitterCrawler(configFileCrawler, feedsLogFile, updateRateLogFile, serializatoinFileName)
        
        # The query array is just the current stock
        twitterCrawler.queryArray = []
        twitterCrawler.queryArray.append(stock)
        
        # Start crawling
        twitterCrawler.Crawl('')
    
    
    if(DATASET_BUILDER):
        # Start the DatasetBuilder
        #-------------------------
        # Configurations file xml of the dataset builder
        configFileDatasetBuilder = ".\\DatasetBuilder\\Configurations\\Configurations.xml"
        
        # The CSV file name for tweets to be manually labeled
        xlsxManualLabelsFileName = ".\\DatasetBuilder\\Output\\ManualLabels_" + stock
    
        # The CSV file name for tweets to be manually labeled
        csvManualLabelsFileName = ".\\DatasetBuilder\\Output\\ManualLabels_" + stock 
    
        # The serialization file to save the dataset
        datasetSerializationFile = ".\\DatasetBuilder\\Output\\dataset_" + stock +".bin"
        
        # Train/Test serialization file
        trainTestSerializationFile = ".\\DatasetBuilder\\Output\\train_test_dataset_" + stock + ".bin"
        
        # Load queryArray
        if(DATASET_BUILDER_SINGLE_STOCK_PER_TIME):
            f_in = open('.\\TwitterCrawler\\stocks.txt', 'r', encoding='utf-8')
            lines = f_in.readlines()
            queryArray = []
            stock_under_test = 4
            i = 1
            for line in lines:
                if(i == stock_under_test):
                    queryArray.append(line.strip())
                    print(line.strip()+"\n")
                    break
                i += 1
    
    
        # Check if the current stage is to initialize random labels
        if LOAD_DATASET_FROM_SERIALIZATION_FILE:
            # Initialize the DatasetBuilder from serialization file
            datasetBuilder = DatasetBuilder(configFileDatasetBuilder, [], datasetSerializationFile)
            
            # Load the dataset
            datasetBuilder.LoadDataset()  
            
            # Form or load the train/test sets
            if SPLIT_DATASET_TRAIN_TEST:
                datasetBuilder.SplitTrainTest()
                datasetBuilder.SaveTrainTestDataset(trainTestSerializationFile)
            elif LOAD_TRAIN_TEST:
                datasetBuilder.LoadTrainTestDataset(trainTestSerializationFile)      
            
        elif UPDATE_LABELS_FROM_CSV:
            # Initialize the DatasetBuilder from serialization file
            datasetBuilder = DatasetBuilder(configFileDatasetBuilder, [], datasetSerializationFile)
            
            # Load the dataset
            datasetBuilder.LoadDataset()
            
            # Update the labels
            numFiles = 48
            for i in range(numFiles):
                datasetBuilder.UpdateManualLabelsFromCSVFile(csvManualLabelsFileName + "_" + str(i + 1)) # This should be done separately when dataset is manually labeled
            
            # Form or load the train/test sets
            if SPLIT_DATASET_TRAIN_TEST:
                datasetBuilder.SplitTrainTest()
                datasetBuilder.SaveTrainTestDataset(trainTestSerializationFile)
            elif LOAD_TRAIN_TEST:
                datasetBuilder.LoadTrainTestDataset(trainTestSerializationFile) 
        elif UPDATE_LABELS_FROM_XLSX:
            # Initialize the DatasetBuilder from serialization file
            datasetBuilder = DatasetBuilder(configFileDatasetBuilder, [], datasetSerializationFile)
            
            # Load the dataset
            #datasetBuilder.LoadDataset()
            
            # Update the labels
            numFiles = 50
            for i in range(numFiles):
                print('Updating labels from file ' + xlsxManualLabelsFileName  + "_" + str(i + 1) + '...')
                if(CLASSIFIER_TWO_STAGE_FILTER_BY_QUERY_RELEVANCE):
                    datasetBuilder.UpdateManualLabelsFromXLSXFileFilterByQuery(xlsxManualLabelsFileName  + "_" + str(i + 1), (i + 1), queryArray)
                else:
                    datasetBuilder.UpdateManualLabelsFromXLSXFile(xlsxManualLabelsFileName  + "_" + str(i + 1), (i + 1)) # This should be done separately when dataset is manually labeled
            
            #print('Number of irrelevant examples: ' + str(datasetBuilder.irrelevantNum) + '\n')
            # Save to binary file for later labeling
            if DATASET_BUILDER_SAVE_DATASET:
                datasetBuilder.SaveDataset()
            
            # Form or load the train/test sets
            if SPLIT_DATASET_TRAIN_TEST:
                datasetBuilder.SplitTrainTest()
                datasetBuilder.SaveTrainTestDataset(trainTestSerializationFile)
            elif LOAD_TRAIN_TEST:
                datasetBuilder.LoadTrainTestDataset(trainTestSerializationFile) 
    
        else:                
            serializatoinFile = open(serializatoinFileName, 'rb')
            rawData = []
            rawData.append(pickle.load(serializatoinFile))            # Form the labels of each dataset
            
            label = []
            label.append('irrelevant')
            
            
            # Form the list to be passed to the dataset builder
            rawDataList = []
            
            rawDataList.append({'label':label[0], 'rawData':rawData[0]})
            
            
            # Initialize the DatasetBuilder
            datasetBuilder = DatasetBuilder(configFileDatasetBuilder, rawDataList, datasetSerializationFile)
            datasetBuilder.BuildDataset()
            
            if SPLIT_DATASET_TRAIN_TEST:
                datasetBuilder.SplitTrainTest()
    
            # Save to binary file for later labeling
            datasetBuilder.SaveDataset()
            
            # Dump to csv initial random labels depending on twitter crawling
            if(DUMP_TO_MANUAL_CSV):
                datasetBuilder.DumpDatasetToCSV(csvManualLabelsFileName)
            elif(DUMP_TO_MANUAL_XLSX):
                datasetBuilder.DumpDatasetToXLSX(xlsxManualLabelsFileName)
            
            # Form or load the train/test sets
            if SPLIT_DATASET_TRAIN_TEST:
                datasetBuilder.SplitTrainTest()
                datasetBuilder.SaveTrainTestDataset(trainTestSerializationFile)
            elif LOAD_TRAIN_TEST:
                datasetBuilder.LoadTrainTestDataset(trainTestSerializationFile) 
    
            
    if(LANGUAGE_MODEL):
        
        # Configurations file xml of the language model
        configFileLanguageModel = ".\\LanguageModel\\Configurations\\Configurations.xml"
        langModelLogFile = ".\\LanguageModel\\Output\\language_model_" + stock + ".txt"
        stopWordsFileName = ".\\LanguageModel\\Input\\stop_words.txt"
        # The serialization file to save the model
        languageModelSerializationFile = ".\\LanguageModel\\Output\\language_model_" + stock + ".bin"
    
        # Start the LanguageModel:
        #-------------------------    
        if not LOAD_LANGUAGE_MODEL:
            # Initialize the LanguageModel
            languageModel = LanguageModel(configFileLanguageModel, stopWordsFileName, languageModelSerializationFile, datasetBuilder.dataSet)
            languageModel.BuildLanguageModel()
            if MERGE_BI_GRAM:
                languageModel.NGram = 2
                languageModel.BuildLanguageModel()
            if MERGE_TRI_GRAM:
                languageModel.NGram = 3
                languageModel.BuildLanguageModel()
    
            languageModel.DumpLanguageModel(langModelLogFile)
            languageModel.SaveModel()
        else:
            # Load the LanguageModel
            languageModel = LanguageModel(configFileLanguageModel, stopWordsFileName, languageModelSerializationFile, datasetBuilder.dataSet)
            languageModel.LoadModel()
    
    if(FEATURES_EXTRACTION):
        # Configurations file xml of the features extractor
        configFileFeaturesExtractor = ".\\FeaturesExtractor\\Configurations\\Configurations.xml"
        # The serialization file to save the features
        trainFeaturesSerializationFile = ".\\FeaturesExtractor\\Output\\train_features_" + stock +".bin"
        trainLabelsSerializationFile = ".\\FeaturesExtractor\\Output\\train_labels_" + stock + ".bin"
        testFeaturesSerializationFile = ".\\FeaturesExtractor\\Output\\test_features_" + stock + ".bin"
        testLabelsSerializationFile = ".\\FeaturesExtractor\\Output\\test_labels_" + stock + ".bin"
        # Start the FeaturesExtractor:
        #-----------------------------    
        if not LOAD_FEATURES:
            # Initialize the FeaturesExtractor
            trainFeaturesExtractor = FeaturesExtractor(configFileFeaturesExtractor, trainFeaturesSerializationFile, trainLabelsSerializationFile, languageModel, datasetBuilder.trainSet)
            trainFeaturesExtractor.ExtractFeatures()
            trainFeaturesExtractor.SaveFeatures()
            trainFeaturesExtractor.SaveLabels()
    
            testFeaturesExtractor = FeaturesExtractor(configFileFeaturesExtractor, testFeaturesSerializationFile, testLabelsSerializationFile, languageModel, datasetBuilder.testSet)
            testFeaturesExtractor.ExtractFeatures()
            testFeaturesExtractor.SaveFeatures()
            testFeaturesExtractor.SaveLabels()
    
        else:
            # Initialize the FeaturesExtractor
            trainFeaturesExtractor = FeaturesExtractor(configFileFeaturesExtractor, trainFeaturesSerializationFile, trainLabelsSerializationFile, languageModel, datasetBuilder.trainSet)
            trainFeaturesExtractor.LoadFeatures()
            if LOAD_LABELS:
                trainFeaturesExtractor.LoadLabels()
    
            testFeaturesExtractor = FeaturesExtractor(configFileFeaturesExtractor, testFeaturesSerializationFile, testLabelsSerializationFile, languageModel, datasetBuilder.testSet)
            testFeaturesExtractor.LoadFeatures()
            if LOAD_LABELS:
                testFeaturesExtractor.LoadLabels()
    
    if(CLASSIFIER):
        # The serialization file to save the features
        modelSerializationFile = ".\\Classifier\\Output\classifier_model_" + stock + ".bin"
        
        # Start the Classifier:
        #---------------------
        if(SVM_CLASSIFIER):
            classifier = Classifier(modelSerializationFile, 'SVM', trainFeaturesExtractor.features, trainFeaturesExtractor.labels, testFeaturesExtractor.features, testFeaturesExtractor.labels)
            
            if not LOAD_MODEL:
                # Train
                classifier.Train()
                classifier.SaveModel()
            else:
                classifier.LoadModel()
            # Test
            labels, acc, val = classifier.Test()
        
    
            # Build the confusion matrix
            mConfusionMatrix, mNormalConfusionMatrix, vNumTrainExamplesPerClass, vAccuracyPerClass, nOverallAccuracy = classifier.BuildConfusionMatrix(testFeaturesExtractor.labels, labels)
            print(mConfusionMatrix)
        
f_in.close()