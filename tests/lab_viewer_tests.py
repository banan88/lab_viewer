import os
import unittest
import tempfile
from app.shared import db
from lab_viewer import app


class SomeTestCase(unittest.TestCase):
    def setUp(self):
        self.db_handle = tempfile.NamedTemporaryFile(delete=False)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + self.db_handle.name
        app.config['TESTING'] = True
        self.test_client = app.test_client()
        db.init_app(app)
        with app.app_context():
            self.init_test_db()

    def tearDown(self):
        self.db_handle.close()
        os.unlink(self.db_handle.name)

    def init_test_db(self):
        db.create_all()

    def test(self):
        response = self.test_client.get('/api/v1/tag')
        print response.data


if __name__ == '__main__':
    unittest.main()

