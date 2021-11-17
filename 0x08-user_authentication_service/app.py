#!/usr/bin/env python3
"""This is another basic Flask Application
"""
from flask import Flask, jsonify, request, abort, redirect
from sqlalchemy.sql.functions import user
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome():
    '''Returns Json Payload'''
    return jsonify({"message": "Bienvenue"}), 200


@app.route('/users', methods=['POST'], strict_slashes=False)
def register_user() -> str:
    '''This method registers the user using a POST request'''
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """
    This is a login function
    """
    email = request.form.get('email')
    password = request.form.get('password')

    valid_login = AUTH.valid_login(email, password)

    if valid_login:
        session_id = AUTH.create_session(email)
        message = {"email": "<user email>", "message": "logged in"}
        response = jsonify(message)
        response.set_cookie('session_id', session_id)

        return response
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """This logs out the user"""
    session_id = request.cookies.get('session_id')
    logged_user = AUTH.get_user_from_session_id(session_id)

    if not logged_user:
        abort(403)

    AUTH.destroy_session(logged_user.id)
    return redirect('/')


if __name__ == '__main__':
    app.run()
