from app import app
from unittest import TestCase 
import json


class TestStoreEndpoints(TestCase):


    def setUp(self):
        self.products = [
            {
                'id' : 1,
                "product_name" : "Bread",
                "manufacture_date" : "2018-11-02",
                "expiry_date" : "2019-01-10"
            }        
        ]
        self.sales = [
            {
                'id' : '1',
                'product_sold' : 'Rice',
                'quantity' : '3 kgs',
                'unit_cost' : '3500',
                'total_cost' : '10500',
                'attendant' : 'john'
            }
        ]
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

        self.assertEqual(response_data['msg'], 'You have successfully added ezra')
        self.assertEqual(response.status_code, 201)