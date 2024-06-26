ASCII_A_UPPER = 65
ASCII_A_LOWER = 97
ALPHABET_LENGTH = 26


class CeaserCipher:
    def encrypt(self, text: str, key: int) -> str:
        """encrypts string using Caesar Cipher using given key"""
        if not isinstance(key, int):
            raise TypeError

        result = ""
        for char in text:
            if char.isalpha():
                shift = ASCII_A_UPPER if char.isupper() else ASCII_A_LOWER
                result += chr((ord(char) + key - shift) % ALPHABET_LENGTH + shift)
            else:
                result += char
        return result

    def decrypt(self, text: str, key: int) -> str:
        """decrypts string using Caesar Cipher with a given key"""
        return self.encrypt(text, -key)
