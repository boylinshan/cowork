from ..monitor import Monitor

class Host(object):
    # __slots__ =[]
    def __init__(self, ip, username, password, splunk_home):
        # self._monitor = Monitor(self, )
        self._ip = ip
        self._username = username
        self._password = password
        self._splunk_home = splunk_home
        self._monitor = Monitor(ip, username, password)

    @property
    def ip(self):
        return self._ip

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def splunk_home(self):
        return self._splunk_home

    @property
    def Monitor(self):
        return self._monitor
