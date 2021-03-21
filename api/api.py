import json
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine

# Set up the flask app
app = Flask(__name__)

# Database settings for mongodb 
app.config['MONGODB_SETTINGS'] = {
    'db': 'cloud_db',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)

class User1(db.Document):
    """ MongoEngine.Document class to store user details """
    uid = db.IntField(required=True)
    name = db.StringField()
    mobile_number = db.StringField()
    age = db.IntField()


# Routing GET requests to one single method
@app.route('/user/', methods=['GET'])
@app.route('/user/id/<int:uid>/', methods=['GET'])
@app.route('/user/name/<string:name>/', methods=['GET'])
@app.route('/user/mobile-number/<string:number>/', methods=['GET'])
@app.route('/user/age/<int:age>/', methods=['GET'])
def query_records(uid=None,name=None,number=None,age=None):
    users = None

    # Fetching users based on the corresponding url details
    users = User1.objects(uid=uid) if uid is not None else \
            User1.objects(name=name) if name is not None else \
            User1.objects(mobile_number=number) if number is not None else \
            User1.objects(age=age) if age is not None else \
            User1.objects()


    if not users:
        # Returning error message in case of data not found
        return jsonify({'error': 'data not found'})
    else:
        # Returning all User1 objects in json format 
        return jsonify([{"ID":user.uid,"name":user.name, \
                        "mobile number":user.mobile_number, \
                        "age":user.age} for user in users])


# Routing POST requests
@app.route('/', methods=['POST'])
def create_record():

    # Api takes json format input
    record = request.json
    
    # uid is required parameter hence input validation
    if record.get('ID',None) is None:
        return jsonify({'error': 'ID is required'})

    # Creating a User1 object and inserting by .save() 
    user = User1(uid=record.get('ID'),
                name=record.get('name'),
                mobile_number=record.get('mobile number'),
                age=record.get('age'))
    user.save()

    # Returning success message after execution
    return jsonify({"Status":200,"body":"Data stored successfully"})

if __name__ == "__main__":
    app.run(debug=True)

