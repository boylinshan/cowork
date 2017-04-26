# -*- coding: utf-8 -*-
from lib.flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound
from tools.LogManager import LogManager

testPage = Blueprint('test_page', __name__, template_folder='templates')

@testPage.route('/config/<page>/', methods=['GET', 'POST'])
def show(page):
	a = request.form['code']
	try:
		return render_template('pages/config.html')
	except TemplateNotFound:
		abort(404)
