import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(
                                database = "andela_test_db",
                                user = "postgres",
                                password = "Tahiti92",
                                host = "127.0.0.1",
                                port = "5432"                                
                            )

    cursor = connection.cursor()

    creating_table_user_roles = '''CREATE TABLE user_roles
        (
            id INTEGER      PRIMARY KEY     NOT NULL,
            role         VARCHAR (50)    NOT NULL,
            create_date  TIMESTAMP       NOT NULL
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
    
    cursor.execute(creating_table_user_roles)
    cursor.execute(creating_table_users)
    connection.commit()
    print("Tables successfully Created")

except (Exception, psycopg2.DatabaseError) as error :
    print ("Error!!!, could not connect to database", error)
finally:
    #closing database connection (connection was successful).
        if(connection):
            cursor.close()
            connection.close()
            print("Database connection closed")