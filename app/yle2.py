#-*- coding: utf8 -*-

import unicodecsv as csv
import random
import os

#Hakee medialistasta (tai ainakin pitäisi hakea) listan jossa vuoden embettävät mediaid:t

def get_video_list(year):
    path = os.path.join(os.path.dirname(__file__), '../data/media.csv')
    
    with open(path) as media:
        reader = csv.DictReader(media, delimiter=',')
        #year = input('Anna vuosi: ')
        results = []
        for row in reader:
            if row['EMBED'] == '1' and year in row['FIRSTRUN']:
                results.append(row['MID'])
        
        #try:
        #   mid = random.choice(results)
        #except:
        #   mid = ''
    media.close()
    return results
    
def get_video_url(mid): 
#Hakee mediaid:tä vastaavan artikkeliurl:n
    path = os.path.join(os.path.dirname(__file__), '../data/media-article.csv')
    with open(path) as articlemedia:
        reader = csv.DictReader(articlemedia, delimiter=',')
        for row in reader:
            if row['MID'] == mid:
                aid = row['AID']
                break
    
    articlemedia.close()
    path2 = os.path.join(os.path.dirname(__file__), '../data/articles.csv')
    with open(path2) as articles:
        reader = csv.DictReader(articles, delimiter=',')
        for row in reader:
            if row['AID'] == aid:
                url = row['URL']
                break
    
    articles.close()
    return url