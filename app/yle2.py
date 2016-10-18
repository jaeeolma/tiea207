import unicodecsv as csv
import random

def get_video_list(year)
	with open('C:/Kurssit/tiea207/tiea207/data/media.csv', 'rb') as media:
		reader = csv.DictReader(media, delimiter=',')
		year = input('Anna vuosi: ')
		tulokset = []
		for row in reader:
			if row['EMBED'] == '1' and year in row['FIRSTRUN']:
				tulokset.append(row['MID'])
		
		#try:
		#	mid = random.choice(tulokset)
		#except:
		#	mid = ''
			
	return tulokset

def get_video_url(mid)		
	with open('C:/Kurssit/tiea207/tiea207/data/media-article.csv', 'rb') as articlemedia:
		reader = csv.DictReader(articlemedia, delimiter=',')
		for row in reader:
			if row['MID'] == mid:
				aid = row['AID']
				break
		

	with open('C:/Kurssit/tiea207/tiea207/data/articles.csv', 'rb') as articles:
		reader = csv.DictReader(articles, delimiter=',')
		for row in reader:
			if row['AID'] == aid:
				url = row['URL']
				break
		
	return url