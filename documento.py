class Documento:
    def __init__(self, id, contenido=None):
        self.id = id
        self.contenido = contenido if contenido is not None else {}

    def obtener_valor(self, clave):
        return self.contenido.get(clave, False)
    
    def modificar_valor(self, clave, valor):
        self.contenido[clave] = valor

    def __str__(self):
        return f"Documento: id={self.id}, contenido={self.contenido} " 
    
