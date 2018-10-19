import os
import sys
from app import app
from unittest import TestCase 




class TestStoreEndpoints(TestCase):

    def setUp(self):
        self.client = app.test_client(self)
    
    def tearDown(self):
        pass
    
    def test_invalid_route(self):
        response = self.client.get('/api/products')
        self.assertTrue(response.status_code, 406)

    def test_if_products_endpoint_exists(self):
        response = self.client.get('/api/v1/products', redirect_resource = True)
        return (response.status, 200)

    