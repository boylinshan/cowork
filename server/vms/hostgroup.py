import os
import yaml
from host import Host


class HostGroup(object):
    def __init__(self, filepath):
        self._group = self._parse_yaml(filepath)

    def _parse_yaml(self, file_path):
        group = {}
        f = open(file_path)
        content = yaml.load(f)
        for key in content.keys():
            key_list = []
            list = content[key]
            for li in list:
                host = Host(li['host']['ip'], li['host']['ssh_username'], li['host']['ssh_password'], li['splunk_home'])
                key_list.append(host)
            group[key] = key_list

        return group
