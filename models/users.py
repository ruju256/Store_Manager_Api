from database.dbsetup import Database
import datetime
import time

databaseObject = Database()
class Users(object):

    def __init__(self, name, email, password, role):
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        
    def save_user(self):
        '''creating database connection'''
        
        databaseObject.create_a_user(self.name, self.email, self.password, self.role)
        return "{}".format(self.name)

