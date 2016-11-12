
# coding: utf-8

# In[5]:

import pickle 
data = pickle.load(open('data/sent_dataset2.pkl','rb'))


# In[6]:



from tpot import TPOT
from sklearn.datasets import load_digits
from sklearn.cross_validation import train_test_split
import numpy 


X = numpy.array(data['X'])
Y = numpy.array(data['Y'])
X_train, X_test, y_train, y_test = train_test_split(X, Y,
                                                    train_size=0.75, test_size=0.25)
X_train.shape, X_test.shape, y_train.shape, y_test.shape


# In[ ]:



tpot = TPOT(generations=1, verbosity=2)
tpot.fit(X_train, y_train)
print(tpot.score(X_test, y_test))



# In[ ]:



tpot.export('sentiment_pipeline2.py')


"""
with open("/media/Data2/workspace/projects/kalamacom/sentiment_model_selection.py") as f:
    code = compile(f.read(), "/media/Data2/workspace/projects/kalamacom/sentiment_model_selection.py", 'exec')
    exec(code)

"""