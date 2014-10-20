#!/usr/bin/python3

import flask
app = flask.Flask(__name__)

@app.route('/load', methods=['GET'])
def load_data():
	flask.abort(501)

@app.route('/store', methods=['PUT'])
def store_data():
	flask.abort(501)

if __name__ == '__main__':
	app.run()
