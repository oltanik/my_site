from flask import Flask, render_template, request, app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

DBUSER = 'service'
DBPASS = 'pass'
DBHOST = 'database'
DBPORT = '5432'
DBNAME = 'testdb'

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    # Установка параметров для БД
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
            user=DBUSER,
            passwd=DBPASS,
            host=DBHOST,
            port=DBPORT,
            db=DBNAME)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'testdb'
    db = SQLAlchemy(app)


    @app.route('/')
    def index():
        # Создание таблиц в БД, если их нет
        db.create_all()

        page_title = app.config['TEXT_TITLE']
        text = app.config['TEXT']
        return render_template('index.html', page_title=page_title, text=text, users=User.query.all())

    @app.route("/registration", methods=["GET", "POST"])
    def registration():
        page_title = app.config['TEXT_TITLE']
        text = app.config['TEXT']

        if request.method == "POST":
            # Считываем параметры из формы
            login = request.form.get("login")
            password = request.form.get("password")
            # Заливаем данные в БД
            new_user = User(login, password)
            db.session.add(new_user)
            db.session.commit()

            return render_template('index.html', page_title=page_title, text=text, login=login, password=password, users=User.query.all())
        else:
            return render_template('index.html', page_title=page_title, text=text, users=User.query.all())


    @app.route("/db_contains", methods=["GET", "POST"])
    def show_users():
        page_title = app.config['TEXT_TITLE']
        text = app.config['TEXT']

        if request.method == "POST":
            username = request.form.get("login")
            password = request.form.get("password")
            new_user = app.User(
                    username,
                    password
                )
            db.session.add(new_user)
            db.session.commit()
            return render_template('index.html', page_title=page_title, text=text, username=username, password=password, users=User.query.all())
        else:
            return render_template('index.html', page_title=page_title, text=text, users=User.query.all())


    # -----------------------------------------------------
    # Функции и классы, необходимые для БД
    # -----------------------------------------------------
    # Таблица с пользователями
    class User(db.Model):
        __tablename__ = 'users'
        id = db.Column(db.Integer(), primary_key=True)
        login = db.Column(db.String(100), unique=True, nullable=False)
        password = db.Column(db.String(100), nullable=False)
        created_on = db.Column(db.DateTime(), default=datetime.utcnow)
        updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)
        def __init__(self, login, password):
            self.login = login
            self.password = password

    return app


"""
Запуск сервера:
set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run
"""
