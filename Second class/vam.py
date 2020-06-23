import numpy as np
from sklearn.neighbors import KNeighborsClassifier
'''In this example, we give the algorithm the costumer's data
   that if they give back the credit or not using Sklearn Library. '''
data = np.array([[1,3],
                [0,1],
                [1, 1.5],
                [1, 5],
                [0,2],
                [0,2.5]])

label = ['yes', 'no', 'yes', 'yes', 'no', 'no']

# Creating an object from data
clf = KNeighborsClassifier(n_neighbors=3)

clf.fit(data, label)
'''Fitting data to algorithm '''

out = clf.predict(np.array([[0, 2]]))
''' Predicting a new feature'''
print(out)
