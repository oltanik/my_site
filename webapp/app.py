from flask import Flask, render_template
from webapp.db import db, init_app_db
from .models.user import User
from .authorization import authorization

app = Flask(__name__)
app.config.from_pyfile('config.py')
init_app_db(app, db)

@app.route('/')
def index():
    page_title = app.config['TEXT_TITLE']
    text = app.config['TEXT']
    return render_template('main_page.html', page_title=page_title, text=text, users=User.query.all())


app.register_blueprint(authorization)

"""
Запуск сервера:
set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run
"""
