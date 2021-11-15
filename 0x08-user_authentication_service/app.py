#!/usr/bin/env python3
"""This is another basic Flask Application
"""
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome():
    '''Returns Json Payload'''
    return jsonify({"message": "Bienvenue"}), 200


if __name__ == '__main__':
    app.run()
