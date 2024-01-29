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
        record = [record for record in self.all() if record['id'] == id]
        if record:
            return record[0]
        return []

    def create(self, data):
        self.records.append(data)

    def save_all(self):
        with open("records.json", "w") as f:
            json.dump(self.records, f)

    def update(self, id, data):
        self.records[id] = data
    
    def delete(self, id):
        record = self.get(id)
        if record == []:
            return False
        self.records.remove(record)
        return True

records_colletion = RecordsCollection()
