from DatasetBuilder.DatasetBuilder import DatasetBuilder
import os, pickle
import pandas as pd
from sklearn.cross_validation import train_test_split
from DatasetBuilder.DatasetBuilder import DatasetBuilder
from LanguageModel.LanguageModel import LanguageModel   
from FeaturesExtractor.FeaturesExtractor import FeaturesExtractor
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.feature_selection import RFE
from sklearn.svm import LinearSVC, SVC
from app import models
from datetime import datetime

MAX_DAYS = 2

class QuestionsModel(object):
	def __init__(self, words_dict_path=None, dataset_path = None, modeln = 1):
		if not words_dict_path:
			words_dict_path = os.path.join('data', 'questions_dict.bin')
		if not dataset_path:
			dataset_path = os.path.join('data', 'questions_dataset.bin')
		self.modeln = modeln
		self.words_dict_path = words_dict_path
		self.dataset_path = dataset_path
		configFileLanguageModel = os.path.join('LanguageModel', 'Configurations', 'Configurations_questions.xml')
		stopWordsFileName = os.path.join('LanguageModel', 'Input', 'stop_words.txt')
		linksDBFile = os.path.join('LanguageModel', 'Output', 'links_database.txt')
		languageModelSerializationFile = os.path.join('LanguageModel', 'Output', 'language_model.bin')


		self.languageModel = LanguageModel(configFileLanguageModel, stopWordsFileName, languageModelSerializationFile, linksDBFile, [])
		

		self.configFileFeaturesExtractor = os.path.join('FeaturesExtractor', 'Configurations', 'Configurations_questions.xml')
		self.trainFeaturesSerializationFile = os.path.join('FeaturesExtractor', 'Output', 'train_features.bin')
		self.trainLabelsSerializationFile = os.path.join('FeaturesExtractor', 'Output', 'train_labels.bin')

	def get_data(self):
		configFileDatasetBuilder = os.path.join('DatasetBuilder','Configurations','Configurations.xml')
		datasetSerializationFile = os.path.join('DatasetBuilder','Output', 'dataset.bin')

		self.datasetBuilder = DatasetBuilder(configFileDatasetBuilder, [], datasetSerializationFile)
		dataset = self.datasetBuilder.getQuestionsDataset(self.dataset_path)
		self.languageModel.dataset = dataset
		self.languageModel.totalNumberOfDocs = len(dataset)
		self.languageModel.BuildLanguageModel()
		self.languageModel.dataset = []
		return dataset


	def prepare_data(self, dataset):
		trainFeaturesExtractor = FeaturesExtractor(self.configFileFeaturesExtractor, self.trainFeaturesSerializationFile, 
													self.trainLabelsSerializationFile, self.languageModel, dataset, 
													questions_features=True)
		
		print("Data length: ", len(dataset))

		
		words_dict = self.datasetBuilder.getQuestionsDatasetDictionary(self.words_dict_path)
		trainFeaturesExtractor.ExtractNumTfFeatures(questions_dict=words_dict)

		maxid =  max([max(i.keys()) for i in trainFeaturesExtractor.features])

		X= []
		Y = []
		L = len(dataset)

		for i, item in enumerate(trainFeaturesExtractor.features):    
			itemx = [0 for _ in range(maxid)]
			l = [0,0,0]
			l[trainFeaturesExtractor.labels[i]-1] = 1

			for j in trainFeaturesExtractor.features[i]:
				v = trainFeaturesExtractor.features[i][j]
				itemx[j-1] = v

			X.append(itemx)
			Y.append(trainFeaturesExtractor.labels[i])

		return X, Y, L


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


	def train(self):
		rawdata = self.get_data()
		X, Y, L = self.prepare_data(rawdata)
		ret = [0,0]
		ret[0] = L
		d = self.transform_data(X, Y)
		self.training_indices, self.testing_indices = self.split_data(d)

		X = d.loc[self.training_indices].drop('class', axis=1).values
		Y = d.loc[self.training_indices, 'class'].values
		Xtest = d.loc[self.testing_indices].drop('class', axis=1).values
		Ytest = d.loc[self.testing_indices, 'class'].values
		if self.modeln == 1:
			print(self.fit_model1(X, Y))
			ret[1] = self.evaluate_model1(Xtest, Ytest)
			print(ret[1])
		if self.modeln == 2:
			print(self.fit_model2(X, Y))
			ret[1] = self.evaluate_model2(Xtest, Ytest)
			print(ret[1])
		if self.modeln == 3:
			print(self.fit_model3(X, Y))
			ret[1] = self.evaluate_model2(Xtest, Ytest)
			print(ret[1])

		return ret

	@classmethod
	def load(cls, path):
		return pickle.load(open(path, 'rb'))


	
	def save(self, path):
		return pickle.dump(self, open(path, 'wb'))


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



	def isQuestion(self, opinion):
		dataset = [{'text': opinion.text, 'label':'negativeq'}]
		X, Y, L = self.prepare_data(dataset)
		return self.model1.predict(X)[0]

	def addQuestion(self, opinion):
		q = models.QuestionOpinion()
		q.tweet = opinion
		q.since_id = opinion.twitter_id
		q.save()
		return q

	def checkQuestion(self, twitter, q):
		s = twitter.search(q='@' + q.tweet.tweeter.tweeter_name, count='500', result_type='mixed', since_id = q.since_id)
		replies = []

		for tw in s['statuses']:
			if tw['in_reply_to_status_id_str'] == str(q.tweet.twitter_id):
				replies.append(tw)
		diffdate = datetime.now() - q.date_created.replace(tzinfo=None)
		if diffdate.days > MAX_DAYS:
			q.delete()
		else:
			q.since_id = s['statuses'][0]['in_reply_to_status_id_str']
			q.save()
		return {"replies": replies, 'found': s['statuses']}


	def checkQuestions(self, twitter):
		for q in models.QuestionOpinion.objects.filter():
			self.checkQuestion(twitter, q)
