import json

class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_text(self):
        try:
            with open(self.file_path, 'r') as file:
                content = file.read()
                return content
        except FileNotFoundError:
            print(f"Error: File {self.file_path} not found.")
        except Exception as e:
            print(f"Error reading file {e}.")

    def write_text(self, content):
        try:
            with open(self.file_path, 'w') as file:
                file.write(content)
            print(f"File {self.file_path} written successfully")
        except Exception as e:
            print(f"Error writting file {e}.")
    
    def read_json(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print(f"Error: File {self.file_path} not found.")
        except json.JSONDecodeError:
            print(f"Error decoding file json.")
        except Exception as e:
            print(f"Error reading file json {self.file_path}.")

    def write_json(self, data):
        try:
            with open(self.file_path, 'w') as file:
                json.dump(data, file, indent=4)
            print(f"File json {self.file_path} written successfully.")
        except Exception as e:
            print(f"Error writting file json {e}.")


