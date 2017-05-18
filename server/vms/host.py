

class Host(object):
    # __slots__ =[]
    def __init__(self, ip, username, password, splunk_home):
        # self._monitor = Monitor(self, )
        self._ip = None
        self._username = None
        self._password = None
        self._splunk_home = None

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
