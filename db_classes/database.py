from db_classes.collection import Collection
from utils.filemanager import FileManager
from utils.str2dic import Str2Dic

class Database:
    def __init__(self):
        self.collections = {}

    def create_collection(self, name_collection):
        if name_collection not in self.collections:
            self.collections[name_collection] = Collection(name_collection)

    def delete_collection(self, name_collection):
        if name_collection in self.collections:
            del self.collections[name_collection]
        
    def get_collection(self, name_collection):
        return self.collections.get(name_collection, None)
    
    def get_list(self):
        return list(self.collections.keys())
    
    def import_csv(self, name, path):
        file = FileManager(path)
        try:
            content = file.read_text().splitlines()
        except:
            return False
        conv = Str2Dic(content[0])
        i = 1
        while i < len(content):
            dic_line = conv.convert(content[i])
            self.collections[name].add_document(dic_line)
            i+=1
        return True
            
    def __str__(self):
        return f"Document Database has {len(self.collections)} collections."