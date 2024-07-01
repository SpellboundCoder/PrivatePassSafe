import secrets
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import os
import hashlib
from dotenv import load_dotenv


def get_salt() -> bytes:
    env_file_path = '.env'
    load_dotenv(env_file_path)
    salt = os.getenv('SALT')
    if salt:
        return salt.encode()
    else:
        with open(env_file_path, 'w') as file:
            file.write("# .env file \n")
            file.write(f"SALT={os.urandom(16)}")


def generate_password(length: int, upper: bool, num: bool, punc: bool):

    lowercase: str = ascii_lowercase
    uppercase = ascii_uppercase if upper else ''
    numbers: str = digits if num else ''
    symbols: str = punctuation if punc else ''
    characters: str = lowercase + uppercase + numbers + symbols
    password: list = [secrets.choice(lowercase)]
    password += secrets.choice(uppercase) if upper else ''
    password += secrets.choice(numbers) if num else ''
    password += secrets.choice(symbols) if punc else ''
    password += [secrets.choice(characters) for _ in range(length - len(password))]
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)


def hash_password(password, algorithm='sha512'):

    salt = get_salt()
    password_bytes = password.encode('utf-8')
    salted_password = salt + password_bytes
    hash_object = hashlib.new(algorithm)
    hash_object.update(salted_password)
    return hash_object.hexdigest()


def compare_hashes(hash1, hash2):
    return hash1 == hash2
