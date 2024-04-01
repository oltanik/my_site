from flask import render_template, request, Blueprint, current_app
from webapp.db import db, clear_tables
from .models.user import User

authorization = Blueprint('authorization', __name__)

@authorization.route("/registration", methods=["GET", "POST"])
def registration():
    page_title = current_app.config['TEXT_TITLE']
    text = current_app.config['TEXT']

    if request.method == "POST":
        # Считываем параметры из формы
        login = request.form.get("login")
        password = request.form.get("password")
        # # Заливаем данные в БД
        db.session.add(User(login, password))
        db.session.commit()

        return render_template('main_page.html', page_title=page_title, text=text, login=login, password=password,
                               users=User.query.all())
    else:
        return render_template('main_page.html', page_title=page_title, text=text, users=User.query.all())


@authorization.route("/clear", methods=["GET", "POST"])
def clear():
    page_title = current_app.config['TEXT_TITLE']
    text = current_app.config['TEXT']

    clear_tables(db)

    return render_template('main_page.html', page_title=page_title, text=text, users=User.query.all())
