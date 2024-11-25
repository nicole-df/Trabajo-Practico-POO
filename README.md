# Trabajo Practico Final 
**IFTS 11 - Desarrollo de Sistemas Orientado a Objetos**

### 📚 Project Overview
 This is a Python-based in-memory database for documents, supporting CRUD operations, CSV imports, and designed with extensibility for future features.

### 🛠 Technology
 :snake: Python

### :cd: How to use
 Execute **main.py**

---

### :page_facing_up: Content
1. **Database classes**  
   In this section, we can find the key classes for managing the database. These classes allow for storing, retrieving, and manipulating documents and collections.
   - [Database](src/db_classes/database.py):
   - [Collection](src/db_classes/collection.py)
   - [Document](src/db_classes/document.py): 
3. **Utils**  
   Here we can find two classes that help us with operations such as managing file operations and converting string data into a dictionary format.
   - [File Manager](src/utils/filemanager.py)
   - [String to Dic](src/utils/str2dic.py)
4. **Main**  
   Main is where the application starts. It manages user interactions with the database.
   - [Main](src/main.py)
