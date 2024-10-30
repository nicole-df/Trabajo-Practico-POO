from collection import Collection
from document import Document

class DocumentDatabase:
    def __init__(self):
        self.collections = {}

    def create_collection(self, name_collection):
        if name_collection in self.collections:
            self.collections[name_collection] = Collection(name_collection)

    def delete_collection(self, name_collection):
        if name_collection in self.collections:
            del self.collections[name_collection]
        
    def get_collection(self, name_collection):
        return self.collections.get(name_collection, None)
    
    def __str__(self):
        return f"Document Database has {len(self.collections)} collections."