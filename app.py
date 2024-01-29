from flask import Flask, request, jsonify, abort, make_response

from forms import RecordForm
from models import records_colletion

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

@app.route("/api/v1.0/records", methods=['POST'])
def create():
    if records_colletion.all() == []:
        record_id = 1
    else:
        record_id = records_colletion.all()[-1]['id'] + 1
    if not ("name" in request.json and "author" in request.json and "year" in request.json):
        abort(400)
    record = {
        "id": record_id,
        "name": request.json["name"],
        "author": request.json["author"],
        "year": request.json["year"],
    }
    records_colletion.create(record)
    records_colletion.save_all()
    return jsonify(records_colletion.get(record_id)), 201

@app.route("/api/v1.0/records", methods=['GET'])
def list_records():
    count = len(records_colletion.all())
    result = {
        "count": count,
        "records": records_colletion.all()
    }
    return jsonify(result), 200

@app.route("/api/v1.0/records/<int:id>", methods=['GET'])
def get(id):
    record = records_colletion.get(id)
    if record == []:
        abort(404)
    return jsonify(record), 200

@app.route("/api/v1.0/records/<int:id>", methods=['PUT'])
def update(id):
    record = {
        "id": id,
        "name": request.json["name"],
        "author": request.json["author"],
        "year": request.json["year"],
    }
    records_colletion.update(id, record)
    records_colletion.save_all()
    return jsonify(record), 200

@app.route("/api/v1.0/records/<int:id>", methods=['DELETE'])
def delete(id):
    deleted = records_colletion.delete(id)
    if not deleted:
        abort(404)
    records_colletion.save_all()
    return jsonify(deleted), 200

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)

if __name__ == "__main__":
    app.run(debug=True)