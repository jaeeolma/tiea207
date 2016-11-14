from flask import Flask
from flask import render_template, request
from yle2 import get_video_list
from yle2 import get_video_url
from finna import search_finna
from postimerkki import merkin_url
from postimerkki import merkin_tiedot
from presidentti import hae_presidentti
from presidentti import hae_presidentin_nimi
from paaministerit import hae_paaministeri
import os
import csv
import random
import sys
import urllib
reload(sys)
sys.setdefaultencoding("utf-8")

FINNA_RECORD_URL='https://www.finna.fi/Record/'
FINNA_IMAGE_URL='https://api.finna.fi'

app = Flask(__name__)

app.static_folder = 'static'


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    try:
        year = request.form['year']
    except:
        year = '1962'

    tulokset = get_video_list(year)
    if len(tulokset) == 0:
        mid = ''
        url = ''
    else:
        mid = random.choice(tulokset)
        url = get_video_url(mid)

    postimerkit = merkin_url(year)
    postimerkki_urlit = []
    postimerkki_tiedot = []
    if len(postimerkit) == 0:
        postimerkki_urlit.append('')
        postimerkki_url = ''
    else:
        for x in range(0, 4):
            postimerkki_url = random.choice(postimerkit)
            if (postimerkki_url not in postimerkki_urlit):
                postimerkki_urlit.append(postimerkki_url)
                url_tiedot = merkin_tiedot(postimerkki_url)
                postimerkki_tiedot = postimerkki_tiedot + url_tiedot
        
    finnaresult = search_finna(year)
    finna_kuva = FINNA_IMAGE_URL + finnaresult['image']
    finna_record = FINNA_RECORD_URL + urllib.quote(finnaresult['id'])

    finna_title = finnaresult['title']
    finna_source = finnaresult['building']
    

    presidentin_kuva = hae_presidentti(year)
    presidentin_nimi = hae_presidentin_nimi(year)

    paaministerin_tiedot = hae_paaministeri(year)
    if len(paaministerin_tiedot) == 0:
        paaministeri_nimi = ''
        paaministeri_url = ''
    else:
        paaministeri_nimi = paaministerin_tiedot[0]
        paaministeri_url = paaministerin_tiedot[1]


    return render_template('base.html',
                           postimerkki_url=postimerkki_url,
                           areena_url=url,
                           areena_mid=mid,
                           finna_kuva=finna_kuva,
                           finna_record = finna_record,
                           finna_title = finna_title,
                           finna_source = finna_source,
                           year=year,
                           postimerkki_urlit = postimerkki_urlit,
                           postimerkki_tiedot = postimerkki_tiedot,
                           presidentin_kuva=presidentin_kuva,
                           presidentin_nimi=presidentin_nimi,
                           paaministeri_url=paaministeri_url,
                           paaministeri_nimi=paaministeri_nimi)

if __name__ == '__main__':
    app.run()
