from flask import Flask, render_template, url_for, request
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

class Songes(db.Model):
    __tablename__ = "Songs"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable = False)
    author = db.Column(db.String(100),nullable = False)
    URL = db.Column(db.String(100),nullable = False)

@app.route('/', methods=["GET","POST"])
def homepage():
	if request.method == 'POST':
		check = Users.query.filter_by(username=request.form['Username'], passowrd=request.form['Password']).first()
		if not(check is None):
			return render_template('HomePage_D.html',nick = check.nickname)

	return render_template('HomePage.html')

@app.route('/Register',methods=["GET","POST"])
def Register():
	if request.method == 'POST':
		if Users.query.filter_by(username=request.form['Username']).first() is None:
			new_user = Users()
			new_user.nickname = request.form['Nickname']
			new_user.username = request.form['Username']
			new_user.passowrd = request.form['Password']
			new_user.email = request.form['Email']
			db.session.add(new_user)
			db.session.commit()
			return render_template('HomePage_D.html',nick=new_user.nickname)
	return render_template('Register.html')

@app.route('/Minigame')
def Minigame():
	return render_template('Minigame.html')   

@app.route('/Songs')
def Songs():
	getList = Songes.query.all()
	return render_template('Songs.html',getList = getList)

@app.route('/HomePage_D', methods=["GET","POST"])
def LoggedIn():
	if(request.method == 'POST'):
		new_song = Songes()
		new_song.name = request.form['Name']
		new_song.author = 'doesntMetter'
		new_song.URL = request.form['URL']
		db.session.add(new_song)
		db.session.commit()
		return render_template('HomePage.html')


if __name__ == '__main__':
	app.run(debug=True)