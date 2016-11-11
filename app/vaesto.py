#-*- coding: utf8 -*-   

import csv as csv
import os

def get_male(year): 
    path = os.path.join(os.path.dirname(__file__), '../data/vaesto_miehet.csv') 
    with open(path) as data:
        reader = csv.DictReader(data, delimiter=',')
        
        tulokset = []
        for row in reader:
            if year in row['Vuosi']:
                for column in reader.fieldnames:
                    tulokset.append(row[column])
        del tulokset[0]
        print(tulokset)
    data.close()
    #return tulokset
    
def get_female(year): 
    path = os.path.join(os.path.dirname(__file__), '../data/vaesto_naiset.csv') 
    with open(path) as data:
        reader = csv.DictReader(data, delimiter=',')
        
        tulokset = []
        for row in reader:
            if year in row['Vuosi']:
                for column in reader.fieldnames:
                    tulokset.append(row[column])
        del tulokset[0]
        print(tulokset)
    data.close()
    #return tulokset

year = str(input('Anna vuosi: '))
get_male(year)
get_female(year)