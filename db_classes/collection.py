from db_classes.document import Document

class Collection:
    def __init__(self, name):
        self.name = name
        self.documents = {}
        self._id = 1

    def add_document(self, content):
        self.documents[self._id] = Document(content)
        self._id += 1

    def delete_document(self, id_doc):
        if id_doc in self.documents:
            del self.documents[id_doc]
    
    def search_document(self, id_doc):
        return self.documents.get(id_doc, None)
    
    def get_list(self):
        return list(self.documents.items())

    def __str__(self):
        return f"Collection {self.name} has {len(self.documents)} documents." 
    