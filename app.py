from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
	return '<h1>Flask GIIIITTTTT</h1>'

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0')
