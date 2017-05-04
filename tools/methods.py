# -*- coding: utf-8 -*-
'''
common methods used in the project
'''
import os
import const
from lib import yaml

def parse_yml_config_file(name):
	path ='{0}/{1}.yml'.format(const.CONFIG_FILE_PATH, name)
	host_group = {}
	with open(path, 'r') as f:
		config_file = yaml.load(f)
		for name, host_list in config_file.get('instance_roles',{}).iteritems():
			hosts = {}
			for host in host_list:
				hosts[host['splunkd_host']] = host
			host_group[name]  = {'hosts': hosts, 'host_num': len(hosts)}

	return host_group


