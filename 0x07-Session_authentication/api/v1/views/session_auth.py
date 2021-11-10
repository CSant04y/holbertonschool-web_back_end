#!/usr/bin/env python3
""" Module of Session Auth
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv


@app_views.route("/auth_session/login", methods=['POST'], strict_slashes=False)
def login():
    """Login Method"""

    email = request.form.get("email")
    password = request.form.get("password")

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400
    users = User.search({"email": email})

    if not users:
        return jsonify(error="no user found for this email"), 404

    for user in users:
        if not user.is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401

        else:
            from api.v1.app import auth
            session_id = auth.create_session(user.id)
            sesion_name = getenv("SESSION_NAME")
            user_dict = jsonify(user.to_json())
            user_dict.set_cookie(sesion_name, session_id)
            return user_dict


@app_views.route("/auth_session/logout", methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """logout"""
    from api.v1.app import auth
    destroy_session = auth.destroy_session(request)

    if destroy_session:
        return jsonify({}), 200
    abort(404)
