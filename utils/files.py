import json


class FileManager:
    @staticmethod
    def load_from_json(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    @staticmethod
    def save_to_json(data):
        with open("history.json", 'w') as file:
            json.dump(data, file)
