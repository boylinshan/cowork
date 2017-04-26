# -*- coding: utf-8 -*-
import const

from lib.flask import Flask
from blueprint.entryPage import entryPage
from blueprint.testPage import testPage
from scripts import test
from tools.LogManager import LogManager

app = Flask(__name__)
app.register_blueprint(entryPage)
app.register_blueprint(testPage)

if __name__ == '__main__':
	app.run(debug=True)