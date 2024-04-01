from flask_sqlalchemy import SQLAlchemy

DBUSER = 'service'
DBPASS = 'pass'
DBHOST = 'database'
DBPORT = '5432'
DBNAME = 'testdb'

DBURL = 'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
    user=DBUSER,
    passwd=DBPASS,
    host=DBHOST,
    port=DBPORT,
    db=DBNAME)

db = SQLAlchemy()


def init_app_db(app, db):
    app.config['SQLALCHEMY_DATABASE_URI'] = DBURL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'testdb'
    db.init_app(app)

def clear_tables(db):
    db.drop_all()
    db.create_all()
    db.session.commit()