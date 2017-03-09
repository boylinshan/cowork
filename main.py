# -*- coding: utf-8 -*-
from lib.flask import Flask
from module.entryModule.entryPage import entryPage

app = Flask(__name__)
app.register_blueprint(entryPage)

if __name__ == '__main__':
	app.run(debug=True)