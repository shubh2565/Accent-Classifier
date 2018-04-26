import experiment1 as module1
import serial
import time

from importlib import reload




import librosa
from numpy  import array, reshape


s = serial.Serial("/dev/ttyACM1", 9600)       #port is 11 (for COM12), and baud rate is 9600
time.sleep(2)                                 #wait for the Serial to initialize
s.write('Ready...'.encode())


choice = 'y'

while choice is 'y':

	
	if 'record_audio' in dir():
		reload(record_audio)
	else:
		import record_audio

	y, sr = librosa.load('/home/shubham/Accent/file.wav')
	y = y[0:int(10 * sr)]
	mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
	mfcc = [j for i in mfccs for j in i]
	mfcc = array( mfcc )
	mfcc = mfcc.reshape(1, -1)
	mfcc = module1.feature.transform(mfcc)
	mfcc_pca = module1.kpca.transform(mfcc)
	answer = module1.classifier.predict(mfcc_pca)
	if answer > 0.5:

		#str = 'Indian Accent   '
		#s.write(str.encode())
		#time.sleep(3)
		#str = ''

		str2 = 'A'
		s.write(str2.encode())

		#if 'speech_to_text' in dir():
		#	reload(speech_to_text)
		#	str = str + speech_to_text.text
		#	chunks, chunk_size = len(str), 16
		#	sentence = [ str[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
		#	for i in range(len(sentence)):
		#		s.write(sentence[i].encode())
		#		time.sleep(1.6)
		#else:
		#	import speech_to_text
		#	str = str + speech_to_text.text
		#	chunks, chunk_size = len(str), 16
		#	sentence = [ str[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
		#	for i in range(len(sentence)):
		#		s.write(sentence[i].encode())
		#		time.sleep(1.6)

	else:
		#str = 'American Accent '
		#s.write(str.encode())
		#time.sleep(3)

		str2 = 'B'
		s.write(str2.encode())

	choice = input('Do you want to test again (y/n) : ')