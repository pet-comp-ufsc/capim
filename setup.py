import setuptools

setuptools.setup(
		name='CAPIM',
		version='2.0.0-alpha',
		description='Combinador Automático de Possibilidades Interativo de Matrícula',
		url='https://github.com/ranisalt/capim',
		author='Ramiro Polla, Ranieri Althoff',
		author_email='ramiropolla@gmail.com, ranisalt@gmail.com',
		license='GNU/GPL Affero',
		install_requires=[
			'flask',
			'uwsgi',
		],
)
