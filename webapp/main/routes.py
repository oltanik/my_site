from datetime import datetime, timezone
from flask import render_template, flash, redirect, url_for, request, g, \
    current_app
from flask_babel import _, get_locale
from flask_login import current_user, login_required
from webapp.app import db
from webapp.main import bp

@bp.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.now(timezone.utc)
        db.session.commit()
    g.locale = str(get_locale())

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    page_title = current_app.config['TEXT_TITLE']
    text = current_app.config['TEXT']
    return render_template('main_page.html', page_title=page_title, text=text)