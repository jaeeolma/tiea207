from flask import Flask
from flask import render_template, request
from yle2 import get_video_list
from yle2 import get_video_url
from finna import return_url
from postimerkki import merkin_url
from postimerkki import merkin_tiedot
import os
import csv
import random
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


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
    if len(postimerkit) == 0:
        postimerkki_url = ''
    else:
        postimerkki_url = random.choice(postimerkit)
        postimerkki_tiedot = merkin_tiedot(postimerkki_url)
        postimerkki_nimi = postimerkki_tiedot[0]
        postimerkki_ilmestymispaiva = postimerkki_tiedot[1]
        

    finna_url = return_url(year)


    return render_template('base.html',
                           postimerkki_url=postimerkki_url,
                           url=url,
                           mid=mid,
                           finna_url=finna_url,
                           postimerkki_nimi=postimerkki_nimi,
                           postimerkki_ilmestymispaiva=postimerkki_ilmestymispaiva)


if __name__ == '__main__':
    app.run()
