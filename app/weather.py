#-*- coding: utf8 -*-   

import csv as csv
import os

def get_temp(year, city):
    path = os.path.join(os.path.dirname(__file__), '../data/weather/' + city + '/' + year + '.csv')
    with open(path) as data:
        reader = csv.DictReader(data, delimiter=';')
        results = []
        for row in reader:
            results.append(row['measurement'])

    data.close()
    return results