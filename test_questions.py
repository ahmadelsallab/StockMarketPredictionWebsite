import os
from QuestionsModel.QuestionsModel import QuestionsModel
from app import models
from twython import Twython


try:
	models.Tweeter.objects.get(tweeter_id='2147483647').delete()
except:
	pass

m = QuestionsModel()
m.train()

tweet_id = '764112768177958912'
#tweet_id = '746878093852291074'

twitter = Twython("MGMeNEK5bEqADjJRDJmQ8Yy1f", "eVR1kjrTdHPEiFuLoAEA6pPGSnuZ1NnAa1EwtqBi4wVA1tbRHo", "91079548-uhlRrwtgVQcavlf3lv4Dy1ZFCq5CXvBQFvc5A1l0n", "V6vLsqzqrdfs2YX4I1NVG2gP845gjTrBSDNxHVz496g66")


status = twitter.show_status(id=tweet_id)

tweeter = models.Tweeter()

tweeter.tweeter_id = status['user']['id']
tweeter.tweeter_followers_count = status['user']['followers_count']
tweeter.tweeter_followings_count = status['user']['friends_count']
tweeter.tweeter_profile_image_url = status['user']['profile_image_url_https']
tweeter.tweeter_location = status['user']['location']
tweeter.tweeter_name = status['user']['screen_name']
tweeter.tweeter_sname = status['user']['screen_name']
tweeter.tweeter_default_language = status['user']['lang']
tweeter.tweeter_time_zone = ''
tweeter.tweeter_gender = ''
tweeter.tweeter_age = 0
tweeter.tweeter_classification = ''




op = models.Opinion()

op.text = status['text']

op.twitter_id = status['id']
op.tweeter = tweeter


isq = m.isQuestion(op)

tweeter.save()
op.save()
if isq == 2:
	print(op.text , ' is a question...')
	q = m.addQuestion(op)
	re = m.checkQuestion(twitter, q)
	print('Replies to:', op.text, '\n==========================\n')
	for rr in re['replies']:
		print(rr['text'])



