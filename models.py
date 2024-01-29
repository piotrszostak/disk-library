import json


class RecordsCollection:
    def __init__(self):
        try:
            with open("records.json", "r") as f:
                self.records = json.load(f)
        except FileNotFoundError:
            self.records = []

    def all(self):
        return self.records

    def get(self, id):
        return self.records[id]

    def create(self, data):
        data.pop("csrf_token")
        self.records.append(data)

    def save_all(self):
        with open("records.json", "w") as f:
            json.dump(self.records, f)

    def update(self, id, data):
        data.pop("csrf_token")
        self.records[id] = data

records = RecordsCollection()
