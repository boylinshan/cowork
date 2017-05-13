import os
from hostgroup import HostGroup


class Cluster(object):
    def __init__(self):
        self._host_groups = {}
        self._init_env()

    def _init_env(self):
        config_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'configs')
        for root, dirs, files in os.walk(config_file_path, topdown=False):
            for f in files:
                print f
                if f.endswith('.yml'):
                    key = f.split(".")[0]
                    if self._host_groups.has_key(key) is False:
                        self._host_groups[key] = HostGroup( os.path.join(config_file_path, f) )

    @property
    def host_groups(self):
        pass

