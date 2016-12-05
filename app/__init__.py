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
from weather import *
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
VUOSI = 1962

AGE_GROUPS = ['85-', '80-84', '75-79', '70-74', '65-69', '60-64', '55-59', '50-54', '45-49', '40-44', '35-39', '30-34', '25-29', '20-24', '15-19', '10-14', '5-9', '0-4']


app = Flask(__name__)

app.static_folder = 'static'

#ck = Blueprint('ck_page', __name__, static_folder=chartkick.js(), static_url_path='/static')
#app.register_blueprint(ck, url_prefix='/ck')
#app.jinja_env.add_extension("chartkick.ext.charts")

#@app.before_first_request
def update_files():
    articles = 'http://elavaarkisto.kokeile.yle.fi/data/articles.csv'
    mediaarticle = 'http://elavaarkisto.kokeile.yle.fi/data/media-article.csv'
    media = 'http://elavaarkisto.kokeile.yle.fi/data/media.csv'
    path = os.path.join(os.path.dirname(__file__), '../data/articles.csv')
    urllib.urlretrieve(articles, path)
    path = os.path.join(os.path.dirname(__file__), '../data/media-article.csv')
    urllib.urlretrieve(mediaarticle, path)
    path = os.path.join(os.path.dirname(__file__), '../data/media.csv')
    urllib.urlretrieve(media, path)

@app.route('/', methods=['POST', 'GET'])
def faktat():
    try:
        year = request.form['year']
        global VUOSI
        VUOSI = year
    except:
        year = str(VUOSI)

    #väestötaulukon luominen
    chartID = 'vaesto'
    chart_type = 'bar'
    chart = {"renderTo": chartID, "type": chart_type}
    series = [{"name": 'Miehet', "data":get_male(year)},{"name":'Naiset', "data":get_female(year)}]
    #title = {"useHTML":"true", "text": "Suomen väestörakenne vuonna " + str(year) }
    title = {"text":""}
    xAxis = [{"categories": AGE_GROUPS, "reversed":"false", "labels":{"step":"1"}},{"opposite":"true", "reversed":"false", "categories":AGE_GROUPS, "linkedTo":"0","labels":{"step":"1"}}]
    #yAxis = {"title":{"text":"Suomalaisia " + get_population(year)}}
    yAxis = {}
    plotOptions = {"series":{"stacking":"normal"}}
    #plotOptions = {}
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
        
    #säädata
    months = ['Tammikuu', 'Helmikuu', 'Maaliskuu', 'Huhtikuu', 'Toukokuu', 'Kesäkuu', 'Heinäkuu', 'Elokuu', 'Syyskuu', 'Lokakuu', 'Marraskuu', 'Joulukuu']
    
    weatherChartID = 'weather'
    weatherchart = {"renderTo":weatherChartID}
    weather_xAxis =[{"categories": months}]
    weather_title = {"text":""}
    weather_yAxis = {"title":{"text":""}, "plotlines":[{"value":'0', "width":'1', "color":'#808080'}]}
    weather_tooltip = {}
    weather_legend = {"layout":'vertical', "align":'right', "verticalAlign":'middle', "borderWidth":'0'}
    weather_series = [{"name":'Kaisaniemi, Helsinki', "data":get_monthly_temp(year, 'hki')},{"name":'Sodankyla', "data":get_monthly_temp(year, 'sod')}]


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
                           paaministeri_nimi=paaministeri_nimi,
                           weatherChartID = weatherChartID,
                           weatherchart = weatherchart,
                           weather_title = weather_title,
                           weather_xAxis = weather_xAxis,
                           weather_yAxis = weather_yAxis,
                           weather_tooltip = weather_tooltip,
                           weather_legend = weather_legend,
                           weather_series = weather_series)

@app.route('/kuvat', methods=['POST', 'GET'])
def kuvat():
    try:
        year = request.form['year']
        global VUOSI
        VUOSI = year
    except:
        year = str(VUOSI)


    # postimerkkien tulokset
    postimerkit = merkin_url(year)
    postimerkki_urlit = []
    postimerkki_tiedot = []
    if len(postimerkit) == None:
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

    #finnan tulokset
    finna_kuvat = []
    finna_records = []
    finna_titles = []
    finna_sources = []
    finnaresult_list = search_finna(year)
    #finna_kuva = FINNA_IMAGE_URL + finnaresult['image']
    #finna_record = FINNA_RECORD_URL + urllib.quote(finnaresult['id'])
    #finna_title = finnaresult['title']
    #finna_source = finnaresult['building']
    for x in range(len(postimerkit)+1):
        finnaresult = random.choice(finnaresult_list)
        if (finnaresult not in finna_kuvat):
            finna_kuvat.append(FINNA_IMAGE_URL + finnaresult['image'])
            finna_records.append(FINNA_RECORD_URL + urllib.quote(finnaresult['id']))
            finna_titles.append(finnaresult['title'])
            finna_sources.append(finnaresult['building'])
        else:
            x + 1


    return render_template('kuvat.html',
                           #postimerkki_urlit=postimerkki_urlit,
                           postimerkki_urlit=postimerkit,
                           postimerkki_tiedot=postimerkki_tiedot,
                           finna_kuva=finna_kuvat,
                           finna_record=finna_records,
                           finna_title=finna_titles,
                           finna_source=finna_sources,
                           year=year)

@app.route('/videot', methods=['POST', 'GET'])
def videot():
    try:
        year = request.form['year']
        global VUOSI
        VUOSI = year
    except:
        year = str(VUOSI)

    mid_list = []
    url_list = []
    x = 0

    #Elävän arkiston tulokset
    tulokset = get_video_list(year)
    if len(tulokset) == None:
        mid_list.append('')
        url_list.append('')
    else:
        while (len(mid_list) < 8 or x == 15):
            mid = random.choice(tulokset)
            if (mid not in mid_list):
                mid_list.append(mid)
                url = get_video_url(mid)
                url_list.append(url)
                x + 1

    return render_template('videot.html',
                           areena_url=url_list,
                           areena_mid=mid_list,
                           year=year)

                           
@app.route('/pelle', methods=['GET'])
def pelle():
    pellet = ['26-20232', '26-23794', '26-23771', '26-22033', '26-20223', '26-47064', '26-47079', '26-96928', '26-20226', '26-20209', '26-20220', '26-4144']
    mid = random.choice(pellet)
    url = get_video_url(mid)
    
    return render_template('pelle.html', areena_url=url, areena_mid=mid)
    
@app.route('/about', methods=['POST', 'GET'])
def about():
    try:
        year = request.form['year']
        global VUOSI
        VUOSI = year
    except:
        year = str(VUOSI)
        
    return render_template('about.html', year=year)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)

    
