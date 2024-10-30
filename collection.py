class Collection:
    def __init__(self, name, schema):
        self.name = name
        self.schema = schema
        self.documents = {}

    def add_document(self, document):
        self.documents[document.id] = document

    def delete_document(self, id_document):
        if id_document in self.documents:
            del self.documents[id_document]
    
    def search_document(self, id_document):
        return self.documents.get(id_document, None)
    
    def __str__(self):
        return f"Collection {self.name} has {len(self.documents)} documents." 
