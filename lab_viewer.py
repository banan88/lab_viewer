import os
from flask import Flask
from flask.ext.restless import APIManager
from app.shared import db
from app.models.tag import Tag

database_driver = 'sqlite:///'
database_path = 'db/lab_viewer.db'
rest_api_prefix = '/api/v1'


def create_app():
    """
    Creates & configures flask application object and associates sqlalchemy db object with it.
    """
    app = Flask(__name__)
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = database_driver + database_path
    db.app = app
    db.init_app(app)
    return app


def create_api_manager(application):
    """
    Creates & configures flask-restless api manager providing rest api for db model classes.
    """
    manager = APIManager(application, flask_sqlalchemy_db=db)
    manager.create_api(Tag, url_prefix=rest_api_prefix, methods=['GET'])


def create_db_schema():
    """
    Initializes db structure if needed (open & close works like unix 'touch' - to make sure db file exists)
    """
    open(database_path, 'a').close()
    if os.stat(database_path).st_size == 0:
        print 'creating database' #TODO research for some cool file logging utilities
        db.create_all()


app = create_app()
create_api_manager(app)


@app.route('/') #
def hello_world():
    return 'TODO: should serve frontend js app.'


if __name__ == '__main__':
    create_db_schema()
    app.run()
