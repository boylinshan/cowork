import paramiko

def get_cpu_idle(host, username, password, port=22, type=None, isWindows=False ):
    connect = ssh_connect(host, port, username, password)
    cmd = "top -bi -n 2 -d 0.02"
    if type is not None:
        cmd += " | grep %s" % type
    stdin, stdout, stderr = connect.exec_command(cmd)
    info = stdout.readlines()

    if isWindows is False:
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


def release_memory(host, username, password, port=22):
    connect = ssh_connect(host, port, username, password)
    cmd = 'sudo sh -c "sync; echo 3 > /proc/sys/vm/drop_caches"'
    stdin, stdout, stderr = connect.exec_command(cmd)
    info = stdout.readlines()


def check_network(host, username, password, port=22, type=None, isWindows=False ):
    connect = ssh_connect(host, port, username, password)
    # todo
    pass


def ssh_connect(host, port, username, password):
    sshClient = paramiko.SSHClient()
    sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sshClient.connect(host, port, username, password)
    return sshClient

