import numpy as np
import pandas as pd

from sklearn.cross_validation import train_test_split
from sklearn.feature_selection import RFE
from sklearn.svm import LinearSVC, SVC

# NOTE: Make sure that the class is labeled 'class' in the data file
#tpot_data = pd.read_csv('PATH/TO/DATA/FILE', sep='COLUMN_SEPARATOR')

import pickle 
data = pickle.load(open('data/sent_dataset2.pkl','rb'))

X = np.array(data['X'])
Y = np.array(data['Y'])
ri = range(X.shape[0])
rl = range(X.shape[1])

d = pd.DataFrame(X, index=ri, columns=rl)

d['class'] = Y

result1 = d.copy()

training_indices, testing_indices = train_test_split(d.index, stratify = d['class'].values, train_size=0.75, test_size=0.25)

# Perform classification with a LinearSVC classifier
lsvc1 = LinearSVC(C=0.01, penalty="l1", dual=False, random_state=42)
lsvc1.fit(result1.loc[training_indices].drop('class', axis=1).values, result1.loc[training_indices, 'class'].values)

result1['lsvc1-classification'] = lsvc1.predict(result1.drop('class', axis=1).values)

# Use Scikit-learn's Recursive Feature Elimination (RFE) for feature selection
training_features = result1.loc[training_indices].drop('class', axis=1)
training_class_vals = result1.loc[training_indices, 'class'].values

if len(training_features.columns.values) == 0:
    result2 = result1.copy()
else:
    selector = RFE(SVC(kernel='linear'), n_features_to_eslect=min(18, len(training_features.columns)), step=0.99)
    selector.fit(training_features.values, training_class_vals)
    mask = selector.get_support(True)
    mask_cols = list(training_features.iloc[:, mask].columns) + ['class']
    result2 = result1[mask_cols]
