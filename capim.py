#!/usr/bin/python3

import os
import flask
from flask.ext import assets

# CONFIGURAÇÃO
DEBUG = True
VERSAO = '3.0.0-alpha'
TITLE = 'MatrUFSC'
CAMPI = {
		'FLO': 'Florianópolis',
		'JOI': 'Joinville',
		'CBS': 'Curitibanos',
		'ARA': 'Araranguá',
		'BLU': 'Blumenau',
}
SEMESTRES = ['20151', '20142',]
PLANOS = 4
DIAS = {
		2: 'Segunda',
		3: 'Terça',
		4: 'Quarta',
		5: 'Quinta',
		6: 'Sexta',
		7: 'Sábado',
}
HORARIOS = {
		'0730': '07:30',
		'0820': '08:20',
		'0910': '09:10',
		'1010': '10:10',
		'1100': '11:00',
		'1330': '13:30',
		'1420': '14:20',
		'1510': '15:10',
		'1620': '16:20',
		'1710': '17:10',
		'1830': '18:30',
		'1920': '19:20',
		'2020': '20:20',
		'2110': '21:10',
}

app = flask.Flask(__name__)
app.config.from_object(__name__)
env = assets.Environment(app)
env.debug = True

env.register(
	'scripts',
	assets.Bundle(
		'coffee/main.coffee',
		filters='coffeescript',
		output='capim.js'
	)
)

env.register(
	'stylesheets',
	assets.Bundle(
		'stylus/main.styl',
		filters='stylus',
		output='capim.css'
	)
)

@app.route('/', methods=['GET'])
def index():
	return flask.render_template('index.html')

@app.route('/load/<ident>', methods=['GET'])
def load_data(ident):
	try:
		fp = open('/'.join(['data', '.'.join([ident, 'json'])]), 'rb')
		data = fp.read()
		fp.close()
	except IOError:
		flask.abort(404)
	return data, 200

@app.route('/store/<ident>', methods=['POST'])
def store_data(ident):
	try:
		fp = open('/'.join(['data', '.'.join([ident, 'json'])]), 'wb')
		fp.write(flask.request.data)
		fp.close()
	except IOError:
		flask.abort(403)
	return '', 204

if __name__ == '__main__':
	app.run()
