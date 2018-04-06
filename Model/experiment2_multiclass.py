import numpy as np
import pandas as pd


dataset1 = np.load('spanish_female.npy')
dataset2 = np.load('spanish_male.npy')
dataset3 = np.load('usa_female.npy')
dataset4 = np.load('usa_male.npy')
dataset5 = np.load('arabic_female.npy')
dataset6 = np.load('arabic_male.npy')
dataset7 = np.load('indian_accent_part1.npy')
dataset8 = np.load('indian_accent_part2.npy')
dataset9 = np.load('uk_accent.npy')


#features = np.concatenate((dataset1,dataset2,dataset3,dataset4), axis=0)
features = np.concatenate((dataset1, dataset2, dataset3, dataset4, dataset7, dataset8), axis=0)



X = features


#y = np.append(np.ones(162), np.zeros(361))
y = np.concatenate((2*np.ones(162), np.zeros(361), np.ones(194)), axis=0)

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from keras.utils import np_utils
# label_y = LabelEncoder()
# y = label_y.fit_transform(y)
# encode = OneHotEncoder(categorical_features=[3])
# y = encode.fit_transform(y).toarray()
encoder = LabelEncoder()
encoder.fit(y)
encoded_y = encoder.transform(y)
# convert integers to dummy variables (i.e. one hot encoded)
y = np_utils.to_categorical(encoded_y)

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
kpca = KernelPCA(n_components = 13, kernel='rbf')
X_train = kpca.fit_transform(X_train)
X_test = kpca.transform(X_test)





import keras
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import confusion_matrix



#initializing the ANN and adding input and first hidden layer
classifier = Sequential()
classifier.add(Dense(units=6, kernel_initializer='glorot_uniform',activation='relu',input_dim=13))

#adding second and third hidden layer
classifier.add(Dense(units=6, kernel_initializer='glorot_uniform',activation='relu'))
classifier.add(Dense(units=6, kernel_initializer='glorot_uniform',activation='relu'))



#adding output layer
classifier.add(Dense(units=3, kernel_initializer='glorot_uniform',activation='softmax'))

#compiling the ANN
classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

#fitting the ANN to traing set
classifier.fit(X_train, y_train, batch_size=8, epochs=400)

#some changes required for getting confusion matrix

#prediction
y_pred = classifier.predict(X_test)
y_pred =(y_pred > 0.5)

#confusion matrix
cm = confusion_matrix(y_test, y_pred)
print('\n\nConfusion Matrix:\n{}\n\n'.format(cm))
