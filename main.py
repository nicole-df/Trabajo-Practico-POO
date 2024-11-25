from db_classes.database import Database

print("\n--- Base de Datos Documental ---")

def mostrar_menu():
    print("\n1. Crear colección")
    print("2. Importar CSV a colección")
    print("3. Consultar documento en colección")
    print("4. Eliminar documento de colección")
    print("5. Listar todos los documentos en colección")
    print("6. Listar todas las colecciones")
    print("7. Salir")
    return input("\nSeleccione una opción: ")

def main():
    db = Database()

    while True:
        opt = mostrar_menu()
        
        if opt == "1":
            name = input("Ingrese el nombre de la colección: ")
            db.create_collection(name)
            print(f"\nColección '{name}' creada.")
        
        elif opt == "2":
            name = input("Ingrese el nombre de la colección: ")
            if name not in db.get_list():
                print(f"\nColección '{name}' no encontrada.")
            else:
                path = input("Ingrese la ruta del archivo CSV: ")
                if db.import_csv(name, path):
                    print(f"\nArchivo '{path}' importado.")
                else:
                    print(f"\nNo se puedo importar el archivo '{path}'.") 
        
        elif opt == "3":
            name = input("Ingrese el nombre de la colección: ")
            collection = db.get_collection(name)
            if collection:
                doc_id = int(input("Ingrese el ID del documento: "))
                document = collection.search_document(doc_id)
                if document:
                    print("\nDocumento encontrado:")
                    print(document)
                else:
                    print("\nDocumento no encontrado.")
            else:
                print(f"\nColección '{name}' no encontrada.")
        
        elif opt == "4":
            name = input("Ingrese el nombre de la colección: ")
            collection = db.get_collection(name)
            if collection:
                doc_id = int(input("Ingrese el ID del documento a eliminar: "))
                collection.delete_document(doc_id)
                print("\nDocumento eliminado.")
            else:
                print(f"\nColección '{name}' no encontrada.")
        
        elif opt == "5":
            name = input("Ingrese el nombre de la colección: ")
            collection = db.get_collection(name)
            if collection:
                documents = collection.get_list()
                if documents:
                    print("\nLista de Documentos:")
                    for doc in documents:
                        print(f"{doc}")
                else:
                    print("\nNo hay documentos en la colección.")
            else:
                print(f"\nColección '{name}' no encontrada.")
        
        elif opt == "6":
            col_list = db.get_list()
            if col_list:
                print("\nLista de colecciones:")
                for index, col in enumerate(col_list, start=1):
                    print(f"{index}){col}")
            else:
                print("\nNo hay colecciones creadas.")

        elif opt == "7":
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()