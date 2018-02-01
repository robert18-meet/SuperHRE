from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from DB import *

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
			new_user = Users(request.form['Nickname'],request.form['Username'],request.form['Password'],request.form['Email'])
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
		new_song = Songes(request.form['Name'],'doesntMetter',request.form['URL'])
		db.session.add(new_song)
		db.session.commit()
		return render_template('HomePage.html')


if __name__ == '__main__':
	app.run(debug=True)