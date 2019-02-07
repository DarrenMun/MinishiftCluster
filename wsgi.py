from flask import Flask

application = Flask(__name__)
db = SQLAlchemy(application)

@application.route('/')
def hello_world():
	return '<h1>Updated File</h1>'

if __name__ == '__main__':
	application.run()
