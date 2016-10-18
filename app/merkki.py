import pandas as pd 
import random

#atm toimii vain konsolissa
while True:
	merkit = pd.read_csv('static/postimerkit2014.csv')
	year = input("Anna vuosi: ")
	try: 
		merkki = random.choice(list(merkit[merkit.ilmestymispaiva.str.contains(year)].kuvan_url))
		break
	except IndexError:
		print("Ei merkkejä vuodelta, valitse uudestaan.")
		
print(merkki)