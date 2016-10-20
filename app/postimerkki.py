
import csv
import os
import random


def merkin_url():
    vuodet_list = []
    vuosi_numero = random.randrange(1918,2014)
    etsittava_vuosi = str(vuosi_numero)
    path = os.path.join(os.path.dirname(__file__), 'static/merkit.csv')

    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if etsittava_vuosi in row['ilmestymispaiva']:
                 vuodet_list.append(row['kuvan_url'])
    osoite = random.choice(vuodet_list)
    return osoite
