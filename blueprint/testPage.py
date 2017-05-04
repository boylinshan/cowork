# -*- coding: utf-8 -*-
import Globals
from lib.flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound
from tools.LogManager import LogManager

testPage = Blueprint('test_page', __name__, template_folder='templates')

@testPage.route('/config/<page>/', methods=['GET', 'POST'])
def show(page):
	try:
		host_group = request.form['host_group']
		host = request.form['host']
		action_type = request.form['type']
		host_list = Globals.cluster[host_group]['hosts'][host]
		return render_template('pages/config.html', host=host, action_type=action_type, host_list=host_list)
	except TemplateNotFound:
		abort(404)
