import glob
import numpy as np
import pandas as pd
import scipy.io.wavfile
from scipy.fftpack import dct
import librosa
import librosa.display


filenames = glob.glob('/home/shubham/Accent/indian_accents_part1/*.wav')

features = []

for file in range(0,len(filenames)):
	y, sr = librosa.load(filenames[file])
	y = y[0:int(10 * sr)]
	mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
	mfcc = [j for i in mfccs for j in i]
	features.append(mfcc)


np.save('indian_accent_part1.npy', features)