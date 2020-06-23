import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

my_dataset = np.loadtxt("iris.csv", delimiter=",", dtype="str")
''' delimiter = what is the separator'''

features = my_dataset[1:, :4]
# Starting from 1 is because the first column is details

features = np.array(features, dtype=np.float32)
# Converting features from str to float

label = my_dataset[1:, 4]

X_train, X_test, y_train, y_test = train_test_split(features,
                                                    label,
                                                    test_size=0.33)
''' train_test_split(features, labels, test size)'''

clf = KNeighborsClassifier()

clf.fit(X_train, y_train)

score = clf.score(X_test, y_test)

evaluate = np.array([[2.7, 3.0, 1.2, 10.3],
                     [4.1, 3.3, 0.4, 1.5]])

out = clf.predict(evaluate)

print(out)

print(score)
