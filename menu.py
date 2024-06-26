from utils.files import FileManager
from ciphers.caesar import CeaserCipher
from history import Record

MENU = (
    "1. Encrypt Text\n"
    "2. Decrypt Text\n"
    "3. Encrypt from JSON File\n"
    "4. Decrypt from JSON File\n"
    "5. Save History to JSON File\n"
    "6. Load History from JSON File\n"
    "7. Exit"
    )


class Menu:
    def __init__(self):
        self.__is_running = True
        self.files = FileManager()
        self.cipher = CeaserCipher()
        self.history = []
        self.operations = {
            '1': self.encrypt_text,
            '2': self.decrypt_text,
            '3': self.encrypt_from_file,
            '4': self.decrypt_from_file,
            '5': self.save_history_to_file,
            '6': self.load_history_from_file,
            '7': self.end
        }

    def start(self):
        while self.__is_running:
            print(MENU)
            self.get_and_execute_choice()

    def get_and_execute_choice(self):
        users_choice = input("Choose action: ")
        self.operations.get(users_choice, self.show_error)()

    def show_error(self):
        print('Choose from the list!')

    def encrypt_text(self):
        text = input("Enter text to encrypt: ")
        key = int(input("Enter key: "))
        encrypted_text = self.cipher.encrypt(text, key)
        print(f"Encrypted text: {encrypted_text} \n")
        record = Record("encrypt text", text, encrypted_text, key)
        Record.to_save(record, self.history)

    def decrypt_text(self):
        text = input("Enter text to decrypt: ")
        key = int(input("Enter key: "))
        decrypted_text = self.cipher.encrypt(text, key)
        print(f"Decrypted text: {decrypted_text} \n")
        record = Record("decrypt text", text, decrypted_text, key)
        Record.to_save(record, self.history)

    def encrypt_from_file(self):
        file_path = input("Enter path to JSON file: ")
        key = int(input("Enter key: "))
        data = self.files.load_from_json(file_path)
        encrypted_data = self.cipher.encrypt(data, key)
        print(f"Encrypted data from file: {encrypted_data}\n")
        record = Record("encrypt from file", data, encrypted_data, key)
        Record.to_save(record, self.history)

    def decrypt_from_file(self):
        file_path = input("Enter path to JSON file: ")
        key = int(input("Enter key: "))
        data = self.files.load_from_json(file_path)
        decrypted_data = self.cipher.decrypt(data, key)
        print(f"Encrypted data from file: {decrypted_data}\n")
        record = Record("encrypt text", data, decrypted_data, key)
        Record.to_save(record, self.history)

    def save_history_to_file(self):
        self.files.save_to_json(self.history)
        print("History saved.\n")

    def load_history_from_file(self):
        file_path = input("Enter path to load JSON file: ")
        self.history = self.files.load_from_json(file_path)
        print("History loaded.")
        print()

    def end(self):
        save_choice = input('Do you want to save your work? Choose Y/N: ').upper()

        if save_choice == 'Y':
            self.save_history_to_file()
            print("History saved, closing program....")
            self.__is_running = False
        elif save_choice == 'N':
            print("Closing program without saving...")
            self.__is_running = False
        else:
            print("Please, make a choice again \n")
