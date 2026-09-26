import json

FILE_NAME = 'tasks.json'

def load_tasks():
    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []