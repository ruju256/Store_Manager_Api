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

    @staticmethod
    def find_specific_item(table_name, column_name, value):
        item = databaseObject.query(table_name, column_name, value)
        if not item:
            return True
        return item

class ValidateUserEmail(Users):

    def __init__(self, name, email, password, role):
        super().__init__(name, email, password, role)

    
    def does_email_exist(self, email):      

        email_to_check = super().find_specific_item('users','email',email)        
        if email_to_check is None:
            print(email_to_check)
            return {"msg":"{} is available. You can sign in".format(email_to_check)}, email_to_check
        
        return email_to_check
