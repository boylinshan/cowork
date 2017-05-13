# -*- coding: utf-8 -*-
import Globals
from lib.flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from tools.LogManager import LogManager
from tools import methods

entryPage = Blueprint('entry_page', __name__, template_folder='templates')

@entryPage.route('/', defaults={'page': 'index'})
@entryPage.route('/<page>')
def show(page):
	try:
		host_groups = []	
		for name, host_group in Globals.cluster.iteritems():
			host_groups.append({'name': name, 'hosts': host_group['hosts']})

		return render_template('pages/%s.html' % page, cluster=host_groups)
	except TemplateNotFound:
		abort(404)
