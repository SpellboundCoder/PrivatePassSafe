import json


def load_dict(path):
    with open(file=path, mode='r') as file:
        return json.load(file)


def save_dict(dictionary, path):
    with open(file=path, mode='w') as file:
        json.dump(dictionary, file)
