'''
Created on Aug 7, 2014

@author: ASALLAB
'''

#REFERENCE:
#http://radimrehurek.com/gensim/tut3.html
from gensim import corpora, models, similarities


SIZE_OF_LANG_MODEL = 100

# TODO: convert the tweets from excel to text file

# Load the corpus
tweetCopus = corpora.textcorpus('all_tweets_filename.txt') #TODO: add file name

id2word = corpora.Dictionary.load_from_text('all_tweets_filename.txt')#TODO: add file name


lsi = models.LsiModel(corpus=tweetCopus, id2word=id2word, num_topics=SIZE_OF_LANG_MODEL)
#lsi.print_topics(10)

# Map the test sample
tweet = "this is a sample tweet"
vec_bow = corpora.Dictionary.doc2bow(tweet.lower().split())
vec_lsi = lsi[vec_bow]

# Match to simialrities
'''
To prepare for similarity queries, we need to enter all documents which we want to compare against subsequent queries. In our case, they are the same nine documents used for training LSI, converted to 2-D LSA space. But that’s only incidental, we might also be indexing a different corpus altogether
'''
index = similarities.MatrixSimilarity(lsi[tweetCopus]) # transform corpus to LSI space and index it
# Get simialor docs
sims = index[vec_lsi] # perform a similarity query against the corpus
print(list(enumerate(sims)))