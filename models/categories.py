from database.dbsetup import Database
from models.users import Users


databaseObject = Database()
class Categories():

    def __init__(self, category):
        self.category = category


    def save_category(self):
        '''creating database connection'''
        databaseObject.add_a_category(self.category)
        return "{}".format(self.category)
        
    