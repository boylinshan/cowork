# -*- coding: utf-8 -*-
from lib.flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from tools.LogManager import LogManager

testPage = Blueprint('test_page', __name__, template_folder='templates')

@testPage.route('/config/', defaults={'page': 'config'})
@testPage.route('/config/<page>') 
def show(page):
	LogManager().get_logger(__name__).info(page)
	try:
		return render_template('pages/config.html')
	except TemplateNotFound:
		abort(404)
