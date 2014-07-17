'''
Created on Nov 7, 2013

@author: ASALLAB
'''
from xml.dom import minidom
from LanguageModel.LanguageModel import *
import pickle
import numpy
import math
import re
from bs4 import BeautifulSoup
import urllib.request
import locale

locale.setlocale(locale.LC_NUMERIC, 'English_USA.1252')
DEBUG_LIMIT_IRRELEVANT_TRAIN_AND_TEST = False
class FeaturesExtractor(object):
    '''
    classdocs
    '''

    # Map table to map the language model into index
    featuresNamesMap = {}
    labelsNamesMap = {}
    #featuresMapExist = False
        
    def __init__(self, configFileName, featuresSerializationFileName, labelsSerializationFileName, languageModel, dataSet):
        '''
        Constructor
        '''
        # Store the language model. 
        self.languageModel = languageModel
        
        self.linksDB = {}
        self.ranges=[]
        # Parse the configurations file
        self.ParseConfigFile(configFileName)
        
        if(self.considerLinksDB == "true"):
            self.LoadLinksDatabase()
                
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
            
        #Ranges of Numbers to give higher weight    
        #Format:  1st & 2nd entries are digits range,3rd & 4th entries are numbers range  
        self.numOfRanges = int(len(self.ranges)/2)        
        featureIdx = 1
        if(self.libSVMFormat == 'true'):
            for term in self.languageModel.languageModel:
                self.featuresNamesMap[term] = featureIdx
                featureIdx += 1
            if(self.considerLinksDB == "true"):
                self.featuresNamesMap['isLink'] = featureIdx
                featureIdx += 1
                self.featuresNamesMap['isLinkRelevant'] = featureIdx
                featureIdx += 1
            if(self.considerNumbersFeatures == "true"):
                for i in range(0,self.numOfRanges+1):
                    self.featuresNamesMap['numFeature'+str(i)] = featureIdx
                    featureIdx += 1                                              
        # Store the dataset
        self.dataSet = dataSet
        
        # Store the serialization file
        self.featuresSerializationFileName = featuresSerializationFileName
        self.labelsSerializationFileName = labelsSerializationFileName 
        
        # Initialize empty list of features corresponding to each item of a dataset
        self.features = []
        self.labels = []
        
    def ExtractLexiconFeatures(self):
        
        # Loop on the dataset items
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
                
                # Get the text of the item body
                text = item['text']
                
                # Parse the link pattern
                urls = re.findall(r'(https?:[//]?[^\s]+)', item['text'])
                
                for url in urls:
                    if len(url) > 0:
                        if(self.parseLinkBody == "true"):
                            linkText = self.languageModel.ExtractLinkText(url)
                            if(linkText != ''):
                                text += linkText
                    
                # Form the list of language model terms
                terms = self.languageModel.SplitIntoTerms(text)
                
                # Extract lexicon terms from text
                # Special case for lexicon is to traverse the language model and not the terms, because if the term of the 
                # lexicon is not mentioned at all, then we set its non-exist weight
                for term in self.languageModel.languageModel:
                    if term in terms:
                        if(self.libSVMFormat == 'true'):                            
                            if self.featureFormat != 'Binary':
                                itemFeatures[self.featuresNamesMap[term]] = self.languageModel.languageModel[term]['exist_weight']
                            else:
                                itemFeatures[self.featuresNamesMap[term]] = 1
                        else:
                            if self.featureFormat != 'Binary':
                                itemFeatures[term] = self.languageModel.languageModel[term]['exist_weight']
                            else:
                                itemFeatures[term] = 1
                    else:
                        if(self.libSVMFormat == 'true'):                            
                            if self.featureFormat != 'Binary':
                                itemFeatures[self.featuresNamesMap[term]] = self.languageModel.languageModel[term]['exist_weight']
                            else:
                                itemFeatures[self.featuresNamesMap[term]] = 1
                        else:
                            if self.featureFormat != 'Binary':
                                itemFeatures[term] = -1*self.languageModel.languageModel[term]['non_exist_weight']
                            else:
                                itemFeatures[term] = -1                                
                                                      
                # if at least one relevant link exists, then set the corresponding places in the vector
                if(self.considerLinksDB == "true"):
                    for url in urls:
                        if len(url) < 0:
                            # No link
                            if(self.libSVMFormat == 'true'):
                                itemFeatures[self.featuresNamesMap['isLink']] = 0
                                itemFeatures[self.featuresNamesMap['isLinkRelevant']] = 0
    
                            else:
                                itemFeatures['isLink'] = 0
                                itemFeatures['isLinkRelevant'] = 0
                        else:
                            if(self.libSVMFormat == 'true'):
                                itemFeatures[self.featuresNamesMap['isLink']] = 1
                                if url in self.linksDB:
                                    if(self.linksDB[url] == 'relevant'):
                                        itemFeatures[self.featuresNamesMap['isLinkRelevant']] = 1
                                    else:
                                        itemFeatures[self.featuresNamesMap['isLinkRelevant']] = 0
                                else:
                                    linkText = self.languageModel.ExtractLinkText(url)
                                    if(linkText != ''):
                                        text += linkText
                                           
                            else:
                                itemFeatures['isLink'] = 1
                                if url in self.linksDB:
                                    if(self.linksDB[url] == 'relevant'):
                                        itemFeatures['isLinkRelevant'] = 1
                                    else:
                                        itemFeatures['isLinkRelevant'] = 0
                                else:
                                    linkText = self.languageModel.ExtractLinkText(url)
                                    if(linkText != ''):
                                        text += linkText
                             
                # Add to global features list                                      
                if(itemFeatures.__len__() != 0) :   
                    # Normalize the feature
                    maxValue = max(itemFeatures.values())
                    for term in itemFeatures:
                        if self.featureFormat == 'Normal':                            
                            if maxValue != 0:
                                itemFeatures[term] /= maxValue

                    # Add to the global features list
                    self.features.append(itemFeatures)
                    
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
                
                # Get the text of the item body
                text = item['text']
                
                # Parse the link pattern
                urls = re.findall(r'(https?:[//]?[^\s]+)', item['text'])
                
                for url in urls:
                    if len(url) > 0:
                        if(self.parseLinkBody == "true"):
                            linkText = self.languageModel.ExtractLinkText(url)
                            if(linkText != ''):
                                text += linkText
                    
                # Form the list of language model terms
                terms = self.languageModel.SplitIntoTerms(text)
                
                # Extract features for the item based on its terms
                for term in terms:
                    
                    # If the term exist in the language model
                    if term in self.languageModel.languageModel:
                        
                        # Add the feature if not exists or increment it if exists
                        if(self.libSVMFormat == 'true'):
                            if self.featuresNamesMap[term] in itemFeatures:
                                if self.featureFormat != 'Binary':
                                    itemFeatures[self.featuresNamesMap[term]] += 1
                            else:
                                itemFeatures[self.featuresNamesMap[term]] = 1
                        else:
                            if term in itemFeatures:
                                if self.featureFormat != 'Binary':
                                    itemFeatures[term] += 1
                            else:
                                itemFeatures[term] = 1
                                                      
                # if at least one relevant link exists, then set the corresponding places in the vector
                if(self.considerLinksDB == "true"):
                    for url in urls:
                        if len(url) < 0:
                            # No link
                            if(self.libSVMFormat == 'true'):
                                itemFeatures[self.featuresNamesMap['isLink']] = 0
                                itemFeatures[self.featuresNamesMap['isLinkRelevant']] = 0
    
                            else:
                                itemFeatures['isLink'] = 0
                                itemFeatures['isLinkRelevant'] = 0
                        else:
                            if(self.libSVMFormat == 'true'):
                                itemFeatures[self.featuresNamesMap['isLink']] = 1
                                if url in self.linksDB:
                                    if(self.linksDB[url] == 'relevant'):
                                        itemFeatures[self.featuresNamesMap['isLinkRelevant']] = 1
                                    else:
                                        itemFeatures[self.featuresNamesMap['isLinkRelevant']] = 0
                                else:
                                    linkText = self.languageModel.ExtractLinkText(url)
                                    if(linkText != ''):
                                        text += linkText
                                           
                            else:
                                itemFeatures['isLink'] = 1
                                if url in self.linksDB:
                                    if(self.linksDB[url] == 'relevant'):
                                        itemFeatures['isLinkRelevant'] = 1
                                    else:
                                        itemFeatures['isLinkRelevant'] = 0
                                else:
                                    linkText = self.languageModel.ExtractLinkText(url)
                                    if(linkText != ''):
                                        text += linkText
                                                                   
                if(itemFeatures.__len__() != 0) :   
                    # Normalize the feature
                    maxValue = max(itemFeatures.values())
                    for term in itemFeatures:
                        if self.featureFormat == 'Normal':                            
                            if maxValue != 0:
                                itemFeatures[term] /= maxValue
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
    
    def ExtractNumTfFeatures(self):
        
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
                
                # Get the text of the item body
                text = item['text']
                
                # Parse the link pattern
                urls = re.findall(r'(https?:[//]?[^\s]+)', item['text'])
                
                for url in urls:
                    if len(url) > 0:
                        if(self.parseLinkBody == "true"):
                            linkText = self.languageModel.ExtractLinkText(url)
                            if(linkText != ''):
                                text += linkText                
                    
                # Form the list of language model terms
                terms = self.languageModel.SplitIntoTerms(text)
                
                # Extract features for the item based on its terms
                for term in terms:
                    
                    # If the term exist in the language model
                    if term in self.languageModel.languageModel:
                        
                        # Add the feature if not exists or increment it if exists
                        if(self.libSVMFormat == 'true'):
                            if self.featuresNamesMap[term] in itemFeatures:
                                if self.featureFormat != 'Binary':
                                    itemFeatures[self.featuresNamesMap[term]] += 1
                            else:
                                itemFeatures[self.featuresNamesMap[term]] = 1
                        else:
                            if term in itemFeatures:
                                if self.featureFormat != 'Binary':
                                    itemFeatures[term] += 1
                            else:
                                itemFeatures[term] = 1
                                
                                                      
                nums = re.findall(u'([\d|\u0660-\u0669|\u06f0-\u06f3|\u06f7-\u07f9]*[066B|066C|060C|,|\.]*?[\d|\u0660-\u0669|\u06f0-\u06f3|\u06f7-\u07f9]+)+', text)
                numFeaturesInfo = [0] * (self.numOfRanges+1) #Create List to set the output of each row
                for num in nums:
                    if self.isDateLink(text,num) == 1: #If Date or Link Do Not Proceed
                        numFeaturesInfo[0] += 1
                        v = 0
                        for k in range(1,self.numOfRanges+1): #check ranges
                            if(self.isNumber(num)): #Make sure Regex output is Correct
                                if( self.ranges[v] <= locale.atof(num) <= self.ranges[v+1] ):
                                    numFeaturesInfo[k] +=1
                                v+=2        
                        
                #Extract Numbers features
                if(self.considerNumbersFeatures == "true"):
                    if len(nums) == 0:                              
                        # No Number
                        if(self.libSVMFormat == 'true'):
                            for i in range(0,self.numOfRanges+1):
                                itemFeatures[self.featuresNamesMap['numFeature'+str(i)]] = 0                           
                        else:
                            for i in range(0,self.numOfRanges+1):
                                itemFeatures['numFeature'+str(i)] = 0
                    else:
                        if(self.libSVMFormat == 'true'):
                            for i in range(0,self.numOfRanges+1):
                                itemFeatures[self.featuresNamesMap['numFeature'+str(i)]] = numFeaturesInfo[i]                         
                        else:
                            for i in range(0,self.numOfRanges+1):
                                itemFeatures['numFeature'+str(i)] = numFeaturesInfo[i]
                # if at least one relevant link exists, then set the corresponding places in the vector
                if(self.considerLinksDB == "true"):
                    for url in urls:
                        if len(url) < 0:
                            # No link
                            if(self.libSVMFormat == 'true'):
                                itemFeatures[self.featuresNamesMap['isLink']] = 0
                                itemFeatures[self.featuresNamesMap['isLinkRelevant']] = 0
    
                            else:
                                itemFeatures['isLink'] = 0
                                itemFeatures['isLinkRelevant'] = 0
                        else:
                            if(self.libSVMFormat == 'true'):
                                itemFeatures[self.featuresNamesMap['isLink']] = 1
                                if url in self.linksDB:
                                    if(self.linksDB[url] == 'relevant'):
                                        itemFeatures[self.featuresNamesMap['isLinkRelevant']] = 1
                                    else:
                                        itemFeatures[self.featuresNamesMap['isLinkRelevant']] = 0
                                else:
                                    linkText = self.languageModel.ExtractLinkText(url)
                                    if(linkText != ''):
                                        text += linkText
                                           
                            else:
                                itemFeatures['isLink'] = 1
                                if url in self.linksDB:
                                    if(self.linksDB[url] == 'relevant'):
                                        itemFeatures['isLinkRelevant'] = 1
                                    else:
                                        itemFeatures['isLinkRelevant'] = 0
                                else:
                                    linkText = self.languageModel.ExtractLinkText(url)
                                    if(linkText != ''):
                                        text += linkText                                    
                                                   
                if(itemFeatures.__len__() != 0) :
                    # Calculate TF-IDF
                    maxTF = max(self.languageModel.languageModel.values())
                    for term in self.languageModel.languageModel:
                        #itemFeatures[self.featuresNamesMap[term]] = 1+math.log(termFrequency[self.featuresNamesMap[term]])*(self.languageModel.languageModel[term]/len(self.dataSet))
                        #itemFeatures[self.featuresNamesMap[term]] = (0.5 + 0.5 * termFrequency[self.featuresNamesMap[term]] / max(termFrequency.values())) * math.log(len(self.dataSet) / self.languageModel.languageModel[term])
                        #itemFeatures[self.featuresNamesMap[term]] = (0.5 + 0.5 * termFrequency[self.featuresNamesMap[term]] / max(self.languageModel.languageModel.values())) * math.log(len(self.dataSet) / self.languageModel.languageModel[term])
                        #itemFeatures[self.featuresNamesMap[term]] = (termFrequency[self.featuresNamesMap[term]] / max(self.languageModel.languageModel.values())) * math.log(len(self.dataSet) / self.languageModel.languageModel[term])
                        #itemFeatures[self.featuresNamesMap[term]] = (termFrequency[self.featuresNamesMap[term]] / max(self.languageModel.languageModel.values())) * math.log(sum(self.languageModel.languageModel.values()) / self.languageModel.languageModel[term])
                        #itemFeatures[self.featuresNamesMap[term]] = (termFrequency[self.featuresNamesMap[term]] / max(self.languageModel.languageModel.values())) * math.log(sum(documentFequency.values()) / documentFequency[term])
                        #itemFeatures[self.featuresNamesMap[term]] = (termFrequency[self.featuresNamesMap[term]] / max(self.languageModel.languageModel.values())) * math.log(self.dataSet.__len__() / documentFequency[term])
                        #itemFeatures[self.featuresNamesMap[term]] = (termFrequency[self.featuresNamesMap[term]]) * math.log(self.dataSet.__len__() / documentFequency[term])
                        #itemFeatures[self.featuresNamesMap[term]] = (0.5 + 0.5 * termFrequency[self.featuresNamesMap[term]] / max(self.languageModel.languageModel.values())) * math.log(self.dataSet.__len__() / documentFequency[term])
                        #itemFeatures[self.featuresNamesMap[term]] = (0.5 + 0.5 * termFrequency[self.featuresNamesMap[term]] / max(self.languageModel.languageModel.values()))
                        #itemFeatures[self.featuresNamesMap[term]] = termFrequency[self.featuresNamesMap[term]]
                        if(self.libSVMFormat == 'true'):
                            if(itemFeatures[self.featuresNamesMap[term]] != 0):
                                itemFeatures[self.featuresNamesMap[term]] = itemFeatures[self.featuresNamesMap[term]] / maxTF * math.log(self.languageModel.totalNumberOfDocs / self.languageModel.languageModelFreqInfo[term]['documentFrequency'])
                                #itemFeatures[self.featuresNamesMap[term]] = (0.5 + 0.5 * itemFeatures[self.featuresNamesMap[term]] / maxTF) * math.log(self.languageModel.totalNumberOfDocs / self.languageModel.languageModelFreqInfo[term]['documentFrequency'])
                                #itemFeatures[self.featuresNamesMap[term]] = math.log(itemFeatures[self.featuresNamesMap[term]]) / maxTF * math.log(self.languageModel.totalNumberOfDocs / self.languageModel.languageModelFreqInfo[term]['documentFrequency'])
                                #itemFeatures[self.featuresNamesMap[term]] = itemFeatures[self.featuresNamesMap[term]] * math.log(self.languageModel.totalNumberOfDocs / self.languageModel.languageModelFreqInfo[term]['documentFrequency'])
                        else:
                            if(itemFeatures[term] != 0):
                                itemFeatures[term] = (itemFeatures[term] / maxTF) * math.log(self.languageModel.totalNumberOfDocs / self.languageModel.languageModelFreqInfo[term]['documentFrequency'])                                        
                    # Normalize the feature
                    #maxValue = max(itemFeatures.values())
                    #for term in itemFeatures:
                    #    if self.featureFormat == 'Normal':                            
                    #        if maxValue != 0:
                    #            itemFeatures[term] /= maxValue
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
            
    ##
    #Returns 1 if not Date or Link
    ##
    def isDateLink(self,d , matched):
        month = [ 'Ø¯ÙŠØ³Ù…Ø¨Ø±' , 'Ù†ÙˆÙ�Ù…Ø¨Ø±' , 'Ø§ÙƒØªÙˆØ¨Ø±' ,'Ø³Ø¨ØªÙ…Ø¨Ø±' , 'Ø§ØºØ³Ø·Ø³' , 'ÙŠÙˆÙ„ÙŠÙˆ' ,'ÙŠÙˆÙ†ÙŠÙˆ' , 'Ù…Ø§ÙŠÙˆ' , 'Ø§Ø¨Ø±ÙŠÙ„' ,'Ù…Ø§Ø±Ø³' , 'Ù�Ø¨Ø±Ø§ÙŠØ±' , 'ÙŠÙ†Ø§ÙŠØ±'  , 'Ø£Ø¨Ø±ÙŠÙ„'  , 'Ø£ÙƒØªÙˆØ¨Ø±' , 'ÙŠÙˆÙ„ÙŠØ©' , 'ÙŠÙˆÙ†ÙŠØ©' , 'Ø£Ø¹Ø³Ø·Ø³' ]
        for m in month:
            str1 = str(matched) + ' ' + str(m)
            str2 =  str(m) + ' ' + str(matched)
            if (str1 in d) or (str2 in d):
                return 0
        str3 =  str(matched) + '/'
        str4 =  '/' + str(matched)
        if (str3 in d) or ( str4 in d):
            return 0
        pattern = '[Aa-zZ]+' + str(matched) + '[Aa-zZ]*\s*'
        s = re.search (pattern , d)
        if s:
            return 0
        return 1
    

    ##
    #Correct cases in which output of regex fails (i.e B9)
    ##
    def isNumber(self,value):
        try:
            float(value)
            return True
        except ValueError:
            return False             

    def ExtractTFIDFFeatures(self):
        
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
                # Get the text of the item body
                text = item['text']
                
                # Parse the link pattern
                urls = re.findall(r'(https?:[//]?[^\s]+)', item['text'])

                for url in urls:
                    if len(url) > 0:
                        if(self.parseLinkBody == "true"):
                            text += self.languageModel.ExtractLinkText(url)

                if (self.removeLeadTrailTags):
                    text = " ".join(self.languageModel.TrimLeadTrailTags(text.split()))    
                # Form the list of language model terms
                terms = self.languageModel.SplitIntoTerms(text)
                
                # Calculate TF
                for term in terms:
                    
                    # If the term exist in the language model
                    if term in self.languageModel.languageModel:
                        
                        # Add the feature if not exists or increment it if exists
                        if(self.libSVMFormat == 'true'):
                            if self.featuresNamesMap[term] in itemFeatures:
                                if self.featureFormat != 'Binary':
                                    itemFeatures[self.featuresNamesMap[term]] += 1
                            else:
                                itemFeatures[self.featuresNamesMap[term]] = 1
                        else:
                            if term in itemFeatures:
                                if self.featureFormat != 'Binary':
                                    itemFeatures[term] += 1
                            else:
                                itemFeatures[term] = 1
                                                      
   
                if(itemFeatures.__len__() != 0) :   
                    # Calculate TF-IDF
                    maxTF = max(self.languageModel.languageModel.values())
                    for term in self.languageModel.languageModel:
                        #itemFeatures[self.featuresNamesMap[term]] = 1+math.log(termFrequency[self.featuresNamesMap[term]])*(self.languageModel.languageModel[term]/len(self.dataSet))
                        #itemFeatures[self.featuresNamesMap[term]] = (0.5 + 0.5 * termFrequency[self.featuresNamesMap[term]] / max(termFrequency.values())) * math.log(len(self.dataSet) / self.languageModel.languageModel[term])
                        #itemFeatures[self.featuresNamesMap[term]] = (0.5 + 0.5 * termFrequency[self.featuresNamesMap[term]] / max(self.languageModel.languageModel.values())) * math.log(len(self.dataSet) / self.languageModel.languageModel[term])
                        #itemFeatures[self.featuresNamesMap[term]] = (termFrequency[self.featuresNamesMap[term]] / max(self.languageModel.languageModel.values())) * math.log(len(self.dataSet) / self.languageModel.languageModel[term])
                        #itemFeatures[self.featuresNamesMap[term]] = (termFrequency[self.featuresNamesMap[term]] / max(self.languageModel.languageModel.values())) * math.log(sum(self.languageModel.languageModel.values()) / self.languageModel.languageModel[term])
                        #itemFeatures[self.featuresNamesMap[term]] = (termFrequency[self.featuresNamesMap[term]] / max(self.languageModel.languageModel.values())) * math.log(sum(documentFequency.values()) / documentFequency[term])
                        #itemFeatures[self.featuresNamesMap[term]] = (termFrequency[self.featuresNamesMap[term]] / max(self.languageModel.languageModel.values())) * math.log(self.dataSet.__len__() / documentFequency[term])
                        #itemFeatures[self.featuresNamesMap[term]] = (termFrequency[self.featuresNamesMap[term]]) * math.log(self.dataSet.__len__() / documentFequency[term])
                        #itemFeatures[self.featuresNamesMap[term]] = (0.5 + 0.5 * termFrequency[self.featuresNamesMap[term]] / max(self.languageModel.languageModel.values())) * math.log(self.dataSet.__len__() / documentFequency[term])
                        #itemFeatures[self.featuresNamesMap[term]] = (0.5 + 0.5 * termFrequency[self.featuresNamesMap[term]] / max(self.languageModel.languageModel.values()))
                        #itemFeatures[self.featuresNamesMap[term]] = termFrequency[self.featuresNamesMap[term]]
                        if(self.libSVMFormat == 'true'):
                            if(itemFeatures[self.featuresNamesMap[term]] != 0):
                                itemFeatures[self.featuresNamesMap[term]] = itemFeatures[self.featuresNamesMap[term]] / maxTF * math.log(self.languageModel.totalNumberOfDocs / self.languageModel.languageModelFreqInfo[term]['documentFrequency'])
                                #itemFeatures[self.featuresNamesMap[term]] = (0.5 + 0.5 * itemFeatures[self.featuresNamesMap[term]] / maxTF) * math.log(self.languageModel.totalNumberOfDocs / self.languageModel.languageModelFreqInfo[term]['documentFrequency'])
                                #itemFeatures[self.featuresNamesMap[term]] = math.log(itemFeatures[self.featuresNamesMap[term]]) / maxTF * math.log(self.languageModel.totalNumberOfDocs / self.languageModel.languageModelFreqInfo[term]['documentFrequency'])
                                #itemFeatures[self.featuresNamesMap[term]] = itemFeatures[self.featuresNamesMap[term]] * math.log(self.languageModel.totalNumberOfDocs / self.languageModel.languageModelFreqInfo[term]['documentFrequency'])
                        else:
                            if(itemFeatures[term] != 0):
                                itemFeatures[term] = (itemFeatures[term] / maxTF) * math.log(self.languageModel.totalNumberOfDocs / self.languageModel.languageModelFreqInfo[term]['documentFrequency'])
                    
                    if(self.considerLinksDB == "true"):
                        for url in urls:
                            if len(url) < 0:
                                if(self.libSVMFormat == 'true'):
                                    itemFeatures[self.featuresNamesMap['isLink']] = 0
                                    itemFeatures[self.featuresNamesMap['isLinkRelevant']] = 0
        
                                else:
                                    itemFeatures['isLink'] = 0
                                    itemFeatures['isLinkRelevant'] = 0
                            else:
                                if(self.libSVMFormat == 'true'):
                                    itemFeatures[self.featuresNamesMap['isLink']] = 1
                                    if url in self.linksDB:
                                        if(self.linksDB[url] == 'relevant'):
                                            itemFeatures[self.featuresNamesMap['isLinkRelevant']] = 1
                                        else:
                                            itemFeatures[self.featuresNamesMap['isLinkRelevant']] = 0
                                    else:
                                        linkText = self.languageModel.ExtractLinkText(url)
                                        if(linkText != ''):
                                            text += linkText        

                                else:
                                    itemFeatures['isLink'] = 1
                                    if url in self.linksDB:
                                        if(self.linksDB[url] == 'relevant'):
                                            itemFeatures['isLinkRelevant'] = 1
                                        else:
                                            itemFeatures['isLinkRelevant'] = 0
                                    else:
                                        linkText = self.languageModel.ExtractLinkText(url)
                                        if(linkText != ''):
                                            text += linkText        
                        

    
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
       
    def ExtractKLFeatures(self):
        
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
                # Get the text of the item body
                text = item['text']
                
                # Parse the link pattern
                urls = re.findall(r'(https?:[//]?[^\s]+)', item['text'])
                
                for url in urls:
                    if len(url) > 0:
                        if(self.parseLinkBody == "true"):
                            text += self.languageModel.ExtractLinkText(url)

                    
                # Form the list of language model terms
                terms = self.languageModel.SplitIntoTerms(text)
                
                # Calculate TF
                for term in terms:
                    
                    # If the term exist in the language model
                    if term in self.languageModel.languageModel:
                        
                        
                        probRel = self.languageModel.languageModelFreqInfo[term]['relevant'] / self.languageModel.numTermsPerLabel['relevant']
                        probIrrel = self.languageModel.languageModelFreqInfo[term]['irrelevant'] / self.languageModel.numTermsPerLabel['irrelevant']
                        #probTerm = self.languageModel.languageModel[term] / sum(self.languageModel.languageModel.values())
                        '''
                        probRel = self.languageModel.languageModelFreqInfo[term]['relevant']
                        probIrrel = self.languageModel.languageModelFreqInfo[term]['irrelevant']
                        '''
                        # Add the feature if not exists or increment it if exists
                        if(self.libSVMFormat == 'true'):
                            
                            #itemFeatures[self.featuresNamesMap[term]] = (probRel - probIrrel) / probTerm
                            itemFeatures[self.featuresNamesMap[term]] = (probRel - probIrrel)
                            #itemFeatures[self.featuresNamesMap[term]] = probRel
                            '''
                            if (probIrrel != 0):
                                try:
                                    itemFeatures[self.featuresNamesMap[term]] = math.log(probRel / probIrrel)
                                except:
                                    itemFeatures[self.featuresNamesMap[term]] = math.log(probIrrel)
                            else:
                                itemFeatures[self.featuresNamesMap[term]] = math.log(probRel)
                            '''
                        else:
                            itemFeatures[term] = (probRel - probIrrel)
                            '''
                            if (probIrrel != 0):
                                try:
                                    itemFeatures[term] = math.log(probRel / probIrrel)
                                except:
                                    itemFeatures[term] = math.log(probIrrel)
                            else:
                                itemFeatures[term] = math.log(probRel)
                            '''                          
                if(self.considerLinksDB == "true"):
                    for url in urls:
                        if len(url) < 0:
                            if(self.libSVMFormat == 'true'):
                                itemFeatures[self.featuresNamesMap['isLink']] = 0
                                itemFeatures[self.featuresNamesMap['isLinkRelevant']] = 0
                        
                            else:
                                itemFeatures['isLink'] = 0
                                itemFeatures['isLinkRelevant'] = 0
                        else:
                            if(self.libSVMFormat == 'true'):
                                itemFeatures[self.featuresNamesMap['isLink']] = 1
                                if url in self.linksDB:
                                    if(self.linksDB[url] == 'relevant'):
                                        itemFeatures[self.featuresNamesMap['isLinkRelevant']] = 1
                                    else:
                                        itemFeatures[self.featuresNamesMap['isLinkRelevant']] = 0
                                else:
                                    linkText = self.languageModel.ExtractLinkText(url)
                                    if(linkText != ''):
                                        text += linkText             
                            else:
                                itemFeatures['isLink'] = 1
                                if url in self.linksDB:
                                    if(self.linksDB[url] == 'relevant'):
                                        itemFeatures['isLinkRelevant'] = 1
                                    else:
                                        itemFeatures['isLinkRelevant'] = 0
                                else:
                                    linkText = self.languageModel.ExtractLinkText(url)
                                    if(linkText != ''):
                                        text += linkText        

                if(itemFeatures.__len__() != 0) :
                    '''
                    values = []
                    for value in itemFeatures.values():
                        values.append(abs(value))
                        
                    maxValue = max(values)
                    for itemFeature in itemFeatures:
                        itemFeature /= maxValue
                    '''
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
                        exportFile.write(str(feature[i+1]) + ", ")
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

        # Get the buildLinksDB flag
        self.considerLinksDB = xmldoc.getElementsByTagName('ConsiderLinksDB')[0].attributes['considerLinksDB'].value

        # Get the considerNumbersFeatures flag
        self.considerNumbersFeatures = xmldoc.getElementsByTagName('ConsiderNumbersFeatures')[0].attributes['considerNumbersFeatures'].value
        
        # Get the parseLinkBody flag
        self.parseLinkBody = xmldoc.getElementsByTagName('ParseLinkBody')[0].attributes['parseLinkBody'].value

        # Get the removeLeadTrailTags flag
        self.removeLeadTrailTags = xmldoc.getElementsByTagName('RemoveLeadTrailTags')[0].attributes['removeLeadTrailTags'].value        

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
        if(self.considerNumbersFeatures == 'true'):
            ranges = xmldoc.getElementsByTagName('Range')
            for range in ranges:
                self.ranges.append(locale.atof(range.attributes['NumberLimitFrom'].value))
                self.ranges.append(locale.atof(range.attributes['NumberLimitTo'].value))            
                                
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
        
    def LoadLinksDatabase(self):   
        with open(self.languageModel.linksDBFileName, encoding="utf-8") as infile:
            for line in infile:
                tmp = line.split(' ')
                self.linksDB[tmp[0]] = tmp[1]
            infile.close()
