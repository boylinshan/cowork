# -*- coding: utf-8 -*-
from lib.flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from tools.LogManager import LogManager
from tools import methods

entryPage = Blueprint('entry_page', __name__, template_folder='templates')

@entryPage.route('/', defaults={'page': 'entry'})
@entryPage.route('/<page>')
def show(page):
	try:
		nodes_list = []
		for node in methods.get_all_nodes():
			nodes_list.append(methods.get_node_data(node))

		return render_template('pages/%s.html' % page, nodes=nodes_list)
	except TemplateNotFound:
		abort(404)
