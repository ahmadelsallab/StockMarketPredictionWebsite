'''
Created on Nov 14, 2013

@author: ASALLAB
'''
import pickle
import nltk
class Classifier(object):
    '''
    classdocs
    '''    

    def __init__(self, featuresSerializationFileName, classifierType, trainFeatures, trainTargets, testFeatures, testTargets):
        '''
        Constructor
        '''
        self.classifierType = classifierType
        self.trainFeatures = trainFeatures
        self.trainTargets = trainTargets
        self.testFeatures = testFeatures
        self.testTargets = testTargets
        
        # Store the serialization file
        self.featuresSerializationFileName = featuresSerializationFileName 
      
    # Method to train the classifier    
    def Train(self):
    
        # Check classifier type
        if(self.classifierType == "SVM"):
            
            from liblinearutil import train            
            self.cParam = 32# Best cross validation accuracy
            self.nFoldsParam = 10
            self.svmModel = train(self.trainTargets, self.trainFeatures, '-c ' + str(self.cParam))
            train(self.trainTargets, self.trainFeatures, '-c ' + str(self.cParam) + ' -v ' + str(self.nFoldsParam))
            '''
            from svmutil import svm_train
            self.svmModel = svm_train(self.trainTargets, self.trainFeatures, '-c 4 -s 2 -t 2')
            '''
        if(self.classifierType == "naive bayesian classifier"):
            import nltk
#             for (trainDataFeatureSet in self.trainFeatures) and (trainDataLabel in self.trainTargets):
            nbtrainData = []
            i = 0
            while i<len(self.trainFeatures):
                row = [self.trainFeatures[i] , self.trainTargets[i]]
                nbtrainData.append(row)
                i+=1

            self.naiveBayesClassifier = nltk.NaiveBayesClassifier.train(nbtrainData)
            
     # Method to test the classifier    
    def Test(self, languageModel = None):        
        # Check classifier type
        if(self.classifierType == "SVM"):
            
            from liblinearutil import predict
            label, acc, val = predict(self.testTargets, self.testFeatures, self.svmModel)
            return label, acc, val
            
            '''
            from svmutil import svm_predict
            label, acc, val = svm_predict(self.testTargets, self.testFeatures, self.svmModel)
            return label, acc, val
            '''
        
        if(self.classifierType == "naive bayesian classifier"):
            label = []
            acc = 0.0
            val = 0.0
      
            nGood = 0
            nBad = 0
            i = 0
            while i<len(self.testFeatures):  
                classifiedLabel = (self.naiveBayesClassifier.classify(self.testFeatures[i]))
                label.append(classifiedLabel)
                if classifiedLabel == self.testTargets[i]:
                    nGood +=1
                else:
                    nBad +=1
                i+=1
                
            acc = nGood/(nGood+nBad)
            return label, acc, val
        
        if (self.classifierType == "BM25"):
            labels = []
            #BM25 Configration 
            k1 = 1.0
            b = 1.0
 
            tfM = {}
            i = 1
     
            for term in self.trainFeatures[0]:
                cnt = [0,0] #to be scalled to unnknown number of labels

                j = 0
                while j<len(self.trainFeatures):
 
                    if self.trainFeatures[j][i] != 0:  #tfidf values have garbage values 
                        labelID = self.trainTargets[j]
                        cnt[labelID - 1] += 1
 
                    j+=1
     
                tfM[term] = cnt
                
                i+=1;
             
            for tweetRow in self.testFeatures: 
                tf = {}
                for term in tweetRow:
                    if term in tf:
                        tf[term] = tf[term] + 1
                    else:
                        tf[term] = 1
 
                BM_R = 0
                BM_IR = 0
                for term in tweetRow:
                    tfidf = tweetRow[term]  #because the features wights are calculated using TFIDF
                    idf = tfidf/tf[term]
                    i = 1  
                    tfR = tfM[term][0]
                    tfIR = tfM[term][1]
 
                    BM_term_R = ( idf * tfR* (k1 + 1) ) / (tfR + k1*(1-b+b*(len(tweetRow))) )
                    BM_term_IR = ( idf * tfIR* (k1 + 1) ) / (tfIR + k1*(1-b+b*(len(tweetRow))) )
                    
                    BM_R += BM_term_R
                    BM_IR += BM_term_IR
#                 print("BM "+str(BM_R)+" "+str(BM_IR))
                if BM_R > BM_IR:
                    labels.append(1)
                else:
                    labels.append(2)
                    
        for x in tf:
           
            print(str(x) +" " + str(tfM[x][0])+ " "+ str(tfM[x][1]))
        acc = 0.0
        val = 0.0
        return labels,acc,val
    
    # For cross validation accuracy
    # nFoldsParam = 10
    # crossValidationAccuracy = train(featuresExtractor.labels, featuresExtractor.features, '-c' + str(cParam) + '-v' + str(nFoldsParam))
    
    # A train test splitter util needs to be added to DatasetBuilder and called before the features extractor, then
    # we should have trainFeaturesExtractor (trainFeatures) and testFeaturesExtractor (testFeatures) 
        # To save to serialzation file
    def SaveModel(self):
        from liblinearutil import save_model
        save_model(self.featuresSerializationFileName, self.svmModel)
        '''
        # You must close and open to append to the binary file
        # Open the serialization file
        serializationFile = open(self.featuresSerializationFileName, 'wb')
        
        # Save the model
        pickle.dump(self.trainFeatures, serializationFile)
        pickle.dump(self.trainTargets, serializationFile)
        pickle.dump(self.cParam, serializationFile)
        pickle.dump(self.nFoldsParam, serializationFile)
        
        # Open the serialization file
        serializationFile.close()
        '''
        
    # To load saved model
    def LoadModel(self):
        from liblinearutil import load_model
        self.svmModel = load_model(self.featuresSerializationFileName)
        '''
        # Load the model
        serializatoinDatasetFile = open(self.featuresSerializationFileName, 'rb')
        
        self.trainFeatures = pickle.load(serializatoinDatasetFile)
        self.trainTargets = pickle.load(serializatoinDatasetFile)
        self.cParam = pickle.load(serializatoinDatasetFile)
        self.nFoldsParam = pickle.load(serializatoinDatasetFile)
        # Check classifier type
        if(self.classifierType == "SVM"):            
            from liblinearutil import train            
            self.svmModel = train(self.trainTargets, self.trainFeatures, '-c ' + str(self.cParam))
        '''
        
        
    def BuildConfusionMatrix(self, vDesiredTargets, vObtainedTargets):
        import  numpy
        # Size of matrix is the maximum ID of classes
        nSizeOfMatrix = max(vDesiredTargets)
        mConfusionMatrix = numpy.zeros(nSizeOfMatrix * nSizeOfMatrix).reshape(nSizeOfMatrix, nSizeOfMatrix)
        mNormalConfusionMatrix = numpy.zeros(nSizeOfMatrix * nSizeOfMatrix).reshape(nSizeOfMatrix, nSizeOfMatrix)
        vNumTrainExamplesPerClass = numpy.zeros(nSizeOfMatrix)
        
        for i in range(vDesiredTargets.__len__()):
            vNumTrainExamplesPerClass[vDesiredTargets[i] - 1] += 1
            mConfusionMatrix[vDesiredTargets[i] - 1, vObtainedTargets[i] - 1] += 1        
        
    
        for m in range(nSizeOfMatrix):
            mNormalConfusionMatrix[m] = mConfusionMatrix[m] / sum(mConfusionMatrix[m])
        
        vAccuracyPerClass = numpy.zeros(nSizeOfMatrix)
        vCorrectlyClassifiedExamplesPerClass = numpy.diag(mConfusionMatrix)
        for n in range(vNumTrainExamplesPerClass.__len__()):
            vAccuracyPerClass[n] = vCorrectlyClassifiedExamplesPerClass[n] / vNumTrainExamplesPerClass[n]        
        
        nOverallAccuracy = sum(numpy.diag(mConfusionMatrix))/sum(vNumTrainExamplesPerClass)
        
        return mConfusionMatrix, mNormalConfusionMatrix, vNumTrainExamplesPerClass, vAccuracyPerClass, nOverallAccuracy
    
            