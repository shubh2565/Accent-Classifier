import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

dataset1 = np.load('spanish_male.npy')
dataset2 = np.load('spanish_female.npy')
dataset3 = np.load('usa_male.npy')
dataset4 = np.load('usa_female.npy')
dataset5 = np.load('indian_accent_part1.npy')
dataset6 = np.load('indian_accent_part2.npy')
dataset7 = np.load('uk_accent.npy')


#features = np.concatenate((dataset1,dataset2,dataset3,dataset4), axis=0)
features = np.concatenate((dataset3, dataset4, dataset5, dataset6), axis=0)

X = features



y = np.concatenate((np.zeros(361), np.ones(194)), axis=0)



#splitting the dataset into training and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


#feature scaling so that no variable dominates over the other(s)
from sklearn.preprocessing import StandardScaler
feature = StandardScaler()
X_train = feature.fit_transform(X_train)
X_test = feature.transform(X_test)


#applying Principal Component Analysis
from sklearn.decomposition import KernelPCA
kpca = KernelPCA(n_components = 2)
X_train = kpca.fit_transform(X_train)
X_test = kpca.transform(X_test)
#explained_variance = pca.explained_variance_ratio_
#print('\n\nExplained Variance Ratio:\n{}'.format(explained_variance))



#fitting logistic regression model and predicting the test set results
# from sklearn.linear_model import LogisticRegression
# classifier = LogisticRegression(random_state=0)
# classifier.fit(X_train, y_train)
# y_pred = classifier.predict(X_test)


#fitting kernel SVM model and predicting the test set results
from sklearn.svm import SVC
classifier = SVC(kernel = 'linear', random_state=0,  C=1)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)


#making confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print('\nConfusion Matrix :\n{}'.format(cm))




#applying grid search
from sklearn.model_selection import GridSearchCV
parameters = [{'C' : [1,10,100,1000], 'kernel' : ['linear']},{'C' : [1,10,100,1000], 'kernel' : ['rbf'], 'gamma' : [0.5,0.1,0.01,0.001]}]
grid_search = GridSearchCV(estimator=classifier,
	param_grid=parameters,
	scoring='accuracy',
	cv=10,
	n_jobs=-1)
grid_search = grid_search.fit(X_train,y_train)
best_accuracy = grid_search.best_score_
print('\nBest Accuracy : \n{}'.format(best_accuracy))
best_parameters = grid_search.best_params_
print('\nBest Parameters : \n{}'.format(best_parameters))
