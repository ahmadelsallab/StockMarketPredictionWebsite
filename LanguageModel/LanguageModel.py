'''
Created on Oct 22, 2013

@author: ASALLAB
'''

from xml.dom import minidom
from collections import OrderedDict
import pickle
from nltk.stem.isri import ISRIStemmer
class LanguageModel(object):
    '''
    classdocs
    '''

    # The dataset to work on to extract the model
    dataset = []
    
    # Term/Freq langauge model
    languageModel = {}
    
    # Dict of stop words
    stopWords = {}
        
    def __init__(self, configFileName, stopWordsFileName, languageModelSerializationFileName, dataset):
        '''
        Constructor
        '''
        
        # Store the dataset
        self.dataset = dataset
        
        # Parse the configurations file
        self.ParseConfigFile(configFileName)
        
        # Instanstiate the stemmer if stemming is enabled
        if self.enableStemming == "true":
            self.stemmer = ISRIStemmer()
            
        # Store the stop words
        self.UpdateStopWords(stopWordsFileName)
        
        # Store the serialization file
        self.languageModelSerializationFileName = languageModelSerializationFileName 
        

    
    # Manager to choose which language model to build    
    def BuildLanguageModel(self):
        
        # Build the N-gram
        self.BuildNGram(self.NGram)
        
        # Order with the highest encountered word first
        self.languageModel = OrderedDict(reversed(sorted(self.languageModel.items(), key=lambda t:t[1])))
        
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
 
    def BuildNGram(self, N):
         
        # Loop on all dataset entries
        for item in self.dataset:
            # Get the text
            text = item['text']
            
            # Split into words
            try:
                items = text.split()
            except:
                print('Error in tweet text' + str(text))
                #items = str(text)
                
            for i in range(len(items) - (N-1)):
                # Form the term
                term = ''
                for j in range(N):
                    if(self.enableStemming == "true"):
                        term += self.stemmer.stem(items[i + j])
                    else:                        
                        term += items[i + j]
                    if(j < N-1):
                        term += ' '
                
                # Insert the term in the model
                self.InsertInLanguageModel(term)
    
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
        for term, freq in self.languageModel.items():
            fout.write(term + " " + str(freq) + "\n")
        
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
            try:
                self.languageModel[item] = lineItems[1]
            except:
                # The language model contains no frequency, assume 1 for each term
                self.languageModel[item] = 1
            
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