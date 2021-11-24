#!/usr/bin/env python3
'''This Is the flask application'''
from flask import Flask, render_template, request, g
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """[This class sets the config for babel]s
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    '''this gets the user'''
    login_as = request.get('login_as', False)
    if login_as:
        user = users.get(int(login_as), False)
        if user:
            return user
    return None

@app.before_request
def before_request():
    '''This is before request'''
    user = get_user()
    g.user = user

@babel.localeselector
def get_locale():
    """[This determinds the best match in language]

    Returns:
        [Str]: [Lanaguage choosen]
    """
    locale = request.args.get('locale')

    if locale and (locale == 'en' or locale == 'fr'):
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'])
def index():
    """[This renders the template for website]

    Returns:
        [template]: rendered template
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
