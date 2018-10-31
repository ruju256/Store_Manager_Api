import datetime
from database.dbsetup import Database

database = Database()
class Products():

    product_list = []

    def __init__(self, product_name, manufacture_date, expiry_date, quantity):
        self.product_name = product_name
        self.manufacture_date = manufacture_date
        self.expiry_date = expiry_date
        self.quantity = quantity

    # def fetch_all_products():
    #     product_list =  database.q

