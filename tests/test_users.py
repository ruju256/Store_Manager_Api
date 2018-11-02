from app import app
from unittest import TestCase 
import json


class TestUserEndpoints(TestCase):


    def setUp(self):
        self.client = app.test_client()
    
    def tearDown(self):
        pass
    

    
    def test_if_user_is_created(self):
        new_user = {
            "name":"ezra",
            "email":"ezramahlon@gmail.com",
            "password":"admin123",
            "role":"admin"
             }

        response =  self.client.post('/auth/signup',content_type='application/json',data=json.dumps(new_user)
        )
        response_data = json.loads(response.data.decode())

        self.assertEqual(response_data['msg_fail'], 'ezramahlon@gmail.com is already registered. Try other or Login')
        self.assertEqual(response_data['msg'], 'You have successfully added ezra')
        self.assertEqual(response.status_code, 201)
    
