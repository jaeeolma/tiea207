from flask import Flask
from flask import render_template
import os
import csv


app = Flask(__name__)

urltesti = 'moi'


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    return render_template('base.html',
                           url=urltesti)


if __name__ == '__main__':
    app.run()