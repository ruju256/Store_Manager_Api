import os
import sys
from main.app import app
from unittest import TestCase 
import coverage
import json


class TestStoreEndpoints(TestCase):


    def setUp(self):
        self.products = [
            {
                'id' : 1,
                'product_name' : 'Bread',
                'manufacture_date' : '2018-11-02',
                'expiry_date' : '2019-01-10'
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
        self.client = app.test_client(self)
    
    def tearDown(self):
        pass
    
     
    def test_if_get_products_returns_a_list_of_all_products(self):
        response = self.client.get('/api/v1/products', data=json.dumps(self.products), content_type='application/json')        
        self.assertEqual(response.status_code, 200)
        
        
    def test_if_get_single_product_details_returns_details_for_one_product(self):
        response = self.client.get('/api/v1/products/1', data = json.dumps(self.products), content_type='application/json')
        self.assertEqual(response.status_code, 200)       


    def test_if_get_sales_records_returns_a_list_of_all_sale_records(self):
        response = self.client.get('/api/v1/sales', data=json.dumps(self.sales), content_type='application/json')        
        self.assertEqual(response.status_code, 200)
        

    def test_if_get_single_sales_record_returns_details_for_one_sale_record(self):
        response = self.client.get('/api/v1/sales/1', data = json.dumps(self.sales), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        

    # def test_if_add_new_product_adds_a_new_product_to_json_list(self):
    #     response = self.client.post('/api/v1/products', data=json.dumps(self.products), content_type='application/json')
    #     self.assertEqual(response.status_code, 201)

    # def test_if_create_a_sale_adds_a_new_sale_record(self):
    #     response = self.client.post('api/v1/sales', data=json(self.sales), content_type='application/json')
    #     self.assertEqual(response.status_code, 201)

    # def test_if_update_product_updates_details_for_a_specific_product(self):
    #     response = self.client.put('/api/v1/products/1')
    #     self.assertEqual(response.status_code, 200)
    
    # def test_if_delete_product_removes_product_from_json_list(self):
    #     response = self.client.delete('/api/v1/prodcuts/1')
    #     self.assertEqual(response.status_code, 200)
    


if __name__ == '__main__':
    unittest.main()