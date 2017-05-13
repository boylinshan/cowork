# -*- coding: utf-8 -*-
import Globals
from lib.flask import Blueprint, render_template, abort, request, jsonify
from jinja2 import TemplateNotFound
from tools.LogManager import LogManager

testPage = Blueprint('test_page', __name__, template_folder='templates')

@testPage.route('/config/', methods=['GET', 'POST'])
def show():
	try:
		host_group = request.form['host_group']
		host = request.form['host']    
		info = Globals.cluster[host_group]['hosts'][host]
		return jsonify(info)
	except TemplateNotFound:
		abort(404)
