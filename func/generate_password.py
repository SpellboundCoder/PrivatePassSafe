import secrets
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


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

