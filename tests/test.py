import unittest 
from app.app import app


class StoreEndpoints(unittest.TestCase):

    def test_if_products_endpoit_exists(self):
        response = self.app.get('/api/v1/products', redirect_resource = True)
        return (response.status, 200)

    


if "__name__" == "__main__":
    unittest.main()
    