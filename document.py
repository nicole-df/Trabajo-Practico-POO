class Document:
    def __init__(self, id, content=None):
        self.id = id
        self.content = content if content is not None else {}

    def get_value(self, key):
        return self.content.get(key, None)
    
    def update_value(self, key, value):
        self.content[key] = value

    def __str__(self):
        return f"Document:\n ID: {self.id}\n Content: {self.content}"
    
