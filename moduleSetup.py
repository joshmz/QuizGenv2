import Database as db

class Module:
    def __init__(self,name,description):
        self.name = name
        self.description = description

    def insert_data(self):
        module = [
            self.name,
            self.description
        ]
        db.cursor.execute('INSERT INTO modules (moduleName, moduleDesc) VALUES (?,?)',module)
        db.conn.commit()

def create_module(name,desc):
    module_instance = Module(name,desc)
    module_instance.insert_data()