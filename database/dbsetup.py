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
            
            creating_table_users = '''CREATE TABLE users
                (
                    id SERIAL   PRIMARY KEY ,                                        
                    name    VARCHAR (50)    NOT NULL,
                    email   VARCHAR (50)    NOT NULL,
                    password    VARCHAR (50)    NOT NULL,
                    role    VARCHAR (50) NOT NULL
                ); '''    

            self.cursor.execute(creating_table_users)
            self.connection.commit()
            print("Tables successfully Created")

        except Exception as error :
            print ("Error!!!, could not connect to database", error)
        

    def create_a_user(self, name, email, password, role):        
        creating_a_user = '''INSERT INTO users(name,email,password,role) VALUES('{}','{}','{}','{}');'''.format(name,email,password,role)
        self.cursor.execute(creating_a_user)
    
