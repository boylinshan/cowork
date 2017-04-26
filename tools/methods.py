# -*- coding: utf-8 -*-
'''
common methods used in the project
'''

import os
import const

def get_all_nodes():
	nodes = []
	for filename in os.listdir(const.CONFIG_FILE_PATH):
		if filename.endswith(const.FILE_EXTENSIONS):
			if not filename.startswith('__init__'):
				nodes.append(filename[:filename.rfind('.')])
	return nodes

def get_node_data(name):
	module = __import__(const.CONFIG_FILE_PATH, globals(), locals(), [name])
	node = getattr(module, name, object)
	data = getattr(node, 'data', {})
	return data

