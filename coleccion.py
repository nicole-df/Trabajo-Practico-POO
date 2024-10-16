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

class Coleccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.documentos = {}

    def añadir_documento(self, documento):
        self.documentos[documento.id] = documento

    def eliminar_documento(self, id_documento):
        if id_documento in self.documentos:
            del self.documentos[id_documento]
    
    def buscar_documento(self, id_documento):
        return self.documentos.get(id_documento)
    
    def __str__(self):
        return f"Coleccion {self.nombre} con {len(self.documentos)} documentos"
