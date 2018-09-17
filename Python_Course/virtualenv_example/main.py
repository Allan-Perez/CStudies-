from flask import Flask 

app = Flask(__name__)


@app.route('/')
def hello_world():
	return 'Hello, world. You\'re now a software engineer'


@app.route('/hello')
def what_ya_doin():
	return 'Whatafack are you looking for?'

if __name__ == '__main__':
	app.run()