import psycopg2
from psycopg2 import Error

class Database():

    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                                        database = "andela_test_db",
                                        user = "postgres",
                                        password = "Tahiti92",
                                        host = "localhost",
                                        port = "5432"                                
                                    )

            self.cursor = self.connection.cursor()
           

            creating_table_users = '''CREATE TABLE IF NOT EXISTS users
                (
                    id SERIAL   PRIMARY KEY ,                                        
                    name    TEXT    NOT NULL,
                    email   TEXT    NOT NULL,
                    password    TEXT    NOT NULL,
                    role    TEXT NOT NULL
                ); '''    

            creating_table_categories = '''CREATE TABLE IF NOT EXISTS product_categories
            (
                id SERIAL   PRIMARY KEY ,                                        
                category    TEXT    NOT NULL
            ); '''    

            creating_table_products = '''CREATE TABLE IF NOT EXISTS products
                (
                    id SERIAL PRIMARY KEY,
                    product_name TEXT NOT NULL,
                    unit_price INT NOT NULL,
                    quantity INT NOT NULL,
                    description TEXT NOT NULL,
                    category_id INT REFERENCES product_categories(id)
                );'''

            creating_table_sales = '''CREATE TABLE IF NOT EXISTS sales
                (
                    id SERIAL PRIMARY KEY,
                    product_id INT REFERENCES products(id) NOT NULL,
                    product_name TEXT NOT NULL,
                    product_unit_price INT NOT NULL,
                    quantity INT NOT NULL,
                    total_amount INT NOT NULL                    
                );'''
            
            self.cursor.execute(creating_table_users)
            self.cursor.execute(creating_table_categories)
            self.cursor.execute(creating_table_products)
            self.cursor.execute(creating_table_sales)
            self.connection.commit()          
            print("Tables successfully Created")

        except Exception as error :
            print ("Error!!!, could not connect to database", error)
        

    def create_a_user(self, name, email, password, role):        
        creating_a_user = """
        INSERT INTO users (name,email,password,role) VALUES('{}','{}','{}','{}');
        """.format(name,email,password,role)
        self.cursor.execute(creating_a_user)
        self.connection.commit()

    def query(self,table_name, column_name, value):
        get_an_item = """ SELECT * FROM {} WHERE {}='{}';""".format(table_name, column_name, value)
        self.cursor.execute(get_an_item)
        row = self.cursor.fetchone()
        self.connection.commit()
        return row

    def add_a_product(self, product_name, unit_price, quantity, description, category):
        adding_a_product="""
        INSERT INTO products (product_name, unit_price, quantity, description, category_id) VALUES('{}','{}','{}','{}','{}');
        """.format(product_name, unit_price, quantity, description, category)
        self.cursor.execute(adding_a_product)
        self.connection.commit()

    def update_a_product(self, product_name, unit_price, quantity, description, category, id):
        updating_a_product = """
        UPDATE products SET product_name='{}', unit_price='{}', quantity='{}', description='{}', category_id='{}'\
        WHERE id='{}';""".format(product_name, unit_price, quantity, description, category, id)
        self.cursor.execute(updating_a_product)
        self.connection.commit()
    
    def delete_product(self, id):
        deleting_a_product = """
        DELETE FROM products WHERE id = '{}';""".format(id)
        self.cursor.execute(deleting_a_product)
        self.connection.commit()

    def view_all_records(self, table_name):
        products = """SELECT * FROM {};""".format(table_name)
        self.cursor.execute(products)
        self.connection.commit()
        return self.cursor.fetchall() 

    def add_a_category(self, category):
        adding_a_category="""
        INSERT INTO product_categories (category) VALUES('{}');
        """.format(category)
        self.cursor.execute(adding_a_category)
        self.connection.commit()