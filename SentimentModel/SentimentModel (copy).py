from DatasetBuilder.DatasetBuilder import DatasetBuilder
import os
import pandas as pd
from sklearn.cross_validation import train_test_split
from DatasetBuilder.DatasetBuilder import DatasetBuilder
from LanguageModel.LanguageModel import LanguageModel   
from FeaturesExtractor.FeaturesExtractor import FeaturesExtractor
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.feature_selection import RFE
from sklearn.svm import LinearSVC, SVC
import pickle 


VALID_C = 200
MIN_DATA = 800

def init_dicts():

	configFileDatasetBuilder = os.path.join('DatasetBuilder','Configurations','Configurations.xml')
					   
	datasetSerializationFile = os.path.join('DatasetBuilder','Output', 'dataset.bin')

	xlsxTrainFileName = os.path.join('DatasetBuilder','Input','sentiment')


	datasetBuilder = DatasetBuilder(configFileDatasetBuilder, [], datasetSerializationFile)
	datasetBuilder.trainSet = datasetBuilder.GetSentimentDatasetFromXLSXFile(xlsxTrainFileName).values()

	words_dict = {'negative':[], 'positive': [], 'neutral': []}
	for item in datasetBuilder.trainSet:
		words_dict[item['label']] += item['words']
	for k in words_dict:
		words_dict[k] = list(set(words_dict[k]))
	
	return words_dict


class SentimentModel(object):
	def __init__(self, modeln = 1):

		self.modeln = modeln
		configFileLanguageModel = os.path.join('LanguageModel', 'Configurations', 'Configurations_sentiment.xml')
		stopWordsFileName = os.path.join('LanguageModel', 'Input', 'stop_words.txt')
		linksDBFile = os.path.join('LanguageModel', 'Output', 'links_database.txt')
		languageModelSerializationFile = os.path.join('LanguageModel', 'Output', 'language_model.bin')


		self.languageModel = LanguageModel(configFileLanguageModel, stopWordsFileName, languageModelSerializationFile, linksDBFile, [])
		

		self.configFileFeaturesExtractor = os.path.join('FeaturesExtractor', 'Configurations', 'Configurations_sentiment.xml')
		self.trainFeaturesSerializationFile = os.path.join('FeaturesExtractor', 'Output', 'train_features.bin')
		self.trainLabelsSerializationFile = os.path.join('FeaturesExtractor', 'Output', 'train_labels.bin')


	def get_data(self, backend=True):
		configFileDatasetBuilder = os.path.join('DatasetBuilder','Configurations','Configurations.xml')
		datasetSerializationFile = os.path.join('DatasetBuilder','Output', 'dataset.bin')

		self.datasetBuilder = DatasetBuilder(configFileDatasetBuilder, [], datasetSerializationFile)
		dataset = None

		#if not backend:
		xlsxTrainFileName = os.path.join('DatasetBuilder','Input','sentiment')
		dataset = self.datasetBuilder.GetSentimentDatasetFromXLSXFile(xlsxTrainFileName)
		if backend:
			dataset2 = self.datasetBuilder.GetSentimentDatasetFromBackend()
			for item in dataset2:
				dataset[item] = dataset2[item]
		dataset = list(dataset.values())
		if len(dataset) < MIN_DATA:
			return
		print("Data length: ", len(dataset))
		self.languageModel.dataset = dataset
		self.languageModel.totalNumberOfDocs = len(dataset)
		self.languageModel.BuildLanguageModel()
		self.languageModel.dataset = []
		

		return dataset


	def prepare_data(self, dataset):
		trainFeaturesExtractor = FeaturesExtractor(self.configFileFeaturesExtractor, self.trainFeaturesSerializationFile, 
													self.trainLabelsSerializationFile, self.languageModel, dataset, 
													sentiment_features=True)
		trainFeaturesExtractor.ExtractNumTfFeatures(init_dicts())

		maxid = max([max(i.keys()) for i in trainFeaturesExtractor.features])

		X= []
		Y = []

		for i, item in enumerate(trainFeaturesExtractor.features):    
			itemx = [0 for _ in range(maxid)]
			l = [0,0,0]
			l[trainFeaturesExtractor.labels[i]-1] = 1

			for j in trainFeaturesExtractor.features[i]:
				v = trainFeaturesExtractor.features[i][j]
				itemx[j-1] = v

			X.append(itemx)
			Y.append(trainFeaturesExtractor.labels[i])
		trainFeaturesExtractor.dataset = []
		trainFeaturesExtractor.features = []
		trainFeaturesExtractor.labels = []
		return X, Y


	def transform_data(self, X, Y):
		X = np.array(X)
		Y = np.array(Y)

		ri = range(X.shape[0])
		rl = range(X.shape[1])

		d = pd.DataFrame(X, index=ri, columns=rl)

		d['class'] = Y

		return d


	def split_data(self, d):
		training_indices, testing_indices = train_test_split(d.index, stratify = d['class'].values, train_size=0.75, test_size=0.25)
		return training_indices, testing_indices


	def train(self, backend=True):
		rawdata = self.get_data(backend)
		dxy = self.prepare_data(rawdata)
		d = self.transform_data(dxy[0], dxy[1])
		self.training_indices, self.testing_indices = self.split_data(d)

		X = d.loc[self.training_indices].drop('class', axis=1).values
		Y = d.loc[self.training_indices, 'class'].values
		Xtest = d.loc[self.testing_indices].drop('class', axis=1).values
		Ytest = d.loc[self.testing_indices, 'class'].values
		if self.modeln == 1:
			print(self.fit_model1(X, Y))
			print(self.evaluate_model1(Xtest, Ytest))
		if self.modeln == 2:
			print(self.fit_model2(X, Y))
			print(self.evaluate_model2(Xtest, Ytest))
		if self.modeln == 3:
			print(self.fit_model3(X, Y))
			print(self.evaluate_model3(Xtest, Ytest))
		if self.modeln == 4:
			print(self.fit_model4(X, Y))
			print(self.evaluate_model4(Xtest, Ytest))


	def fit_model1(self, X, Y):
		self.model1 = LinearSVC(C=0.01, penalty="l1", dual=False, random_state=42)
		self.model1.fit(X, Y)
		recall = self.model1.score(X, Y)
		return recall


	def evaluate_model1(self, X, Y):
		evaluation = self.model1.score(X, Y)
		return evaluation


	def fit_model2(self, X, Y):
		self.model1 = LinearSVC(C=0.18, penalty="l1", dual=False, random_state=42)
		self.model1.fit(X, Y)
		recall = self.model1.score(X, Y)
		return recall


	def evaluate_model2(self, X, Y):
		evaluation = self.model1.score(X, Y)
		return evaluation


	def fit_model3(self, X, Y):
		pre_recall = 0.0
		for g in [0.01, 0.05, 0.1, 0.3, 0.5]:
			model = SVC(C=0.18, gamma=g, random_state=42)
			model.fit(X, Y)
			recall = model.score(X, Y)
			print(recall)
			if recall > pre_recall:
				pre_recall = recall
				self.model1 = model
		return recall


	def evaluate_model3(self, X, Y):
		evaluation = self.model1.score(X, Y)
		return evaluation

	def fit_model4(self, X, Y):
		model = SVC(C=0.18, gamma=0.1, random_state=42)
		model.fit(X, Y)
		recall = model.score(X, Y)
		self.model1 = model
		return recall


	def evaluate_model4(self, X, Y):
		evaluation = self.model1.score(X, Y)
		return evaluation


	def classify(self, tweets):
		dataset = []
		for tw in  tweets:
			dataset.append({'text': tw, 'label':'neutral'})
		X, Y = self.prepare_data(dataset)
		return self.model1.predict(X)


	@classmethod
	def load(cls, path):
		return pickle.load(open(path, 'rb'))


	
	def save(self, path):
		return pickle.dump(self, open(path, 'wb'))