#-*- coding: utf8 -*-   

import csv as csv
import os

AGE_GROUPS = ['0-4', '5-9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80-84', '85-']

#hakee taulusta väestöjakaumat ja palauttaa ne listoina

def get_male(year):
    if '2016' in year:
        year = '2015'
    path = os.path.join(os.path.dirname(__file__), '../data/vaesto_miehet.csv') 
    with open(path) as data:
        reader = csv.DictReader(data, delimiter=',')
        
        results = []
        for row in reader:
            if year in row['Vuosi']:
                i = 0
                for column in reversed(reader.fieldnames):
                    count = row[column]
                    count = int(count)
                    results.append(count)
        del results[len(results)-1]
        
    data.close()
    return results
    
def get_female(year):
    if '2016' in year:
        year = '2015'
    path = os.path.join(os.path.dirname(__file__), '../data/vaesto_naiset.csv') 
    with open(path) as data:
        reader = csv.DictReader(data, delimiter=',')
        
        results = []
        for row in reader:
            if year in row['Vuosi']:
                i = 0
                for column in reversed(reader.fieldnames):
                    count = row[column]
                    count = int(count)
                    results.append(count)
        del results[len(results)-1]
    data.close()
    return results
   
def get_population(year):
    path = os.path.join(os.path.dirname(__file__), '../data/vakimaara.csv')
    with open(path) as data:
        reader = csv.DictReader(data, delimiter=',')
        for row in reader:
            if year in row['Vuosi']:
                result = row['Väkiluku']
                break
    data.close()
    return result