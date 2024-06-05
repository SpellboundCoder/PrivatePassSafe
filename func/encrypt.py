from dotenv import load_dotenv
import base64
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

load_dotenv()


class Encryption:
    def __init__(self, password: str):
        self.password = password
        self.salt = self.get_salt()
        self.key = self.get_key()

    @staticmethod
    def get_salt() -> bytes:
        salt = os.getenv('SALT')
        if salt is not None:
            return salt.encode()
        else:
            with open('.env', 'a') as file:
                file.write(f"SALT={os.urandom(16)}")

    def get_key(self):

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=1_000_000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(self.password.encode()))

        return key

    def encrypt_data(self, data: str):
        f = Fernet(self.key)
        encrypted_data = f.encrypt(data.encode())
        return encrypted_data

    def decrypt_data(self, encrypted_data: bytes):
        f = Fernet(self.key)
        decrypted_data = f.decrypt(encrypted_data)
        return decrypted_data.decode()
