from flask_sqlalchemy import SQLAlchemy
from flask import abort, Response

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)

    def __repr__(self):
        return f'User (id={self.id}, username={self.username})'
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at
        }

def db_create_user(username, email, password) -> User:
    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return user

def db_get_user(id: int) -> User:
    user = User.query.get(id)
    if not user:
        abort(Response(f'User with id {id} not found', 404))
    return user

def db_get_users() -> list[User]:
    return User.query.all()

def db_update_user(id: int, username: str | None = None, email: str | None = None, password: str | None = None) -> User:
    db.session.begin()
    user = db_get_user(id)
    if username:
        user.username = username
    if email:
        user.email = email
    if password:
        user.password = password
    db.session.commit()
    return user

def db_delete_user(id: int):
    user = db_get_user(id)
    db.session.delete(user)
    db.session.commit()
