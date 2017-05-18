
import paramiko

class Monitor(object):
    def __init__(self, ip, username, password):
        self._ip = ip
        self._username = username
        self._password = password
        self.iswindows = False
        self._sshconnection = None
        self._port = 22

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
    def sshconnection(self):
        if self._sshconnection is None:
            self.ssh_connect()
        return self._sshconnection

    @property
    def port(self):
        return self._port

    def ssh_connect(self):
        sshClient = paramiko.SSHClient()
        sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        sshClient.connect(self.ip, self.port, self.username, self.password)
        self._sshconnection = sshClient


    def get_cpu_idle_percent(self):
        connect = self.sshconnection
        cmd = "top -bi -n 2 -d 0.02 | grep Cpu"
        stdin, stdout, stderr = connect.exec_command(cmd)
        info = stdout.readlines()

        if self.iswindows is False:
            list = info[1].split(",")
            for li in list:
                if "id" in li:
                    if '%' in li:
                        cpuusage = li.strip().split("%")[0]
                    else:
                        cpuusage = li.strip().split(" ")[0]
                    return float(cpuusage)
            return 0
        else:
            num_cpu = len(info) / 2  # number of cpu cores
            cur_usage = 0
            for i in range(num_cpu, num_cpu * 2):
                line = info[i]
                if 'Cpu' in line:
                    usage = float(line.split(':')[1].split('/')[0].strip())
                    cur_usage += usage
            print cur_usage / num_cpu
            return int(cur_usage / num_cpu)

    # def release_memory(host, username, password, port=22):
    #     connect = ssh_connect(host, port, username, password)
    #     cmd = 'sudo sh -c "sync; echo 3 > /proc/sys/vm/drop_caches"'
    #     stdin, stdout, stderr = connect.exec_command(cmd)
    #     info = stdout.readlines()
    #
    # def check_network(host, username, password, port=22, type=None, isWindows=False):
    #     connect = ssh_connect(host, port, username, password)
    #     pass
    #
    # def ssh_connect(host, port, username, password):
    #     sshClient = paramiko.SSHClient()
    #     sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     sshClient.connect(host, port, username, password)
    #     return sshClient