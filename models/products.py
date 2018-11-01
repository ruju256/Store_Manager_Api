import datetime
from database.dbsetup import Database
from models.users import Users

databaseObject = Database()
class Products():

    product_list = []

    def __init__(self, product_name, manufacture_date, expiry_date, quantity, description):
        self.product_name = product_name
        self.manufacture_date = manufacture_date
        self.expiry_date = expiry_date
        self.quantity = quantity
        self.description = description


    def save_product(self):
        '''creating database connection'''
        databaseObject.add_a_product(self.product_name, self.manufacture_date, self.expiry_date, self.quantity, self.description)
        return "{}".format(self.product_name)

    def update_a_product(self, id):
        product = Users.find_specific_item('products','id', id)        
        if product is None:
            return False       
        databaseObject.update_a_product(self.product_name, self.manufacture_date, self.expiry_date, self.quantity, self.description, id)
        product = Users.find_specific_item('products','id', id)

        return{
            "id":product[0],
            "product_name":product[1],
            "manufacture_date":product[2],
            "expiry_date":product[3],
            "quantity":product[4],
            "description":product[5]
        }

    def get_details_for_single_product(self, id):
        product = Users.find_specific_item('products', 'id', id)
        if product is None:
            return False
        return{
            "product_name":product[1],
            "manufacture_date":product[2],
            "expiry_date":product[3],
            "quantity":product[4],
            "description":product[5]
        }

    @staticmethod
    def delete_product(id):
        product = Users.find_specific_item('products', 'id', id)
        if product is None:
            return False
        databaseObject.delete_product(id)
        return{
            "msg":"Product has been deleted"
        }

