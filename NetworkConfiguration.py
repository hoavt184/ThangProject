# 3.1
# 3.3
# 3.4
# 3.5
import subprocess
class NetworkParameters:
    def IPForwarding():
        cmd = 'sysctl net.ipv4.ip_forward'
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
        
        (output, err) = p.communicate()
        print(output.decode('ascii'))
        return True


class TCPWrapper:
    def __init__(self):
        pass


class UncommonNetworkProtocols:
    def __init__(self):
        pass

class FirewallConfiguration:
    def __init__(self):
        pass