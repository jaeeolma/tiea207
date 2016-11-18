
#-*- coding: utf8 -*-

from flask import Flask
from flask import render_template, request, Blueprint
from yle2 import get_video_list
from yle2 import get_video_url
from finna import search_finna
from postimerkki import merkin_url
from postimerkki import merkin_tiedot
from presidentti import hae_presidentti
from vaesto import *
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

AGE_GROUPS = ['0-4', '5-9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80-84', '85-']


app = Flask(__name__)

app.static_folder = 'static'

#ck = Blueprint('ck_page', __name__, static_folder=chartkick.js(), static_url_path='/static')
#app.register_blueprint(ck, url_prefix='/ck')
#app.jinja_env.add_extension("chartkick.ext.charts")

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
    
    chartID = 'vaesto'
    chart_type = 'bar'
    chart = {"renderTo": chartID, "type": chart_type}
    series = [{"name": 'Miehet', "data":get_male(year)},{"name":'Naiset', "data":get_female(year)}]
    title = {"useHTML":"true", "text":'Suomen väestörakenne vuonna ' + str(year)}
    xAxis = [{"categories": AGE_GROUPS, "reversed":"false", "labels":{"step":"1"}},{"opposite":"true", "reversed":"false", "categories":AGE_GROUPS, "linkedTo":"0","labels":{"step":"1"}}]
    yAxis = {"title":{"text":""}}
    plotOptions = {"series":{"stacking":"normal"}}
    tooltip = {"formatter": "function() {return '<b>' + this.series.name + ', age ' + this.point.category + '</b><br/>' + 'Population: ' + Highcharts.numberFormat(Math.abs(this.point.y), 0);}"}


    presidentin_tiedot = hae_presidentti(year)
    if len(presidentin_tiedot) == 0:
        presidentin_nimi = ''
        presidentin_kuva = ''
    else:
        presidentin_nimi = presidentin_tiedot[0]
        presidentin_kuva = presidentin_tiedot[1]

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
                           chartID = chartID,
                           chart = chart,
                           series = series,
                           title = title,
                           xAxis = xAxis,
                           yAxis = yAxis,
                           plotOptions = plotOptions,
                           tooltip = tooltip,
                           postimerkki_urlit = postimerkki_urlit,
                           postimerkki_tiedot = postimerkki_tiedot,
                           presidentin_kuva=presidentin_kuva,
                           presidentin_nimi=presidentin_nimi,
                           paaministeri_url=paaministeri_url,
                           paaministeri_nimi=paaministeri_nimi)

if __name__ == '__main__':
    app.run()
