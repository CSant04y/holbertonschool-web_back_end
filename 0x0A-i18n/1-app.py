#!/usr/bin/env python3
'''This Is the flask application'''
from flask import Flask, render_template
from flask_babel import Babel
app = Flask(__name__)

babel = Babel(app)


class Config(object):
    '''langauge configuration class'''
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)
babel.default_local = 'en'
babel.default_timeszone = 'UTC'


@app.route('/', methods=['GET'])
def index():
    '''This renders the index.html template'''
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
