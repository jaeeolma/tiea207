
import csv
import os
import random


def merkin_url(year):
    vuodet_list = []
    vuosi_numero = year
    etsittava_vuosi = str(vuosi_numero)
    path = os.path.join(os.path.dirname(__file__), '../data/postimerkit2014.csv')

    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if etsittava_vuosi in row['ilmestymispaiva']:
                 vuodet_list.append(row['kuvan_url'])
    return vuodet_list

def merkin_nimi(url):
    url_list = []
    etsittava_url = str(url)
    path = os.path.join(os.path.dirname(__file__), '../data/postimerkit2014.csv')

    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if etsittava_url in row['kuvan_url']:
                 url_list.append(row['kuvan_url'])
    return url_list