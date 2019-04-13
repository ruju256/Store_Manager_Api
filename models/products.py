import datetime
from database.dbsetup import Database
from models.users import Users

databaseObject = Database()
class Products():

    product_list = []

    def __init__(self, product_name, unit_price, quantity, description, category):
        self.product_name = product_name
        self.unit_price = unit_price
        self.quantity = quantity
        self.description = description
        self.category = category


    def save_product(self):
        '''creating database connection'''
        databaseObject.add_a_product(self.product_name, self.unit_price, self.quantity, self.description, self.category)
        return "{}".format(self.product_name)

    def update_a_product(self, id):
        product = Users.find_specific_item('products','id', id)        
        if product is None:
            return False       
        databaseObject.update_a_product(self.product_name, self.unit_price, self.quantity, self.description, self.category, id)
        product = Users.find_specific_item('products','id', id)

        return{
            "id":product[0],
            "product_name":product[1],
            "unit_price":product[2],
            "quantity":product[3],
            "description":product[4],
            "category":product[5]
        }

    def get_details_for_single_product(self, id):
        product = Users.find_specific_item('products', 'id', id)
        if product is None:
            return False
        return{
            "product_name":product[1],
            "unit_price":product[2],
            "quantity":product[3],
            "description":product[4],
            "category":product[5]
        }

    @staticmethod
    def delete_product(id):
        product = Users.find_specific_item('products', 'id', id)
        if product is None:
            return False
        databaseObject.delete_product(id)
        return{"msg":"Product has been deleted"}

    @staticmethod
    def view_all_products(table_name):
        product_list = databaseObject.view_all_records(table_name)
        if product_list ==[]:
            print("You have no products in the store")
            return False
        
        Products.product_list.clear()
        for product in product_list:
            product = {
                "id":product_list[0],
                "product_name":product_list[1],
                "unit_price":product_list[2],
                "quantity":product_list[3],
                "description":product_list[4],
                "category":product_list[5]
            }
            Products.product_list.append(product)
            return Products.product_list
    
     


