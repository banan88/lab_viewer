import os

from flask import Flask, make_response
from app.services.api import create_api_manager
from app.shared import db

database_driver = 'sqlite:///'
database_path = 'db/lab_viewer.db'


def create_app():
    """
    Creates & configures flask application object and associates sqlalchemy db object with it.
    """
    app = Flask(__name__, static_url_path='')
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = database_driver + database_path
    db.app = app
    db.init_app(app)
    return app

def create_db_schema():
    """
    Initializes db structure if needed (open & close works like unix 'touch' - to make sure db file exists)
    """
    open(database_path, 'a').close()
    if os.stat(database_path).st_size == 0:
        print 'creating database...'
        db.create_all()


app = create_app()
create_api_manager(app)

@app.route('/')
def home():
    return make_response(open('static/home.html').read())

if __name__ == '__main__':
    create_db_schema()
    app.run()
