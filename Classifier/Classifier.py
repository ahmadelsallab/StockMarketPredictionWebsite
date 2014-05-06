'''
Created on Nov 14, 2013

@author: ASALLAB
'''
import pickle
from xml.dom import minidom
import nltk, nltk.classify.util, nltk.metrics
from nltk.classify import MaxentClassifier
from encodings.utf_8 import encode

class Classifier(object):
    '''
    classdocs
    '''    

    def __init__(self,configDocName ,featuresSerializationFileName,  trainFeatures, trainTargets, testFeatures, testTargets):
        '''
        Constructor
        '''
         # Parse the configurations file
        self.ParseConfigFile(configDocName)
        
         
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
            self.classifierModel = train(self.trainTargets, self.trainFeatures, '-c ' + str(self.cParam))
            train(self.trainTargets, self.trainFeatures, '-c ' + str(self.cParam) + ' -v ' + str(self.nFoldsParam))
            '''
            from svmutil import svm_train
            self.classifierModel = svm_train(self.trainTargets, self.trainFeatures, '-c 4 -s 2 -t 2')
            '''
        else:
            train_set = []
            i = 0;
            weights = [];
            encoding = []
            for fet in self.trainFeatures:
                train_set.append((self.trainFeatures[i],self.trainTargets[i]))
                weights.append( i * 0.5)
               
                i +=1
            if(self.classifierType == "DecisionTree"):
                self.classifierModel = nltk.DecisionTreeClassifier.train(train_set,entropy_cutoff=.01,depth_cutoff=300,binary=True,verbose=True)
                sorted(self.classifierModel.labels())
                print(self.classifierModel)
            

    # Method to test the classifier    
    def Test(self):        
        # Check classifier type
        if(self.classifierType == "SVM"):
            
            from liblinearutil import predict
            label, acc, val = predict(self.testTargets, self.testFeatures, self.classifierModel)
            return label, acc, val
            
            
            '''
            from svmutil import svm_predict
            label, acc, val = svm_predict(self.testTargets, self.testFeatures, self.classifierModel)
            return label, acc, val
            '''
        else:
            label = []
            acc  = 0
            rel = 0
            irrel = 0;
            i = 0;
            for test in self.testFeatures:
                res = self.classifierModel.classify(test)
                label.append(res)
                if self.testTargets[i] == res:
                    acc += 1
                if res == 1.0:
                    rel +=1
                else:
                    irrel +=1
                i +=1 
            val = [rel/len(self.testFeatures) , irrel /len(self.testFeatures) ]
            acc = acc / len(self.testFeatures) *100 
            print("Count " + str(rel+irrel))
            print("Acc = " + str(acc) + " %")
            return label,acc, val
                    
                
              
            
           
    # For cross validation accuracy
    # nFoldsParam = 10
    # crossValidationAccuracy = train(featuresExtractor.labels, featuresExtractor.features, '-c' + str(cParam) + '-v' + str(nFoldsParam))
    
    # A train test splitter util needs to be added to DatasetBuilder and called before the features extractor, then
    # we should have trainFeaturesExtractor (trainFeatures) and testFeaturesExtractor (testFeatures) 
        # To save to serialzation file
    def SaveModel(self):
        from liblinearutil import save_model
        save_model(self.featuresSerializationFileName, self.classifierModel)
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
        self.classifierModel = load_model(self.featuresSerializationFileName)
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
            self.classifierModel = train(self.trainTargets, self.trainFeatures, '-c ' + str(self.cParam))
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
    
    def ParseConfigFile(self, configDocName):
        # Get the name of configuration file from the cmd line argument
        xmldoc = minidom.parse(configDocName)    
        # Get the classifierType
        self.classifierType = xmldoc.getElementsByTagName('classifierType')[0].attributes['classifierType'].value
