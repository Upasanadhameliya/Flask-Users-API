#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'cloud_db',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)

class User(db.Document):
    name = db.StringField()
    email = db.StringField()
    def to_json(self):
        return {"name": self.name,
                "email": self.email}


# @app.route('/<int:number>/')
# def incrementer(number):
#     return "Incremented number is " + str(number+1)

# @app.route('/<string:name>/')
# def hello(name):
#     return "Hello " + name


@app.route('/', methods=['GET'])
def query_records():
    name = request.args.get('name')
    user = User.objects(name=name).first()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify(user.to_json())

@app.route('/', methods=['POST'])
def create_record():

    print(request.json)
    # print(request.values)
    # print(request.files)
    # print(request.args)
    # print(request.data)
    # print(request.form)
    record = request.json
    user = User(name=record.get('name'),
                email=record.get('email'))
    user.save()

    return jsonify({"Hello":"World"})

# @app.route('/', methods=['POST'])
# def update_record():
#     record = json.loads(request.data)
#     user = User.objects(name=record['name']).first()
#     if not user:
#         return jsonify({'error': 'data not found'})
#     else:
#         user.update(email=record['email'])
#     return jsonify(user.to_json())

# @app.route('/', methods=['DELETE'])
# def delete_record():
#     record = json.loads(request.data)
#     user = User.objects(name=record['name']).first()
#     if not user:
#         return jsonify({'error': 'data not found'})
#     else:
#         user.delete()
#     return jsonify(user.to_json())

if __name__ == "__main__":
    app.run(debug=True)