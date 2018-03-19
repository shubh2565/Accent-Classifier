from bs4 import BeautifulSoup
import requests
import urllib.request
import time
import pandas
import numpy



# getting the list of languages

languages = []
url = "http://accent.gmu.edu/browse_language.php"
r = requests.get(url)
c = r.content
soup = BeautifulSoup(c, 'html.parser')
print(soup.prettify())
language_lists = soup.findAll('ul', {'class': 'languagelist'})
    
for lan in language_lists:
	for lis in lan.findAll('li'):
		languages.append(lis.text)


# get the urls of all languages

urls = []
for language in languages:
	urls.append('http://accent.gmu.edu/browse_language.php?function=find&language=' + language)


# get the number of speakers for each language

num = []
maximum = 0
for url in urls:
	r = requests.get(url)
	c = r.content
	soup = BeautifulSoup(c, 'html.parser')
	test = soup.find_all('div', {'class': 'content'})
	try:
		num.append(int(test[0].find('h5').text.split()[2]))
		maximum = maximum + int(test[0].find('h5').text.split()[2])
	except AttributeError:
		num.append(0)



# get list of tuples (LANGUAGE, LANGUAGE_NUM_SPEAKERS) ignoring language with 0 speakers
language_num_speakers = []
for language, no in zip(languages, num):
	if num != 0:
		language_num_speakers.append((language, no))



# from the accent.gmu website, pass in list of languages to scrape mp3 files and save them to disk
for j in range(len(language_num_speakers)):
	for i in range(1,language_num_speakers[j][1]+1):
	 while True:
	 	try:
	 		urllib.request.urlretrieve("http://accent.gmu.edu/soundtracks/{0}{1}.mp3".format(lst[j][0], i), '{0}{1}.mp3'.format(lst[j][0], i))
	 	except:
	 		time.sleep(2)
	 	else:
	 		break



#Outputs: Pandas Dataframe containing speaker filename, birthplace, native_language, age, sex, age_onset of English

user_data = []
for n in range(maximum):
	info = {}
	url = "http://accent.gmu.edu/browse_language.php?function=detail&speakerid={}".format(n)
	html = get(url)
	soup = BeautifulSoup(html.content, 'html.parser')
	body = soup.find_all('div', {'class': 'content'})
	try:
		bio_bar = soup.find_all('ul', {'class':'bio'})
		info['age'] = float(bio_bar[0].find_all('li')[3].text.split()[2].strip(','))
		info['age_onset'] = float(bio_bar[0].find_all('li')[4].text.split()[4].strip())
		info['birthplace'] = str(bio_bar[0].find_all('li')[0].text)[13:-6]
		info['filename']=str(body[0].find('h5').text.split()[0])
		info['native_language'] = str(bio_bar[0].find_all('li')[1].text.split()[2])
		info['sex'] = str(bio_bar[0].find_all('li')[3].text.split()[3].strip())
		info['speakerid'] = n
		user_data.append(info)
	except:
		info['age'] = ''
		info['age_onset'] = ''
		info['birthplace'] = ''
		info['filename']= ''
		info['native_language'] = ''
		info['sex'] = ''
		info['speakerid'] = ''
		user_data.append(info)
            
        
df = pandas.DataFrame(user_data)
df.to_csv('speaker.csv')