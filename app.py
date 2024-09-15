from flask import Flask, jsonify, request
from flask_cors import CORS
from db.models import db, db_create_user, db_get_user, db_get_users, db_update_user, db_delete_user

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/basic_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/')
def hello():
    return jsonify({"message": "Hello, world!"})

@app.route('/user/<id>', methods=['GET'])
def get_user(id: int):
    user = db_get_user(id)
    return jsonify(user.to_dict()), 200

@app.route('/user', methods=['GET'])
def get_users():
    users = db_get_users()
    return jsonify({"users": [user.to_dict() for user in users]}), 200

@app.route('/user', methods=['POST'])
def create_user():
    data = request.json
    user = db_create_user(data['username'], data['email'], data['password'])
    return jsonify(user.to_dict()), 200

@app.route('/user/<id>', methods=['PATCH'])
def update_user(id: int):
    data = request.json
    user = db_update_user(id, data.get('username'), data.get('email'), data.get('password'))
    return jsonify(user.to_dict()), 200

@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id: int):
    db_delete_user(id)
    return jsonify({}), 200

if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        # Uncomment if you make schema changes
        # db.drop_all()
        db.create_all()
    app.run(port=8080, debug=True)
