import numpy as np
import pandas as pd

from sklearn.cross_validation import train_test_split
from sklearn.kernel_approximation import RBFSampler
from sklearn.svm import LinearSVC

# NOTE: Make sure that the class is labeled 'class' in the data file
tpot_data = pd.read_csv('PATH/TO/DATA/FILE', sep='COLUMN_SEPARATOR')
training_indices, testing_indices = train_test_split(tpot_data.index, stratify = tpot_data['class'].values, train_size=0.75, test_size=0.25)

result1 = tpot_data.copy()

# Perform classification with a LinearSVC classifier
lsvc1 = LinearSVC(C=0.18, penalty="l1", dual=False, random_state=42)
lsvc1.fit(result1.loc[training_indices].drop('class', axis=1).values, result1.loc[training_indices, 'class'].values)

result1['lsvc1-classification'] = lsvc1.predict(result1.drop('class', axis=1).values)

# Use Scikit-learn's RBFSampler to transform the feature set
training_features = result1.loc[training_indices].drop('class', axis=1)

if len(training_features.columns.values) > 0:
    # RBF must be fit on only the training data
    rbf = RBFSampler(gamma=0.18)
    rbf.fit(training_features.values.astype(np.float64))
    transformed_features = rbf.transform(result1.drop('class', axis=1).values.astype(np.float64))
    result2 = pd.DataFrame(data=transformed_features)
    result2['class'] = result1['class'].values
else:
    result2 = result1.copy()
