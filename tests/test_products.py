from app import app
from unittest import TestCase 
import json


class TestProductEndpoints(TestCase):


    def setUp(self):
        self.client = app.test_client()
    
    def tearDown(self):
        pass
    

    
    def test_if_product_is_saved(self):
        new_product = {
            "description": "TipTop bread",
            "expiry_date": "2019-06-17",
            "manufacture_date": "2018-06-17",
            "product_name": "Bread",
            "quantity": 50
        }

        response =  self.client.post('/api/v1/products',content_type='application/json',data=json.dumps(new_product)
            )

        response_data = json.loads(response.data.decode())

        self.assertEqual(response_data['msg'], 'Bread successfully added')
        self.assertEqual(response.status_code, 201)

  