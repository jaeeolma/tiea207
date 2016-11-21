#-*- coding: utf8 -*-   

import csv as csv
import os

AGE_GROUPS = ['0-4', '5-9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80-84', '85-']

def get_male(year):
    if '2016' in year:
        year = '2015'
    path = os.path.join(os.path.dirname(__file__), '../data/vaesto_miehet.csv') 
    with open(path) as data:
        reader = csv.DictReader(data, delimiter=',')
        
        tulokset = []
        for row in reader:
            if year in row['Vuosi']:
                i = 0
                for column in reversed(reader.fieldnames):
                    count = row[column]
                    count = int(count)
                    tulokset.append(count)
        del tulokset[len(tulokset)-1]
        #print(tulokset)
        
    data.close()
    return tulokset
    
def get_female(year):
    if '2016' in year:
        year = '2015'
    path = os.path.join(os.path.dirname(__file__), '../data/vaesto_naiset.csv') 
    with open(path) as data:
        reader = csv.DictReader(data, delimiter=',')
        
        tulokset = []
        for row in reader:
            if year in row['Vuosi']:
                i = 0
                for column in reversed(reader.fieldnames):
                    count = row[column]
                    count = int(count)
                    tulokset.append(count)
        del tulokset[len(tulokset)-1]
        #print(tulokset)
    data.close()
    return tulokset

def combine(year):
    male = get_male(year)
    female = get_female(year)
    i = 0
    vaesto = []
    for id in AGE_GROUPS:
        cell = []
        cell.append(id)
        cell.append(male[i])
        cell.append(female[i])
        vaesto.append(cell)
        i = i+1
    #i = 0
    #for id in AGE_GROUPS:
     #   cell = []
      #  cell.append(id)
       # #cell.append(male[i])
        #cell.append(female[i])
        #vaesto.append(cell)
        #i = i+1
    return vaesto
   
#year = str(input('Anna vuosi: '))
#get_male(year)
#get_female(year)