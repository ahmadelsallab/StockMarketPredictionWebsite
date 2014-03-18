'''
Created on Nov 7, 2013

@author: ASALLAB
'''
from xml.dom import minidom
from LanguageModel.LanguageModel import *
import pickle
import numpy
import math
DEBUG_LIMIT_IRRELEVANT_TRAIN_AND_TEST = False
class FeaturesExtractor(object):
    '''
    classdocs
    '''

    # Initialize empty list of features corresponding to each item of a dataset
    features = []
    labels = []

    # Map table to map the language model into index
    featuresNamesMap = {}
    labelsNamesMap = {}
    #featuresMapExist = False
        
    def __init__(self, configFileName, featuresSerializationFileName, labelsSerializationFileName, languageModel, dataSet):
        '''
        Constructor
        '''
        # Parse the configurations file
        self.ParseConfigFile(configFileName)
        
        
        # Store the language model
        self.languageModel = languageModel
        
        # Only re-fill the language model with first N entries unless the desired features vector length is "Full"
        if(self.featuresVectorLength != "Full"): 
            tempLanguageModel = {}
            length = 0
            for text in self.languageModel.languageModel:
                if(length <= int(self.featuresVectorLength) - 1):             
                    tempLanguageModel[text] = self.languageModel.languageModel[text]
                length += 1  
            self.languageModel.languageModel = tempLanguageModel
        
        # Construct the map from language model term into index
        '''
        if not self.featuresMapExist:
            self.featuresMapExist = True
            featureIdx = 1
            if(self.libSVMFormat == 'true'):
                for term in self.languageModel.languageModel:
                    self.featuresNamesMap[term] = featureIdx
                    featureIdx += 1
        '''    
        featureIdx = 1
        if(self.libSVMFormat == 'true'):
            for term in self.languageModel.languageModel:
                self.featuresNamesMap[term] = featureIdx
                featureIdx += 1
                
        # Store the dataset
        self.dataSet = dataSet
        
        # Store the serialization file
        self.featuresSerializationFileName = featuresSerializationFileName
        self.labelsSerializationFileName = labelsSerializationFileName 
        
        # Initialize empty list of features corresponding to each item of a dataset
        self.features = []
        self.labels = []

    def ExtractTFFeatures(self):
        
        # Loop on the dataset items
        irrelevantNum = 0
        for item in self.dataSet:
            if(not (item['text'] is None) and not(item['label'] is None)):
                # Initialize the items dictionary. It's sparse dictionary, with only words in the language model that exist in the item.
                itemFeatures = {}
                # Initialize the features vector
                
                for term in self.languageModel.languageModel:
                    if(self.libSVMFormat == 'true'):
                        itemFeatures[self.featuresNamesMap[term]] = 0
                    else:
                        itemFeatures[term] = 0
                    
                # Form the list of language model terms
                terms = self.languageModel.SplitIntoTerms(item['text'])
                
                # Extract features for the item based on its terms
                for term in terms:
                    
                    # If the term exist in the language model
                    if term in self.languageModel.languageModel:
                        
                        # Add the feature if not exists or increment it if exists
                        try:
                            if(self.libSVMFormat == 'true'):
                                itemFeatures[self.featuresNamesMap[term]] = 1
                            else:
                                itemFeatures[term] = 1
                        except:
                            if(self.libSVMFormat == 'true'):
                                if self.featureFormat != 'Binary':
                                    itemFeatures[self.featuresNamesMap[term]] += 1
                            else:
                                if self.featureFormat != 'Binary':
                                    itemFeatures[term] += 1
                        
                        # Normalize the feature
                        if(self.libSVMFormat == 'true'):
                            if self.featureFormat == 'Normal':
                                itemFeatures[self.featuresNamesMap[term]] /= terms.__len__()                                                      
                        else:                        
                            if self.featureFormat == 'Normal':
                                itemFeatures[term] /= terms.__len__() 
    
                if(itemFeatures.__len__() != 0) :   
                    # Add to the global features list
                    self.features.append(itemFeatures)
                    
                    '''
                    if(self.libSVMFormat == 'true'):
                        if not item['label'] in self.labelsNamesMap:
                            self.labelsNamesMap[item['label']] = labelIdx
                            labelIdx += 1
                        self.labels.append(self.labelsNamesMap[item['label']])
                        #DEBUG_LIMIT_IRRELEVANT_TRAIN_AND_TEST
                        if DEBUG_LIMIT_IRRELEVANT_TRAIN_AND_TEST:
                            if(item['label'] == 'irrelevant'):
                                irrelevantNum += 1
                        #/DEBUG_LIMIT_IRRELEVANT_TRAIN_AND_TEST
                    else:
                        self.labels.append(item['label'])
                    '''
                    if(self.libSVMFormat == 'true'):
                        if not item['label'] in self.labelsNamesMap:
                            print('Incorrect label ' + item['label']) 
                        if item['label'] == 'irirrelevant':
                            item['label'] = 'irrelevant'
                            print('Incorrect label ' + item['label'])
                        try:
                            self.labels.append(self.labelsNamesMap[item['label']])
                        except KeyError:
                            print('Incorrect label ' + item['label'])
                    else:
                        self.labels.append(item['label'])
        #DEBUG_LIMIT_IRRELEVANT_TRAIN_AND_TEST
        if DEBUG_LIMIT_IRRELEVANT_TRAIN_AND_TEST:
            print('Number of irrelevant examples: ' + str(irrelevantNum) + '\n')
        #/DEBUG_LIMIT_IRRELEVANT_TRAIN_AND_TEST
        
        # Print the label/index mapping
        
        for label in self.labelsNamesMap:
            print(label + '  ' + str(self.labelsNamesMap[label]))


    def ExtractTFIDFFeatures(self):
        
        # Loop on the dataset items
        irrelevantNum = 0
        
        documentFequency = {}
        # First collect the document frequency info
        for item in self.dataSet:
            if(not (item['text'] is None) and not(item['label'] is None)):
                # Form the list of language model terms
                terms = self.languageModel.SplitIntoTerms(item['text'])
            
                # Extract features for the item based on its terms
                for term in self.languageModel.languageModel:
                    # If the term exist in the language model
                    if term in terms:
                        try:
                            documentFequency[term] += 1                                
                        except:
                            documentFequency[term] = 1
                        
        for item in self.dataSet:
            if(not (item['text'] is None) and not(item['label'] is None)):
                # Initialize the items dictionary. It's sparse dictionary, with only words in the language model that exist in the item.
                itemFeatures = {}
                #intialize term frequency dictionary, it holds the occurences of each word in the tweet   
                termFrequency = {}
                # Form the list of language model terms
                # Initialize the features vector
                for term in self.languageModel.languageModel:
                    if(self.libSVMFormat == 'true'):
                        itemFeatures[self.featuresNamesMap[term]] = 0
                    else:
                        itemFeatures[term] = 0
                    
                # Form the list of language model terms
                terms = self.languageModel.SplitIntoTerms(item['text'])
            
                # Extract features for the item based on its terms
                for term in terms:
                
                    # If the term exist in the language model
                    if term in self.languageModel.languageModel:
                    
                        # Add the feature if not exists or increment it if exists
                        try:
                            if(self.libSVMFormat == 'true'):
                                termFrequency[self.featuresNamesMap[term]] = 1
                            else:
                                termFrequency[term] = 1
                        except:
                            if(self.libSVMFormat == 'true'):
                                if self.featureFormat != 'Binary':
                                    termFrequency[self.featuresNamesMap[term]] += 1
                            else:
                                if self.featureFormat != 'Binary':
                                    termFrequency[term] += 1
                #Extract features based on TF-IDF
                for term in terms:
                    # If the term exist in the language model
                    if term in self.languageModel.languageModel:
                        # Add the feature if not exists or increment it if exists
                        try:
                            if(self.libSVMFormat == 'true'):
                                #itemFeatures[self.featuresNamesMap[term]] = 1+math.log(termFrequency[self.featuresNamesMap[term]])*(self.languageModel.languageModel[term]/len(self.dataSet))
                                #itemFeatures[self.featuresNamesMap[term]] = (0.5 + 0.5 * termFrequency[self.featuresNamesMap[term]] / max(termFrequency.values())) * math.log(len(self.dataSet) / self.languageModel.languageModel[term])
                                #itemFeatures[self.featuresNamesMap[term]] = (0.5 + 0.5 * termFrequency[self.featuresNamesMap[term]] / max(self.languageModel.languageModel.values())) * math.log(len(self.dataSet) / self.languageModel.languageModel[term])
                                #itemFeatures[self.featuresNamesMap[term]] = (termFrequency[self.featuresNamesMap[term]] / max(self.languageModel.languageModel.values())) * math.log(len(self.dataSet) / self.languageModel.languageModel[term])
                                #itemFeatures[self.featuresNamesMap[term]] = (termFrequency[self.featuresNamesMap[term]] / max(self.languageModel.languageModel.values())) * math.log(sum(self.languageModel.languageModel.values()) / self.languageModel.languageModel[term])
                                #itemFeatures[self.featuresNamesMap[term]] = (termFrequency[self.featuresNamesMap[term]] / max(self.languageModel.languageModel.values())) * math.log(sum(documentFequency.values()) / documentFequency[term])
                                #itemFeatures[self.featuresNamesMap[term]] = (termFrequency[self.featuresNamesMap[term]] / max(self.languageModel.languageModel.values())) * math.log(self.dataSet.__len__() / documentFequency[term])
                                #itemFeatures[self.featuresNamesMap[term]] = (termFrequency[self.featuresNamesMap[term]]) * math.log(self.dataSet.__len__() / documentFequency[term])
                                itemFeatures[self.featuresNamesMap[term]] = (0.5 + 0.5 * termFrequency[self.featuresNamesMap[term]] / max(self.languageModel.languageModel.values())) * math.log(self.dataSet.__len__() / documentFequency[term])
                                #itemFeatures[self.featuresNamesMap[term]] = (0.5 + 0.5 * termFrequency[self.featuresNamesMap[term]] / max(self.languageModel.languageModel.values()))
                                #itemFeatures[self.featuresNamesMap[term]] = termFrequency[self.featuresNamesMap[term]]
                            else:
                                #itemFeatures[term] = 1+math.log(termFrequency[term])*(self.languageModel.languageModel[term]/len(self.dataSet))
                                #itemFeatures[term] = (0.5 + 0.5 * termFrequency[term] / max(termFrequency.values())) * math.log(len(self.dataSet) / self.languageModel.languageModel[term])
                                #itemFeatures[term] = (0.5 + 0.5 * termFrequency[term] / max(self.languageModel.languageModel.values())) * math.log(len(self.dataSet) / self.languageModel.languageModel[term])
                                #itemFeatures[term] = (termFrequency[term] / max(self.languageModel.languageModel.values())) * math.log(sum(self.languageModel.languageModel.values()) / self.languageModel.languageModel[term])
                                #itemFeatures[term] = (termFrequency[term] / max(self.languageModel.languageModel.values())) * math.log(sum(documentFequency.values()) / documentFequency[term])
                                #itemFeatures[term] = (termFrequency[term] / max(self.languageModel.languageModel.values())) * math.log(self.dataSet.__len__() / documentFequency[term])
                                #itemFeatures[term] = (termFrequency[term]) * math.log(self.dataSet.__len__() / documentFequency[term])
                                itemFeatures[term] = (0.5 + 0.5 * termFrequency[term] / max(self.languageModel.languageModel.values())) * math.log(self.dataSet.__len__() / documentFequency[term])
                        except:
                            if(self.libSVMFormat == 'true'):
                                if self.featureFormat != 'Binary':
                                    #itemFeatures[self.featuresNamesMap[term]] += 1+math.log(termFrequency[self.featuresNamesMap[term]])*(self.languageModel.languageModel[term]/len(self.dataSet))
                                    #itemFeatures[self.featuresNamesMap[term]] += (0.5 + 0.5 * termFrequency[self.featuresNamesMap[term]] / max(termFrequency.values())) * math.log(len(self.dataSet) / self.languageModel.languageModel[term])
                                    #itemFeatures[self.featuresNamesMap[term]] += (0.5 + 0.5 * termFrequency[self.featuresNamesMap[term]] / max(self.languageModel.languageModel.values())) * math.log(len(self.dataSet) / self.languageModel.languageModel[term])
                                    #itemFeatures[self.featuresNamesMap[term]] += (termFrequency[self.featuresNamesMap[term]] / max(self.languageModel.languageModel.values())) * math.log(sum(self.languageModel.languageModel.values()) / self.languageModel.languageModel[term])
                                    #itemFeatures[self.featuresNamesMap[term]] += (termFrequency[self.featuresNamesMap[term]] / max(self.languageModel.languageModel.values())) * math.log(sum(documentFequency.values()) / documentFequency[term])
                                    #itemFeatures[self.featuresNamesMap[term]] += (termFrequency[self.featuresNamesMap[term]] / max(self.languageModel.languageModel.values())) * math.log(self.dataSet.__len__() / documentFequency[term])
                                    #itemFeatures[self.featuresNamesMap[term]] += (termFrequency[self.featuresNamesMap[term]]) * math.log(self.dataSet.__len__() / documentFequency[term])
                                    #itemFeatures[self.featuresNamesMap[term]] += (0.5 + 0.5 * termFrequency[self.featuresNamesMap[term]] / max(self.languageModel.languageModel.values())) * math.log(self.dataSet.__len__() / documentFequency[term])
                                    #itemFeatures[self.featuresNamesMap[term]] += (0.5 + 0.5 * termFrequency[self.featuresNamesMap[term]] / max(self.languageModel.languageModel.values()))
                                    #itemFeatures[self.featuresNamesMap[term]] += termFrequency[self.featuresNamesMap[term]]
                                    itemFeatures[self.featuresNamesMap[term]] = (0.5 + 0.5 * termFrequency[self.featuresNamesMap[term]] / max(self.languageModel.languageModel.values())) * math.log(self.dataSet.__len__() / documentFequency[term])
                                    #itemFeatures[self.featuresNamesMap[term]] = termFrequency[self.featuresNamesMap[term]]
                            else:
                                if self.featureFormat != 'Binary':
                                    #itemFeatures[term] += 1+math.log(termFrequency[term])*(self.languageModel.languageModel[term]/len(self.dataSet))
                                    #itemFeatures[term] += (0.5 + 0.5 * termFrequency[term] / max(termFrequency.values())) * math.log(len(self.dataSet) / self.languageModel.languageModel[term])
                                    #itemFeatures[term] += (0.5 + 0.5 * termFrequency[term] / max(self.languageModel.languageModel.values())) * math.log(len(self.dataSet) / self.languageModel.languageModel[term])
                                    #itemFeatures[term] += (termFrequency[term] / max(self.languageModel.languageModel.values())) * math.log(sum(self.languageModel.languageModel.values()) / self.languageModel.languageModel[term])
                                    #itemFeatures[term] += (termFrequency[term] / max(self.languageModel.languageModel.values())) * math.log(sum(documentFequency.values()) / documentFequency[term])
                                    #itemFeatures[term] += (termFrequency[term] / max(self.languageModel.languageModel.values())) * math.log(self.dataSet.__len__() / documentFequency[term])
                                    #itemFeatures[term] += (termFrequency[term]) * math.log(self.dataSet.__len__() / documentFequency[term])
                                    #itemFeatures[term] += (0.5 + 0.5 * termFrequency[term] / max(self.languageModel.languageModel.values())) * math.log(self.dataSet.__len__() / documentFequency[term])
                                    itemFeatures[term] = (0.5 + 0.5 * termFrequency[term] / max(self.languageModel.languageModel.values())) * math.log(self.dataSet.__len__() / documentFequency[term])
                       
            
               
                if(itemFeatures.__len__() != 0):   
                    # Add to the global features list
                    self.features.append(itemFeatures)
                    '''
                    for itemFeature in itemFeatures:
                        try:
                            itemFeature /= max(itemFeatures.values())
                        except:
                            itemFeature = itemFeature
                    '''
                    '''
                    if(self.libSVMFormat == 'true'):
                        if not item['label'] in self.labelsNamesMap:
                            self.labelsNamesMap[item['label']] = labelIdx
                            labelIdx += 1
                        self.labels.append(self.labelsNamesMap[item['label']])
                        #DEBUG_LIMIT_IRRELEVANT_TRAIN_AND_TEST
                        if DEBUG_LIMIT_IRRELEVANT_TRAIN_AND_TEST:
                            if(item['label'] == 'irrelevant'):
                                irrelevantNum += 1
                        #/DEBUG_LIMIT_IRRELEVANT_TRAIN_AND_TEST
                    else:
                        self.labels.append(item['label'])
                    '''
                    if(self.libSVMFormat == 'true'):
                        if not item['label'] in self.labelsNamesMap:
                            print('Incorrect label ' + item['label']) 
                        if item['label'] == 'irirrelevant':
                            item['label'] = 'irrelevant'
                            print('Incorrect label ' + item['label'])
                        try:
                            self.labels.append(self.labelsNamesMap[item['label']])
                        except KeyError:
                            print('Incorrect label ' + item['label'])
                    else:
                        self.labels.append(item['label'])
        #DEBUG_LIMIT_IRRELEVANT_TRAIN_AND_TEST
        if DEBUG_LIMIT_IRRELEVANT_TRAIN_AND_TEST:
            print('Number of irrelevant examples: ' + str(irrelevantNum) + '\n')
        #/DEBUG_LIMIT_IRRELEVANT_TRAIN_AND_TEST
        
        # Print the label/index mapping
        
        for label in self.labelsNamesMap:
            print(label + '  ' + str(self.labelsNamesMap[label]))

        
    def DumpFeaturesToTxt(self, exportFileName):
        # Open the file
        exportFile = open(exportFileName, 'w')

        # Keep the index for the label dict
        index = 0
        for feature in self.features:
            # Write the target/label line
            for i in range(self.labelsNamesMap.__len__()):
                # labels start from 1 to match liblinear requirements
                if(i == self.labels[index] - 1):
                    exportFile.write("1, ")
                else:
                    exportFile.write("0, ")
            exportFile.write("\n")
            
            # Write the features line
            # We must lop on all the entries of the features map
            for i in range(self.featuresNamesMap.__len__()):
                # Each feature is a dictionary = sparse format in MATLAB
                # i is the position in the full sparse vector
                # if the position i is a valid entry (i.e. in the keys of) features, then its entry is logged
                # else 0 is logged
                # In case of Binary mode, if the position i is filled, 1 is logged and not the normalized value
                # features indices start from 1 to match liblinear requirements 
                if((i+1) in feature.keys()):
                    if(self.featureFormat == "Normal"):
                        exportFile.write(str(feature[i]) + ", ")
                    elif (self.featureFormat == "Binary"):
                        exportFile.write("1, ")
                else:
                    exportFile.write("0, ")
            exportFile.write("\n")
            
            index += 1
            
        exportFile.close()
                    
    def ParseConfigFile(self, configDocName):
        # Get the name of configuration file from the cmd line argument
        xmldoc = minidom.parse(configDocName)    
        
        # Get the language model
        self.featuresVectorLength = xmldoc.getElementsByTagName('FeaturesVectorLength')[0].attributes['featuresVectorLength'].value

        # Get the language model
        self.libSVMFormat = xmldoc.getElementsByTagName('LibSVMFormat')[0].attributes['libSVMFormat'].value        

        # Get the stemming enable flag
        self.enableStemming = xmldoc.getElementsByTagName('EnableStemming')[0].attributes['enableStemming'].value
 
        # Get the ExportMode
        self.featureFormat = xmldoc.getElementsByTagName('FeatureFormat')[0].attributes['featureFormat'].value
        
        # Get the Label
        labelIdx = 1
        if(self.libSVMFormat == 'true'):
            labels = xmldoc.getElementsByTagName('Label')
            for label in labels:
                if not label.attributes['label'].value in self.labelsNamesMap:
                    self.labelsNamesMap[label.attributes['label'].value] = labelIdx
                    labelIdx += 1
                
           
               
    # To save to serialzation file
    def SaveFeatures(self):
        # You must close and open to append to the binary file
        # Open the serialization file
        serializationFile = open(self.featuresSerializationFileName, 'wb')
        # Save the model
        pickle.dump(self.features, serializationFile)
        # Open the serialization file
        serializationFile.close()

        
    # To load saved model
    def LoadFeatures(self):
        # Load the model
        serializatoinDatasetFile = open(self.featuresSerializationFileName, 'rb')
        self.features = pickle.load(serializatoinDatasetFile)
        serializatoinDatasetFile.close()

    # To save to serialzation file
    def SaveLabels(self):
        # You must close and open to append to the binary file
        # Open the serialization file
        serializationFile = open(self.labelsSerializationFileName, 'wb')
        # Save the model
        pickle.dump(self.labels, serializationFile)
        # Open the serialization file
        serializationFile.close()

        
    # To load saved model
    def LoadLabels(self):
        # Load the model
        serializatoinDatasetFile = open(self.labelsSerializationFileName, 'rb')
        self.labels = pickle.load(serializatoinDatasetFile)
        serializatoinDatasetFile.close()        
        