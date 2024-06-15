import json


def save_data_to_json(data: dict, filename: str):
    with open(filename, 'w') as file:
        json.dump(data, file)


# Helper function loading json file as recipes dictionary
def load_data(filename: str) -> dict:
    file = open(filename)
    data = json.load(file)
    return data
