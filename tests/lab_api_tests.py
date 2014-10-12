import unittest
import json
from tests.test_utils import TestClientManager, http_status, db, default_http_headers
from app.models.lab import Lab
from app.models.tag import Tag


class LabApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        TestClientManager.setUpAppClient()

    @classmethod
    def tearDownClass(cls):
        TestClientManager.tearDownAppClient()

    def setUp(self):
        self.prepareLabs()

    def tearDown(self):
        Lab.query.delete()
        Tag.query.delete()
        db.session.commit()

    def test_get_all_labs(self):
        response = TestClientManager.test_client.get('/api/v1/lab')
        data = json.loads(response.data)
        self.assertEquals(http_status[200], response.status)
        self.assertLabs(data)

    def test_get_single_lab(self):
        response = TestClientManager.test_client.get('/api/v1/lab/1')
        data = json.loads(response.data)
        self.assertEquals(http_status[200], response.status)
        self.assertEquals(data['id'], 1)
        self.assertEquals(data['name'], 'lab1')

    def test_get_single_lab_with_children(self):
        response = TestClientManager.test_client.get('/api/v1/lab/3')
        data = json.loads(response.data)
        self.assertEquals(http_status[200], response.status)
        self.assertEquals(data['id'], 3)
        self.assertEquals(data['name'], 'lab3_master')
        self.assertEquals(data['child_nodes'][0]['id'], 4)
        self.assertEquals(data['child_nodes'][0]['name'], 'lab4_slave')
        self.assertEquals(data['child_nodes'][1]['id'], 5)
        self.assertEquals(data['child_nodes'][1]['name'], 'lab5_slave')

    def test_delete_single_lab_and_remove_reference_in_child_nodes(self):
        response = TestClientManager.test_client.delete('/api/v1/lab/3')
        self.assertEquals(http_status[204], response.status)
        self.assertFalse(response.data)
        child_response = TestClientManager.test_client.get('/api/v1/lab/4')
        data = json.loads(child_response.data)
        self.assertFalse(data['parent_id'])

    def test_put_single_lab(self):
        modified_lab = {'name': 'lab3_master_modified'}
        response = TestClientManager.test_client.put('api/v1/lab/3', data=json.dumps(modified_lab),
                                                     headers=default_http_headers)
        data = json.loads(response.data)
        self.assertEquals(http_status[200], response.status)
        self.assertEquals('lab3_master_modified', data['name'])

    def test_put_single_lab_error_when_assigning_master_to_lab_with_children(self):
        modified_lab = {'parent_id': 1}
        response = TestClientManager.test_client.put('api/v1/lab/3', data=json.dumps(modified_lab),
                                                     headers=default_http_headers)
        data = json.loads(response.data)
        self.assertEquals(http_status[400], response.status)

    def test_post_single_lab_with_parent_and_tag(self):
        new_tag_1 = {'name': 'new_tag_1'}
        new_tag_2 = {'name': 'new_tag_2'}
        new_lab = {'name': 'new_lab', 'parent_id': 3, 'tags': [new_tag_1, new_tag_2]}
        response = TestClientManager.test_client.post('api/v1/lab', data=json.dumps(new_lab),
                                                      headers=default_http_headers)
        data = json.loads(response.data)
        self.assertEquals(http_status[201], response.status)
        self.assertEquals('new_lab', data['name'])
        self.assertEquals(3, data['parent_id'])
        self.assertItemsEqual(['new_tag_1', 'new_tag_2'], [data['tags'][0]['name'], data['tags'][1]['name']])

    def test_post_single_lab_with_children(self):
        new_child_lab_1 = {'name': 'child_lab1'}
        new_child_lab_2 = {'name': 'child_lab2'}
        new_lab = {'name': 'new_lab', 'child_nodes': [new_child_lab_1, new_child_lab_2]}
        response = TestClientManager.test_client.post('api/v1/lab', data=json.dumps(new_lab),
                                                      headers=default_http_headers)
        data = json.loads(response.data)
        self.assertEquals(http_status[201], response.status)
        self.assertEquals('new_lab', data['name'])
        self.assertFalse(data['parent_id'])
        print data
        self.assertEquals(['child_lab1', 'child_lab2'],
                          [data['child_nodes'][0]['name'], data['child_nodes'][1]['name']])

    def assertLabs(self, data):
        self.assertEqual(1, data['objects'][0]['id'])
        self.assertEqual('lab1', data['objects'][0]['name'])
        self.assertEqual(2, data['objects'][1]['id'])
        self.assertEqual('lab2', data['objects'][1]['name'])
        self.assertEqual(3, data['objects'][2]['id'])
        self.assertEqual('lab3_master', data['objects'][2]['name'])

    def prepareLabs(self):
        lab_1 = Lab('lab1')
        lab_2 = Lab('lab2')
        lab_3 = Lab('lab3_master')
        lab_4 = Lab('lab4_slave')
        lab_5 = Lab('lab5_slave')
        lab_4.parent = lab_3
        lab_5.parent = lab_3
        db.session.add(lab_1)
        db.session.add(lab_2)
        db.session.add(lab_3)
        db.session.add(lab_4)
        db.session.add(lab_5)
        db.session.commit()
