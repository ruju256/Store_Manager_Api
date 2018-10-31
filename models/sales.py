import datetime
from database.dbsetup import Database

databaseObject = Database()
class Sales():

    product_list = []

    def __init__(self, product_name, manufacture_date, expiry_date, quantity, description):
        self.product_name = product_name
        self.manufacture_date = manufacture_date
        self.expiry_date = expiry_date
        self.quantity = quantity
        self.description = description

    # def fetch_all_products():
    #     product_list =  database.q

    def save_product(self):
        '''creating database connection'''
        databaseObject.add_a_product(self.product_name, self.manufacture_date, self.expiry_date, self.quantity, self.description)
        return "{}".format(self.product_name)

    def update_product(self, id):
        pass
