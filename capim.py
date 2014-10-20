#!/usr/bin/python3

import flask
app = flask.Flask(__name__)

@app.route('/load/<ident>', methods=['GET'])
def load_data(ident):
	try:
		fp = open('/'.join(['data', '.'.join([ident, 'json'])]), 'rb')
		data = fp.read()
		fp.close()
	except IOError:
		flask.abort(404)
	return data, 200

@app.route('/store', methods=['PUT'])
def store_data():
	flask.abort(501)

if __name__ == '__main__':
	app.run()
