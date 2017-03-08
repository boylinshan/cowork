from lib.flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Greeeat!, Daniel got 1 point'

if __name__ == '__main__':
	app.run()