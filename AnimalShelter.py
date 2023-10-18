from pymongo import MongoClient

class AnimalShelter:
    """Initializes the AnimalShelter object with MongoDB connection details."""
    def __init__(self, username, password):
        # Connection Variables
        USER = username
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31798
        DB = 'AAC'
        COL = 'animals'
    
        # Initialize Connection
        self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}')
        self.db = self.client[DB]
        self.collection = self.db[COL]

    """Inserts a new document in the animals collection."""
    def create(self, data):
        try:
            insert_result = self.collection.insert_one(data)
            if insert_result.acknowledged:
                return True
            else:
                return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    """Fetches documents matching the query from the animals collection."""
    def read(self, query):
        try:
            read_result = list(self.collection.find(query))
            if read_result:
                return read_result
            else:
                return []
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
        
    """Updates documents matching the query in the animals collection."""
    def update(self, query, new_values):
        try:
            update_result = self.collection.update_many(query, {"$set": new_values})
            if update_result:
                return update_result.modified_count
            else:
                return 0
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0
    
    """Deletes documents matching the query from the animals collection."""
    def delete(self, query):
        try:
            delete_result = self.collection.delete_many(query)
            if delete_result:
                return delete_result.deleted_count
            else:
                return 0
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0