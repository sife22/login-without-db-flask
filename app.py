from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login', methods=['GET'])
def login():
	return render_template('login.html')

@app.route('/handleLogin', methods=["POST", "GET"])
def handleLogin():
	db = {
	'user1':'pass1',
	'user2':'pass2',
	'user3':'pass3'
	}

	username = request.form['username']
	password = request.form['password']

	if username not in db:
		info = "username incorrect"
		return render_template('index.html', info=info)
	
	else :
		if db[username] != password:
			info = "maybe password incorrect"
			return render_template('index.html', info=info)
		else : 
			info = "hello to your world"
			return render_template('world.html', info=info)
		info
