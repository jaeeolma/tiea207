#-*- coding: utf8 -*-   

import csv as csv
import os

def get_temp(year, city):
    path = os.path.join(os.path.dirname(__file__), '../data/weather/' + city + '/' + year + '.csv')
    with open(path) as data:
        reader = csv.DictReader(data, delimiter=';')
        results = []
        for row in reader:
            count = row['measurement']
            count = float(count)
            results.append(count)

    data.close()

    return results
    
#year = input("anna vuosi: ")
#city = raw_input("anna kaupunki: ")
#print(year)
#print(city)
#for n in get_temp(str(year), str(city)):
#    print(n)