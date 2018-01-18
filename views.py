from FlaskRouter import *

@app.route('/', methods=["GET","POST"])
def homepage():
	if request.method == 'POST':
		if request.form['Username'] == '1':
			if request.form['Password'] == '1':
				return render_template('HomePage_D.html',nick = request.form['Username'])

	return render_template('HomePage.html')

@app.route('/Register',methods=["GET","POST"])
def Register():
	if request.method == 'POST':

		new_username = request.form['Username']
		new_password = request.form['Password']
		new_nickname = request.form['Nickname']
		new_email = request.form['Email']

		return render_template('HomePage_D.html',nick=new_nickname)
	else:
		return render_template('Register.html')

@app.route('/Minigame')
def Minigame():
	return render_template('Minigame.html')   

@app.route('/Songs')
def Songs():
	return render_template('Songs.html')  