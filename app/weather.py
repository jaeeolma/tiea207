#-*- coding: utf8 -*-   

import csv as csv
import os
import math

def get_temp(year, city):
    path = os.path.join(os.path.dirname(__file__), '../data/weather/' + city + '/' + year + '.csv')
    with open(path) as data:
        reader = csv.DictReader(data, delimiter=';')
        results = []
        for row in reader:
            count = row['measurement']
            count = float(count.replace(',', '.'))
            results.append(count)

    data.close()

    return results

#laskee keskilämpötilan vuoden arvoista
def get_monthly_temp(year, city):
    daily_temp = get_temp(year, city)
    monthly_temp = []
    if int(year) % 4 == 0:
        leap = 1
    else:
        leap = 0
    month = 1
    day = 0
    temp_sum = 0
    for temp in daily_temp:
        if month == 2 and leap == 1:
            tot_days = 29
        elif month == 2 and leap == 0:
            tot_days = 28
        elif month == 4 or month == 6 or month == 9 or month == 11:
            tot_days = 30
        else:
            tot_days = 31
        temp_sum += temp
        day += 1
        if day == tot_days:
            avg_temp = temp_sum / (day + 1)
            if math.isnan(avg_temp):
                monthly_temp.append('')
            else: 
                
                avg_temp = float(format(avg_temp, '.2f'))
                monthly_temp.append(avg_temp)
            day = 0
            temp_sum = 0
            if month == 12:
                break
            else:
                month += 1
        
    return monthly_temp
    
#year = raw_input("anna vuosi: ")
#city = raw_input("anna kaupunki: ")
#print(get_temp(year,city))
#print(get_monthly_temp(year, city))