class Document:
    def __init__(self, content=None):
        self.content = content if content is not None else {}

    def get_data(self, key):
        return self.content.get(key, None)
    
    def update_data(self, key, data):
        self.content[key] = data

    def __str__(self):
        return f"{self.content}"
    
    