# 3.1
# 3.3
# 3.4
# 3.5
import subprocess
import re
from termcolor import colored

class NetworkParameters:
    def IPForwarding():
        cmd = 'grep "net\.ipv4\.ip_forward" /etc/sysctl.conf /etc/sysctl.d/* && grep "net\.ipv6\.conf\.all\.forwarding" /etc/sysctl.conf /etc/sysctl.d/*'
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
        # print("here")
        (output, err) = p.communicate()
        # print(output.decode('utf-8'))
        rules_pattern = r"(net\.ipv4\.ip_forward=[0,1])|(net\.ipv6\.conf\.all\.forwarding=[0,1])"
        search_pattern = re.findall(rules_pattern, output.decode("ascii"))
        # tmp = list(set(search_pattern))
        # print(list(set(search_pattern)))
        current = [re.sub(r"['\(\),\[\] ]",'',str(x)) for x in list(set(search_pattern))]
        # configs = [sorted(x.split('=')) for x in current]
        # print(current)
        # configs[0]['net.ipv4.ip_forward']
        for config in current:
            result = config.split('=')
            # print(config[1])
            if result[1] == '1':
                print(colored("IP forwarding is enabled: "+config, 'yellow'))
                print(colored("Recommendation: "+result[0]+"=0\n",'green'))

            
            
            # print(config)
        # tmp_1 = 
        # print(current)
        # print(type(str(tmp[0])))
        
        # print(str(list(set(search_pattern))[0]))
        
        # x = str(list(set(search_pattern))[1])
        # tmp = re.sub(r"'\(\)","",x)
        # print(tmp[0])
        # print(x.split("="))
        # print(list(set(search_pattern)))
        # a = [x if (str(x) != "'')" ) else None for x in search_pattern]

        # search_pattern = list(set(search_pattern))
        # print(search_pattern)
        # print(list(set(search_pattern)))
        # a = [x if (str(x) != "'')" ) else None for x in search_pattern]
        # print(a)
        # x = list(set(search_pattern))
        # x = x.replace(r"(|)","")
        # print(x)
        # print(list(x)[0])
        # print(output.decode('ascii'))
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