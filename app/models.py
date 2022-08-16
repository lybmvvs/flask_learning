from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

class Roffle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fifa_name = db.Column(db.String(140))
    fifa_skill = db.Column(db.String(140))


    def __repr__(self):
        return '<Roffle {}>'.format(self.fifa_name)

class Fellas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fella_name = db.Column(db.String(140))
    fella_location = db.Column(db.String(140))