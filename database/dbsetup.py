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

            creating_table_user_roles = '''CREATE TABLE user_roles
                (
                    id INTEGER      PRIMARY KEY     NOT NULL,
                    role         VARCHAR (50)    NOT NULL
                ); '''
            
            creating_table_users = '''CREATE TABLE users
                (
                    id INTEGER   PRIMARY KEY     NOT NULL,
                    role_id      INTEGER REFERENCES  user_roles(id),
                    email        VARCHAR (50)    NOT NULL,
                    firstname    VARCHAR (50)    NOT NULL,
                    lastname     VARCHAR (50)    NOT NULL, 
                    password     VARCHAR (50)    NOT NULL,
                    create_date  TIMESTAMP       NOT NULL,
                    last_logged_in    TIMESTAMP
                ); '''    
            
            self.cursor.execute(creating_table_user_roles)
            self.cursor.execute(creating_table_users)
            self.connection.commit()
            print("Tables successfully Created")

        except (Exception, psycopg2.DatabaseError) as error :
            print ("Error!!!, could not connect to database", error)
        finally:
            #closing database connection (connection was successful).
                if(self.connection):
                    self.cursor.close()
                    self.connection.close()
                    print("Database connection closed")
    
    def create_a_role(self, role):
        creating_a_role = '''INSERT INTO roles(role) VALUES('{}');'''.format(role)
        self.cursor.execute(creating_a_role)

    def create_a_user(self, name, email, password, role):
        creating_a_user = '''INSERT INTO users(name,email,password,role) VALUES('{}','{}','{}','{}');'''.format(name,email,password, role)
        self.cursor.execute(creating_a_user)