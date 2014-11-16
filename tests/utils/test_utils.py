import os
import tempfile
from app.shared import db
from lab_viewer import create_app, create_api_manager

default_http_headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
http_status = {200: '200 OK', 201: '201 CREATED', 204: '204 NO CONTENT', 400: '400 BAD REQUEST'}


class TestClientManager():
    test_client = None
    db = None

    @classmethod
    def setUpAppClient(cls):
        cls.db_handle = tempfile.NamedTemporaryFile(delete=False)
        app = create_app()
        create_api_manager(app)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + cls.db_handle.name
        app.config['TESTING'] = True
        cls.test_client = app.test_client()
        db.init_app(app)
        with app.app_context():
            cls.init_test_db()

    @classmethod
    def tearDownAppClient(cls):
        cls.db_handle.close()
        os.unlink(cls.db_handle.name)
        db.session.remove()

    @classmethod
    def init_test_db(cls):
        db.create_all()