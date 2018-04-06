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
features = np.concatenate((dataset3, dataset4, dataset7, dataset8), axis=0)



X = features


#y = np.append(np.ones(162), np.zeros(361))
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
classifier.add(Dense(units=1, kernel_initializer='glorot_uniform',activation='sigmoid'))

#compiling the ANN
classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

#fitting the ANN to traing set
classifier.fit(X_train, y_train, batch_size=8, epochs=100)

#prediction
y_pred = classifier.predict(X_test)
y_pred =(y_pred > 0.5)

#confusion matrix
cm = confusion_matrix(y_test, y_pred)
print('\n\nConfusion Matrix:\n{}\n\n'.format(cm))


'''
# test time
import librosa
from numpy  import array, reshape



y, sr = librosa.load('/home/shubham/Accent/file.wav')
y = y[0:int(10 * sr)]
mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
mfcc = [j for i in mfccs for j in i]
mfcc = array( mfcc )
mfcc = mfcc.reshape(1, -1)
mfcc = feature.transform(mfcc)
mfcc_pca = kpca.transform(mfcc)
answer = classifier.predict(mfcc_pca)
print(answer)


if answer > 0.5:
	print('Indian Accent')
else:
	print('American Accent')


'''