import os
import random
import urllib, json


url = 'https://api.finna.fi/v1/search?type[]=year:%222001%22&filter[]=online_boolean:%221%22&filter[]=format:%220/Image/%22&page=100'
data = json.load(urllib.urlopen(url))
print data
    










