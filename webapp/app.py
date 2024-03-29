from flask import Flask, render_template


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        page_title = app.config['TEXT_TITLE']
        text = app.config['TEXT']
        return render_template('index.html', page_title=page_title, text=text)

    return app


"""
Запуск сервера:
set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run
"""
