import json


class FileManager:
    @staticmethod
    def load_from_json(file_path: str):
        """loads a data from a given json file"""
        with open(file_path, 'r') as file:
            return json.load(file)

    @staticmethod
    def save_to_json(data: list):
        """saves current history to json file"""
        with open("history.json", 'w') as file:
            json.dump(data, file)
