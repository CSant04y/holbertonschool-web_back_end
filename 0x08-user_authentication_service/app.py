#!/usr/bin/env python3
"""This is another basic Flask Application
"""
from flask import Flask, jsonify, request
from werkzeug.exceptions import NotFound
from auth import Auth


AUTH = Auth()

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome():
    '''Returns Json Payload'''
    return jsonify({"message": "Bienvenue"}), 200


@app.route('/users', methods=['POST'])
def register_user():
    '''This method registers the user using a POST request'''
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == '__main__':
    app.run()
