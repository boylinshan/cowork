import os
import yaml
from host import Host


class HostGroup(object):
    def __init__(self, filepath):
        self._group = self._parse_yaml(filepath)

    def _parse_yaml(self, file_path):
        f = open(file_path)
        return yaml.load(f)
