
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

AGE_GROUPS = ['85-', '80-84', '75-79', '70-74', '65-69', '60-64', '55-59', '50-54', '45-49', '40-44', '35-39', '30-34', '25-29', '20-24', '15-19', '10-14', '5-9', '0-4']


app = Flask(__name__)

app.static_folder = 'static'

#ck = Blueprint('ck_page', __name__, static_folder=chartkick.js(), static_url_path='/static')
#app.register_blueprint(ck, url_prefix='/ck')
#app.jinja_env.add_extension("chartkick.ext.charts")

@app.route('/', methods=['POST', 'GET'])
def faktat():
    try:
        year = request.form['year']
    except:
        year = '1962'
    
    #väestötaulukon luominen
    chartID = 'vaesto'
    chart_type = 'bar'
    chart = {"renderTo": chartID, "type": chart_type}
    series = [{"name": 'Miehet', "data":get_male(year)},{"name":'Naiset', "data":get_female(year)}]
    #title = {"useHTML":"true", "text": "Suomen väestörakenne vuonna " + str(year) }
    title = {"text":""}
    xAxis = [{"categories": AGE_GROUPS, "reversed":"true", "labels":{"step":"1"}},{"opposite":"false", "reversed":"true", "categories":AGE_GROUPS, "linkedTo":"0","labels":{"step":"1"}}]
    yAxis = {"title":{"text":"Kansalaisia " + get_population(year)}}
    #plotOptions = {"series":{"stacking":"normal"}}
    plotOptions = {}
    tooltip = {}
    #tooltip = {"formatter": "function() {return '<b>' + this.series.name + ', age ' + this.point.category + '</b><br/>' + 'Population: ' + Highcharts.numberFormat(Math.abs(this.point.y), 0);}"}

    #presidenttihaku
    presidentin_tiedot = hae_presidentti(year)
    if len(presidentin_tiedot) == 0:
        presidentin_nimi = ''
        presidentin_kuva = ''
    else:
        presidentin_nimi = presidentin_tiedot[0]
        presidentin_kuva = presidentin_tiedot[1]

    #pääministerihaku
    paaministerin_tiedot = hae_paaministeri(year)
    if len(paaministerin_tiedot) == 0:
        paaministeri_nimi = ''
        paaministeri_url = ''
    else:
        paaministeri_nimi = paaministerin_tiedot[0]
        paaministeri_url = paaministerin_tiedot[1]


    return render_template('faktat.html',
                           year=year,
                           chartID = chartID,
                           chart = chart,
                           series = series,
                           title = title,
                           xAxis = xAxis,
                           yAxis = yAxis,
                           plotOptions = plotOptions,
                           tooltip = tooltip,
                           presidentin_kuva=presidentin_kuva,
                           presidentin_nimi=presidentin_nimi,
                           paaministeri_url=paaministeri_url,
                           paaministeri_nimi=paaministeri_nimi)

@app.route('/kuvat', methods=['POST', 'GET'])
def kuvat():
    try:
        year = request.form['year']
    except:
        year = '1962'

    #finnan tulokset
    finnaresult = search_finna(year)
    finna_kuva = FINNA_IMAGE_URL + finnaresult['image']
    finna_record = FINNA_RECORD_URL + urllib.quote(finnaresult['id'])
    finna_title = finnaresult['title']
    finna_source = finnaresult['building']

    # postimerkkien tulokset
    postimerkit = merkin_url(year)
    postimerkki_urlit = []
    postimerkki_tiedot = []
    if len(postimerkit) == 0:
        postimerkki_urlit.append('')
    else:
        for x in range(len(postimerkit)):
            url_tiedot = merkin_tiedot(postimerkit[x])
            postimerkki_tiedot = postimerkki_tiedot + url_tiedot

       # for x in range(0, 4):
       #     postimerkki_url = random.choice(postimerkit)
       #     if (postimerkki_url not in postimerkki_urlit):
       #         postimerkki_urlit.append(postimerkki_url)
       #         url_tiedot = merkin_tiedot(postimerkki_url)
       #         postimerkki_tiedot = postimerkki_tiedot + url_tiedot


    return render_template('kuvat.html',
                           #postimerkki_urlit=postimerkki_urlit,
                           postimerkki_urlit=postimerkit,
                           postimerkki_tiedot=postimerkki_tiedot,
                           finna_kuva=finna_kuva,
                           finna_record=finna_record,
                           finna_title=finna_title,
                           finna_source=finna_source,
                           year=year)

@app.route('/videot', methods=['POST', 'GET'])
def videot():
    try:
        year = request.form['year']
    except:
        year = '1962'

    #Elävän arkiston tulokset
    tulokset = get_video_list(year)
    if len(tulokset) == 0:
        mid = ''
        url = ''
    else:
        mid = random.choice(tulokset)
        url = get_video_url(mid)

    return render_template('videot.html',
                           areena_url=url,
                           areena_mid=mid,
                           year=year)

if __name__ == '__main__':
    app.run(debug=True)
