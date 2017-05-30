# -*- coding: utf-8 -*-
import Globals
import random
from web.lib.flask import Blueprint, render_template, abort, request, jsonify
from jinja2 import TemplateNotFound

clusterPage = Blueprint('cluster_page', __name__, template_folder='pages')

cpu_info_list = []
memory_info_list = []
disk_info_list = []
network_info_list = []

def generate(info_list):
	info_list.append(random.randint(1,100))
	if len(info_list) > 60:
		info_list = info_list[len(info_list)-60:]


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
		global cpu_info_list, memory_info_list, disk_info_list, network_info_list

		env = request.form['env']
		node = request.form['node']
		generate(cpu_info_list)
		generate(memory_info_list)
		generate(disk_info_list)
		generate(network_info_list)
		info_dict = {'cpu': cpu_info_list,
					 'memory': memory_info_list,
					 'disk': disk_info_list,
					 'network': network_info_list}

		return jsonify(info_dict)
	except TemplateNotFound:
		abort(404)
