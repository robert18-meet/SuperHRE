from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(100),nullable = False)
    username = db.Column(db.String(100),nullable = False)
    passowrd = db.Column(db.String(100),nullable = False)
    email = db.Column(db.String)

    def __init__(self,nickname=None,username=None,password=None,email=None):
    	self.nickname = nickname
    	self.username = username
    	self.passowrd = password
    	self.email = email

class Songes(db.Model):
    __tablename__ = "Songs"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable = False)
    author = db.Column(db.String(100),nullable = False)
    URL = db.Column(db.String(100),nullable = False)

    def __init__(self,name=None,author=None,URL=None):
        self.name = name
    	self.author = author
    	self.URL = URL

#class Pages(db.Model):
 #   __tablename__ = "Pages"
  #  id = db.Column('id', db.Integer, primary_key=True)
   # posted_by = db.Column('posted_by', db.Integer, ForeignKey("Users.id"), nullable=False)
    #song = db.Column('song', db.Integer, ForeignKey("Songs.id"), nullable=False)
    #chords_lyrics = db.Column('chords_lyrics', db.String(500))
