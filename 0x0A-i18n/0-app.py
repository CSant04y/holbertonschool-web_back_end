#!/usr/bin/env python3
'''This Is the flask application'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def render_template():
    '''This renders the index.html template'''
    return render_template('templates/0-index.html')
