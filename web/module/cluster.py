# -*- coding: utf-8 -*-
import Globals
from web.lib.flask import Blueprint, render_template, abort, request, jsonify
from jinja2 import TemplateNotFound

clusterPage = Blueprint('cluster_page', __name__, template_folder='pages')

@clusterPage.route('/')
def cluster():
	try:
		cluster = [{'name':'123', 'node_list':[123]}]
		return render_template('cluster.html', cluster=cluster)
		#return render_template('index.html')
	except TemplateNotFound:
		abort(404)

@clusterPage.route('/node', methods=['POST'])
def node():
	try:
		env = request.form['env']
		node = request.form['node']
		info = [{'111':12}, {'222':22}]
		return jsonify(info)
	except TemplateNotFound:
		abort(404)
