# -*- coding: utf-8 -*-
'''
common methods used in the project
'''
import os
import const
from lib import yaml


def parse_yml_config_file(name):
    path = '{0}/{1}.yml'.format(const.CONFIG_FILE_PATH, name)
    host_group = {}
    with open(path, 'r') as f:
        config_file = yaml.load(f)
        for name, host_list in config_file.get('instance_roles', {}).iteritems():
            host_group[name] = host_list
            # hosts = {}
            # for host in host_list:
            #     hosts[host['splunkd_host']] = host
            # host_group[name] = {'hosts': hosts, 'host_num': len(hosts)}

    return host_group


def init_env():
    info_dict = {}
    if info_dict.has_key('multisite') is False:
        info_dict['multisite'] = parse_yml_config_file('stability_multisite')
    if info_dict.has_key('multisite_windows') is False:
        info_dict['multisite_windows'] = parse_yml_config_file('stability_multisite_windows')
    if info_dict.has_key('multisite_debug') is False:
        info_dict['multisite_debug'] = parse_yml_config_file('stability_multisite_debug')
    return info_dict