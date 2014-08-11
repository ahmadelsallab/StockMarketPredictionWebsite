'''
Created on Oct 22, 2013

@author: ASALLAB
'''

from xml.dom import minidom
from collections import OrderedDict
import pickle
from nltk.stem.isri import ISRIStemmer
import re
from bs4 import BeautifulSoup
import urllib.request
from _io import open

class LanguageModel(object):
    '''
    classdocs
    '''

        
    def __init__(self, configFileName, stopWordsFileName, languageModelSerializationFileName, linksDBFileName, dataset):
        '''
        Constructor
        '''
        # The dataset to work on to extract the model
        self.dataset = []
        
        # Term/Freq langauge model
        self.languageModel = {}    
        self.languageModelFreqInfo = {}
        
        # Dict of stop words
        self.stopWords = {}
        
        # Store the dataset
        self.dataset = dataset
        
        # Initialize number of terms per label
        self.numTermsPerLabel = {}
        
        # Initialize the links DB
        self.linksDB = {}
        self.linksDBFileName = linksDBFileName
        
        # Parse the configurations file
        self.ParseConfigFile(configFileName)
        
        # Instanstiate the stemmer if stemming is enabled
        if self.enableStemming == "true":
            self.stemmer = ISRIStemmer()
            
        # Store the stop words
        self.UpdateStopWords(stopWordsFileName)
        
        # Store the serialization file
        self.languageModelSerializationFileName = languageModelSerializationFileName 
        
        # Initialize total docs
        self.totalNumberOfDocs = len(self.dataset)
        
            
    # Manager to choose which language model to build    
    def BuildLanguageModel(self):
        
        # Build the N-gram
        self.BuildNGram(self.NGram)
        
        # Order with the highest encountered word first
        self.languageModel = OrderedDict(reversed(sorted(self.languageModel.items(), key=lambda t:t[1])))
        
        if(self.buildLinksDB == "true"):
            self.SaveLinksDatabase()   
        '''
        if(self.languageModelMode == "Unigram"):
            self.BuildUniGram()
        elif(self.languageModelMode == "Bigram"):
            self.BuildBiGram()
        elif(self.languageModelMode == "Trigram"):
            self.BuildTriGram()
        else:
            print('Error! No language defined for' + self.languageModelMode) 
        '''
    # Manager to choose which language model to build    
    def UpdateLanguageModel(self, dataset):
        # Update the dataset
        self.dataset = dataset
        # Update the model
        self.BuildNGram(self.NGram)
        
        if(self.buildLinksDB == "true"):
            self.SaveLinksDatabase()       
        
        '''
        if(self.languageModelMode == "Unigram"):
            self.BuildUniGram()
        elif(self.languageModelMode == "Bigram"):
            self.BuildBiGram()
        elif(self.languageModelMode == "Trigram"):
            self.BuildTriGram()
        else:
            print('Error! No language defined for' + self.languageModelMode)
        '''                                    
            
    def BuildNGram(self, Ngram):
                
        # Loop on all dataset entries
        for item in self.dataset:

            # Get the text of the body of the tweet
            text = item['text']
            

            # Parse the link pattern
            url = re.findall(r'(https?:[//]?[^\s]+)', item['text'])
                        
            # if there's any link add it to the Db
            if len(url) > 0:
                if(self.buildLinksDB == "true"):
                    self.linksDB[url[0]] = item['label']
                if(self.parseLinkBody == "true"):      
                    linkText = self.ExtractLinkText(url[0])
                    if(linkText != ''):
                        text += linkText
            
            
            # Split into words
            try:
                items = text.split()
            except:
                print('Error in tweet text' + str(text))
                #items = str(text)

            # Check if leading/trailing #tags to be removed
            if(self.removeLeadTrailTags == "true"):
                items = self.TrimLeadTrailTags(items)


            documentCounted = {}
            
            # Update the language model
            for i in range(len(items) - (Ngram-1)):
                # Form the term
                term = ''
                for j in range(Ngram):
                    if(self.enableStemming == "true"):
                        term += self.stemmer.stem(items[i + j])
                    else:                        
                        term += items[i + j]
                    if(j < Ngram-1):
                        term += ' '
                
                # Insert the term in the model
                self.InsertInLanguageModel(term)
                
                # Initialize the dictionary of frequency info of the term
                if not term in self.languageModelFreqInfo:
                    self.languageModelFreqInfo[term] = {}
                    self.languageModelFreqInfo[term]['documentFrequency'] = 0
                    for label in self.labels:
                        self.languageModelFreqInfo[term][label] = 0
                    
                # We want for each term, a dictionary of:
                # Word    Freq    RelFreq    IrrelFreq    DocFreq
                
                # Update document frequency and label frequencies
                if self.considerStopWords == "true":
                    # Insert the term if not in stopWords
                    if not term in self.stopWords:
                        # Update label frequency
                        self.languageModelFreqInfo[term][item['label']] += 1
                        
                        # Increment number of terms per label
                        self.numTermsPerLabel[item['label']] += 1
    
                            
                        # The term document frequency is incremented once per document, that's why we need documentCounted
                        if not term in documentCounted:                        
                            # Update document frequency
                            documentCounted[term] = "true" 
                            self.languageModelFreqInfo[term]['documentFrequency'] += 1
    
                else:
                    # Update label frequency
                    self.languageModelFreqInfo[term][item['label']] += 1
                    
                    # Increment number of terms per label
                    self.numTermsPerLabel[item['label']] += 1
                        
                    # The term document frequency is incremented once per document, that's why we need documentCounted
                    if not term in documentCounted:                        
                        # Update document frequency
                        documentCounted[term] = "true" 
                        self.languageModelFreqInfo[term]['documentFrequency'] += 1

                
    def TrimLeadTrailTags(self, words):
        # Remove leading tags
        withoutLeadingTags = self.TrimTagsRecursive(words)
        # Remove trailing tags
        # Reverse the words to work on trailing tags
        withoutTrailingTags = self.TrimTagsRecursive(withoutLeadingTags[::-1])
        # Reverse the words back
        return withoutTrailingTags[::-1]

    def TrimTagsRecursive(self, words):
        if '#' in words[0]:
            del words[0]
            return self.TrimTagsRecursive(words)
        else:
            return words
                                  
    # Add term and update frequency                
    def InsertInLanguageModel(self, term):
        
        # If it's required to check on stop words, then we consider them, else just insert or update the word freq
        if self.considerStopWords == "true":
            # Insert the term if not in stopWords
            if not term in self.stopWords:
                               
                # Insert the word only if it doesn't exist before in the model
                if not term in self.languageModel:
                    # Put the word frequency as 1 since it's the first incident
                    self.languageModel[term] = 1       
                else:
                    # Increment the frequency
                    self.languageModel[term] += 1    
        else:

            # Insert the word only if it doesn't exist before in the model
            if not term in self.languageModel:
                # Put the word frequency as 1 since it's the first incident
                self.languageModel[term] = 1       
            else:
                # Increment the frequency
                self.languageModel[term] += 1    
    
    # Utility used to split a text into list of terms
    def SplitIntoTerms(self, text):
        # Initialize the list of terms
        terms = []
        
        # Split into words
        try:
            items = text.split()
        except:
            print('Error in tweet text' + str(text))
            #items = str(text)
            items = []
        
        # For the terms list
        for i in range(len(items) - (self.NGram - 1)):
            # Form the term
            term = ''
            
            # Form the term
            for j in range(self.NGram):
                if(self.enableStemming == "true"):
                    term += self.stemmer.stem(items[i + j])
                else:                        
                    term += items[i + j]
            
            # Insert the term in the list of terms to be returned
            terms.append(term)
        
        # Return the list of terms
        return terms
    
    # Dump the model in a file
    def DumpLanguageModel(self, fileName):
        
        # Open the file for writting
        fout = open(fileName, 'w', encoding='utf-8')
        
        # Loop on languageModel and write the key = term and value = frequency
        # We want for each term, a dictionary of:
        # Word    Freq    RelFreq    IrrelFreq    DocFreq

        for term, freq in self.languageModel.items():
            fout.write(term + " " + str(freq) + " ")
            # Print frequency info
            
            for key, item in self.languageModelFreqInfo[term].items():                
                fout.write(str(item) + " ")
            fout.write("\n")
        
        # Close the file
        fout.close()
               
    # Update stop words list
    def UpdateStopWords(self, stopWordsFileName):  
        # Open the stop words file name
        fin = open(stopWordsFileName, 'r', encoding='utf-8')
        
        # Read the file line by line
        for line in fin:
            
            # The word is the first entry in the line
            rawWord = line.split()[0]

            # Stem the word if enabled
            if(self.enableStemming == "true"):
                word = self.stemmer.stem(rawWord)
            else:
                word = rawWord
            
            # Insert the word only if it doesn't exist before in the model
            if not word in self.stopWords:
                # Put the word frequency as 1 since it's the first incident
                self.stopWords[word] = 1       
            else:
                # Increment the frequency
                self.stopWords[word] += 1  
        
        # Close the file
        fin.close()

    # Update stop words list
    def LoadModelFromTxtFile(self, langModelTxtFileName):  
        
        # Open the stop words file name
        fin = open(langModelTxtFileName, 'r', encoding='utf-8')
        
        self.languageModel = {}
        
        # Read the file line by line
        for line in fin:
            
            lineItems = line.split()
            word = lineItems[0]
            
            # Stem the word if enabled
            if(self.enableStemming == "true"):
                item = self.stemmer.stem(word)
            else:
                item = word
            self.languageModel[item] = {}
            if(self.type == 'frequencyModel'):
                try:
                    self.languageModel[item] = int(lineItems[1])
                except:
                    # The language model contains no frequency, assume 1 for each term
                    self.languageModel[item] = 1
            elif (self.type == 'lexicon'):
                self.languageModel[item]['existWeight'] = int(lineItems[1])
                self.languageModel[item]['nonExistWeight'] = int(lineItems[2])
            
        # Close the file
        fin.close()

    # Parse the configurations file
    def ParseConfigFile(self, configDocName):
        # Get the name of configuration file from the cmd line argument
        xmldoc = minidom.parse(configDocName)    
        
        # Get the language model
        self.NGram = int(xmldoc.getElementsByTagName('NGram')[0].attributes['NGram'].value)
        
        # Get the stop words option
        self.considerStopWords = xmldoc.getElementsByTagName('ConsiderStopWords')[0].attributes['considerStopWords'].value
        
        # Get the stemming enable flag
        self.enableStemming = xmldoc.getElementsByTagName('EnableStemming')[0].attributes['enableStemming'].value
        
        # Get the buildLinksDB flag
        self.buildLinksDB = xmldoc.getElementsByTagName('BuildLinksDB')[0].attributes['buildLinksDB'].value

        # Get the parseLinkBody flag
        self.parseLinkBody = xmldoc.getElementsByTagName('ParseLinkBody')[0].attributes['parseLinkBody'].value

        # Get the removeLeadTrailTags flag
        self.removeLeadTrailTags = xmldoc.getElementsByTagName('RemoveLeadTrailTags')[0].attributes['removeLeadTrailTags'].value        
        
        # Get the removeLeadTrailTags flag
        self.type = xmldoc.getElementsByTagName('Type')[0].attributes['type'].value        
        
        
        # Get the list of labels
        labels = xmldoc.getElementsByTagName('Label')
        self.labels = []
        for label in labels:
            self.labels.append(label.attributes['label'].value)
            self.numTermsPerLabel[label.attributes['label'].value] = 0
                        
        
    # To save to serialzation file
    def SaveModel(self):
        # You must close and open to append to the binary file
        # Open the serialization file
        serializationFile = open(self.languageModelSerializationFileName, 'wb')
        # Save the model
        pickle.dump(self.languageModel, serializationFile)
        # Open the serialization file
        serializationFile.close()

        
    # To load saved model
    def LoadModel(self):
        # Load the model
        serializatoinDatasetFile = open(self.languageModelSerializationFileName, 'rb')
        self.languageModel = pickle.load(serializatoinDatasetFile)
        serializatoinDatasetFile.close()
    

        
    def ExtractLinkText(self, urlstr):
        #Extract Text from Link
        try:
            fileHandle = urllib.request.urlopen(urlstr)
            #print(urlstr)
            html = fileHandle.read()
            soup = BeautifulSoup(html)
            text = ''
            
            t = ''
            #for b in soup.findAll('div'):
            for b in soup.findAll('b'):
                t += str(b)
            text += t 
            
            #data += [str(b) for b in soup.findAll('p')]
            #data += [str(b) for b in soup.findAll('a')]
            t = ''
            for b in soup.findAll('title'):
                t += str(b)
            text += t 
            
            
            #data += [str(b) for b in soup.findAll('span')]
            #data += [str(b) for b in soup.findAll(attrs = 'content')]
            #filter(None, data)
            return text
        except:
            print('URL error ' + urlstr )
            return ''     
            
    #Create Database File
    def SaveLinksDatabase(self):
        file = open(self.linksDBFileName, "w" , encoding="utf-8")
        for link, label in self.linksDB.items():
            file.write(link +' '+ label +'\n')
        file.close()