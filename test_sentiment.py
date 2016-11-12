import os
from SentimentModel.SentimentModel import SentimentModel
from app import models


m = SentimentModel(modeln=4)
m.train(backend=True)
tweets = [
	'البنك الهولندي من فرص السوق الكبيرة جدا أرباح قوية وسيمنح سهم لكل سهم سعر السهم وصل قبل فترة الى ٤٩ ريال', 
	'RT @NefaieIG: تعلن شركة"اسمنت اليمامه"توصية مجلس ادارتها بتوزيع ارباح نقدية عن الربع الثالث للعام المالي 2015 https://t.co/l0DjGeCgMV #الن…',
	'سهم كيان اليوم كان الأكثر ضغطاً على المؤشر العام، وكذلك الأكثر انخفاضاً، ويقع ضمن قائمة الأسهم الأكثر صافي سيولة منخفض #تداول #تاسي'
]


path = os.path.join('data', 'SentimentModel.bin')


m.save(path)

m2 = SentimentModel.load(path)

clss = m2.classify(tweets)


labels = ['negative', 'positive', 'neutral']
for i, tw in  enumerate(tweets):
	print('tweet: ', tw)
	print('sentiment: ', labels[clss[i] - 1])




