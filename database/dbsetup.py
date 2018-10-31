import psycopg2
from psycopg2 import Error

class Database():

    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                                        database = "andela_test_db",
                                        user = "postgres",
                                        password = "Tahiti92",
                                        host = "127.0.0.1",
                                        port = "5432"                                
                                    )

            self.cursor = self.connection.cursor()
            self.connection.autocommit = True

            creating_table_users = '''CREATE TABLE IF NOT EXISTS users
                (
                    id SERIAL   PRIMARY KEY ,                                        
                    name    TEXT    NOT NULL,
                    email   TEXT    NOT NULL,
                    password    TEXT    NOT NULL,
                    role    TEXT NOT NULL
                ); '''    

            self.cursor.execute(creating_table_users)            
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
    
