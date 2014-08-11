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


# Flags to decide which action is required
#------------------------------------------
# Set if a crawler is required to run
CRAWLER = False

# Set if a dataset is required to be built and labeled
DATASET_BUILDER = True
# The following flags are only valid in case of DATASET_BUILDER is True
# Set if a dumping is needed to csv file to update labels manually
DUMP_TO_MANUAL_CSV = False
DUMP_TO_MANUAL_XLSX = True

# Set if manual labels are ready and needs to be parsed
UPDATE_LABELS_FROM_CSV = False

# Set if dataset already exists and we just load it
LOAD_DATASET_FROM_SERIALIZATION_FILE = True

# Set if spliting the dataset into train and test is required
SPLIT_DATASET_TRAIN_TEST = True
# Set if already test/train sets are available
LOAD_TRAIN_TEST = False # THIS IS NOT NEEDED WHILE 'LOAD_FEATURES' exists

# Set if language model is required to be built
LANGUAGE_MODEL = True
# The following flags are only valid in case of LANGUAGE_MODEL is True
LOAD_LANGUAGE_MODEL = False
#Set if you want to include uni-gram
MERGE_UNI_GRAM = True
#Set if you want to include bi-gram
MERGE_BI_GRAM = False
#Set if you want to include tri-gram
MERGE_TRI_GRAM = False

# Set if features extraction is desired for the dataset
FEATURES_EXTRACTION = True
# The following flags are only valid in case of FEATURES_EXTRACTION is True
LOAD_FEATURES = False
LOAD_LABELS = False
DUMP_FEATURES = False

# Set to true if Classifier is required to run
CLASSIFIER = True

# The following flags are only valid in case of CLASSIFIER is True
SVM_CLASSIFIER = True
LOAD_MODEL = False

# A COLLECTIVE FLAG TO USE EXISTING MODEL TO REPLICATE PREVIOUS RESULT: Same svmModel, train and test features and labels
FREEZE_RESULTS = False
if(FREEZE_RESULTS):
    LOAD_FEATURES = True
    LOAD_LABELS = True
    LOAD_MODEL = True
    
# General settings:
#------------------

# Serialization binary file name
serializatoinFileNameIrrel = ".\\TwitterCrawler\\Output\\results_irrel.bin"
serializatoinFileNameRel = ".\\TwitterCrawler\\Output\\results_rel.bin"
if(CRAWLER):
    
    # Crawl for irrel.
    #----------------
    # Configurations file xml of the crawler
    configFileCrawler = ".\\TwitterCrawler\\Configurations\\Configurations_Irrel.xml"
    
    # Feeds file log
    feedsLogFile = ".\\TwitterCrawler\\Output\\feeds_irrel.xml"
    
    # Update rate log file
    updateRateLogFile = ".\\TwitterCrawler\\Output\\update_rate_log_irrel.log"
    
    # Start the TwitterCrawler
    #-------------------------
    twitterCrawler = TwitterCrawler(configFileCrawler, feedsLogFile, updateRateLogFile, serializatoinFileNameIrrel)
    
    # Start crawling
    #twitterCrawler.Crawl('')

    # Crawl for rel
    #--------------
    
    # Configurations file xml of the crawler
    configFileCrawler = ".\\TwitterCrawler\\Configurations\\Configurations_Rel.xml"
    
    # Feeds file log
    feedsLogFile = ".\\TwitterCrawler\\Output\\feeds_rel.xml"
    
    # Update rate log file
    updateRateLogFile = ".\\TwitterCrawler\\Output\\update_rate_log_rel.log"
    
    # Start the TwitterCrawler
    #-------------------------
    twitterCrawler = TwitterCrawler(configFileCrawler, feedsLogFile, updateRateLogFile, serializatoinFileNameRel)
    
    # Start crawling
    twitterCrawler.Crawl('')


if(DATASET_BUILDER):
    # Start the DatasetBuilder
    #-------------------------
    # Configurations file xml of the dataset builder
    configFileDatasetBuilder = ".\\DatasetBuilder\\Configurations\\Configurations.xml"
    
    # The CSV file name for tweets to be manually labeled
    csvManualLabelsFileName = ".\\DatasetBuilder\\Output\\ManualLabels"
    xlsxManualLabelsFileName = ".\\DatasetBuilder\\Output\\ManualLabels"

    # The serialization file to save the dataset
    datasetSerializationFile = ".\\DatasetBuilder\\Output\\dataset.bin"
    
    # Train/Test serialization file
    trainTestSerializationFile = ".\\DatasetBuilder\\Output\\train_test_dataset.bin"

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
        datasetBuilder.UpdateManualLabelsFromCSV() # This should be done separately when dataset is manually labeled
        
        # Form or load the train/test sets
        if SPLIT_DATASET_TRAIN_TEST:
            datasetBuilder.SplitTrainTest()
            datasetBuilder.SaveTrainTestDataset(trainTestSerializationFile)
        elif LOAD_TRAIN_TEST:
            datasetBuilder.LoadTrainTestDataset(trainTestSerializationFile) 

    else:                
        # Load the serialization file
        serializatoinFileIrrel = open(serializatoinFileNameIrrel, 'rb')
        serializatoinFileRel = open(serializatoinFileNameRel, 'rb')
        rawData = []
        rawData.append(pickle.load(serializatoinFileIrrel))
        rawData.append(pickle.load(serializatoinFileRel))
        
        # Form the labels of each dataset
        label = []
        label.append('irrelevant')
        label.append('relevant')
        
        # Form the list to be passed to the dataset builder
        rawDataList = []
        for i in range(2):
            rawDataList.append({'label':label[i], 'rawData':rawData[i]})
        
        
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
    langModelLogFile = ".\\LanguageModel\\Output\\language_model.txt"
    stopWordsFileName = ".\\LanguageModel\\Input\\stop_words.txt"
    # The serialization file to save the model
    languageModelSerializationFile = ".\\LanguageModel\\Output\\language_model.bin"

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
    trainFeaturesSerializationFile = ".\\FeaturesExtractor\\Output\\train_features.bin"
    trainLabelsSerializationFile = ".\\FeaturesExtractor\\Output\\train_labels.bin"
    testFeaturesSerializationFile = ".\\FeaturesExtractor\\Output\\test_features.bin"
    testLabelsSerializationFile = ".\\FeaturesExtractor\\Output\\test_labels.bin"
    testExportFileName = ".\\FeaturesExtractor\\Output\\test_data.txt"
    trainExportFileName = ".\\FeaturesExtractor\\Output\\train_data.txt"
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

    if DUMP_FEATURES:
        trainFeaturesExtractor.DumpFeaturesToTxt(trainExportFileName)
        testFeaturesExtractor.DumpFeaturesToTxt(testExportFileName)
if(CLASSIFIER):
    # The serialization file to save the features
    modelSerializationFile = ".\\Classifier\\Output\classifier_model.bin"
    
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
    
    