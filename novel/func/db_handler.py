import json


def load_json(path):
    with open(path,'r',encoding='utf-8') as f:
        file = json.load(f)
        return file
        
