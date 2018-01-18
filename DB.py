from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://meet:123456@localhost/meet_db'
heroku = Heroku(app)
db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = "Users"
    id = db.Column('id', db.Integer, primary_key=True)
    nickname = db.Column('nickname', db.String(100))
    username = db.Column('username', db.String(100))
    passowrd = db.Column('password', db.String(100))
    email = db.Column('email', db.String)

class Songs(db.Model):
    __tablename__ = "Songs"
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100))
    author = db.Column('author', db.String(100))
    release_date = db.Column('release_date', db.String(100))
    genere = db.Column('genere', db.String(100))

class Pages(db.Model):
    __tablename__ = "Pages"
    id = db.Column('id', db.Integer, primary_key=True)
    posted_by = db.Column('posted_by', db.Integer, ForeignKey("Users.id"), nullable=False)
    song = db.Column('song', db.Integer, ForeignKey("Songs.id"), nullable=False)
    chords_lyrics = db.Column('chords_lyrics', db.String(500))

