import unittest
import json

from app.models.tag import Tag
from app.models.lab import Lab
from tests.utils.test_utils import TestClientManager, http_status, db, default_http_headers


class TagApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        TestClientManager.setUpAppClient()

    @classmethod
    def tearDownClass(cls):
        TestClientManager.tearDownAppClient()

    def setUp(self):
        self.prepareTags()

    def tearDown(self):
        Tag.query.delete()
        Lab.query.delete()
        db.session.commit()

    def test_get_all_tags(self):
        response = TestClientManager.test_client.get('/api/v1/tag')
        data = json.loads(response.data)
        self.assertEquals(http_status[200], response.status)
        self.assertTags(data)

    def test_get_single_tag(self):
        response = TestClientManager.test_client.get('/api/v1/tag/2')
        data = json.loads(response.data)
        self.assertEquals(http_status[200], response.status)
        self.assertEqual(2, data['id'])
        self.assertEqual('tag2', data['name'])
        self.assertEqual('some_lab', data['labs'][0]['name'])

    def test_delete_single_tag(self):
        response = TestClientManager.test_client.delete('/api/v1/tag/2')
        self.assertEquals(http_status[204], response.status)
        self.assertFalse(response.data)

    def test_post_single_tag(self):
        new_tag = {'name': 'sample_tag'}
        response = TestClientManager.test_client.post('api/v1/tag', data=json.dumps(new_tag),
                                                      headers=default_http_headers)
        data = json.loads(response.data)
        self.assertEquals(http_status[201], response.status)
        self.assertEquals('sample_tag', data['name'])

    def test_put_single_tag(self):
        modified_tag = {'name': 'new_tag_name'}
        response = TestClientManager.test_client.put('api/v1/tag/3', data=json.dumps(modified_tag),
                                                     headers=default_http_headers)
        data = json.loads(response.data)
        self.assertEquals(http_status[200], response.status)
        self.assertEquals('new_tag_name', data['name'])

    def prepareTags(self):
        tag_1 = Tag('tag1')
        tag_2 = Tag('tag2')
        tag_3 = Tag('tag3')
        sample_lab = Lab('some_lab')
        sample_lab.tags.append(tag_2)
        db.session.add(tag_1)
        db.session.add(tag_2)
        db.session.add(tag_3)
        db.session.commit()

    def assertTags(self, data):
        self.assertEqual(1, data['objects'][0]['id'])
        self.assertEqual('tag1', data['objects'][0]['name'])
        self.assertEqual(2, data['objects'][1]['id'])
        self.assertEqual('tag2', data['objects'][1]['name'])
        self.assertEqual(3, data['objects'][2]['id'])
        self.assertEqual('tag3', data['objects'][2]['name'])

