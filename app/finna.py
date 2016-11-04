#-*- coding: utf8 -*-

import requests
import random
import urllib

#Koodiin haettu voimakkaasti vaikutteita FinnaBotin koodista

FINNA_API_SEARCH='https://api.finna.fi/v1/search'
FINNA_RECORD_URL='https://www.finna.fi/record'
FINNA_IMAGE_URL='https://api.finna.fi'

IMAGE_MINSIZE_BYTES=1024
IMAGE_MAXSIZE_BYTES=1024*1024
IMAGE_MAXSIZE_SCALED=(1024,1024)

def transform_hit(hit):
    data = {}
    if 'title' in hit:
        data['title'] = hit['title']
    if 'images' in hit:
        data['image'] = hit['images'][0]
    if 'year' in hit:
        data['year'] = hit['year']
    data['id'] = hit['id']
    return data
    
def validate_result(result):
    if 'image' not in result:
        return False
    #if 'year' not in result:
    #    return False
    return True

def search_finna(year):
    fields = ['title', 'images', 'id', 'year']
    facet = 'era_facet:' + str(year)
    filters = ['format:0/Image/', 'online_boolean:1', facet]
    params = {'filter[]': filters, 'lookfor':'','lng':'fi','limit':100, 'field[]':fields, 'page':1} #maksimihakutulosmäärä on 100 per sivu :(
    r = requests.get(FINNA_API_SEARCH, params=params)
    response = r.json()
    if 'records' in response:
        results = [transform_hit(hit) for hit in response['records']]
        validated_results = filter(validate_result, results)
        if len(validated_results) > 0:
            return random.choice(validated_results)
        else:
            return None
    else:
        return None
        
def return_url(year):
    result = search_finna(year)
    if result is None:
        return '';
    imgurl = FINNA_IMAGE_URL + result['image']
    return imgurl
        
#year = input('anna vuosi: ')
#tulos = search_finna(year)
#imgurl = FINNA_IMAGE_URL + tulos['image']
#print(imgurl)

        