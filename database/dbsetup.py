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

            creating_table_products = '''CREATE TABLE IF NOT EXISTS products
                (
                    id SERIAL PRIMARY KEY,
                    product_name TEXT NOT NULL,
                    manufacture_date TEXT NOT NULL,
                    expiry_date TEXT NOT NULL,
                    quantity TEXT NOT NULL,
                    description TEXT NOT NULL
                );'''

            
            self.cursor.execute(creating_table_users)
            self.cursor.execute(creating_table_products)
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

    def add_a_product(self, product_name, manufacture_date, expiry_date, quantity, description):
        adding_a_product="""
        INSERT INTO products (product_name, manufacture_date, expiry_date, quantity, description) VALUES('{}','{}','{}','{}','{}');
        """.format(product_name,manufacture_date,expiry_date,quantity, description)
        self.cursor.execute(adding_a_product)
        self.connection.commit()