import os

basedir = os.path.abspath(os.path.dirname(__file__))

TEXT_TITLE = "Naservice запчасти для Subaru"
TEXT = 'Тут будет наш сайт naservice.ru'

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

DBUSER = 'service'
DBPASS = 'pass'
DBHOST = 'database'
DBPORT = '5432'
DBNAME = 'testdb'

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
    user=DBUSER,
    passwd=DBPASS,
    host=DBHOST,
    port=DBPORT,
    db=DBNAME)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

LANGUAGES = ['en', 'es']