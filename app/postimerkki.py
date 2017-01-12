
import csv
import os
import random
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# Hakee postimerkin urlin postimerkit csv:sta vuoden perusteella
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

# Hakee halutut tiedot postimerkista postimerkin urlin perusteella
def merkin_tiedot(url):
    tiedot_list = []
    etsittava_url = str(url)
    path = os.path.join(os.path.dirname(__file__), '../data/postimerkit2014.csv')

    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if etsittava_url in row['kuvan_url']:
                tiedot_list.append(row['merkin_nimi'])
    return tiedot_list