from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
	return '<h1>Flask GIIIITTTTT</h1>'

if __name__ == '__main__':
	application.run()
