#!/usr/bin/env python3
'''This Is the flask application'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def render_template():
    '''This renders the index.html template'''
    return render_template('templates/0-index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
