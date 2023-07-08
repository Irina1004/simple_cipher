class Encryptor:
    def __init__(self, shift) -> None:
        self.shift = shift

    def simple_encrypt(self, plaintext: str):
        ciphertext = ""
        for char in plaintext:
            if char.isalpha():
                ascii_offset = ord("a") if char.islower() else ord("A")
                shifted_char = chr(
                    (ord(char) - ascii_offset + self.shift) % 26 + ascii_offset
                )
                ciphertext += shifted_char
            else:
                ciphertext += char

        return ciphertext


class Decryptor:
    def __init__(self, shift) -> None:
        self.shift = shift

    def simple_decrypt(self, ciphertext: str):
        plaintext = ""
        for char in ciphertext:
            if char.isalpha():
                ascii_offset = ord("a") if char.islower() else ord("A")
                shifted_char = chr(
                    (ord(char) - ascii_offset - self.shift) % 26 + ascii_offset
                )
                plaintext += shifted_char
            else:
                plaintext += char
        return plaintext
