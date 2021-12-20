# 6.1
# 6.2
import subprocess
import re
from termcolor import colored
class SystemFilePermissions:
    def __init__(self):
        pass
    def PermissionEtcPasswd():
        print("[*] Ensure permissions on /etc/passwd are configured checking....")

        cmd = 'stat /etc/passwd'
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
        # print("here")
        (output, err) = p.communicate()
        # print(output.decode('ascii'))
        # print(err)
        rules_pattern = r'Access: \(0644\/\-rw\-r\-\-r\-\-\)  Uid: \(    0\/    root\)   Gid: \(    0\/    root\)'
        search_pattern = re.findall(rules_pattern, output.decode("ascii"))
        # print(search_pattern)
        if len(search_pattern) > 0:
            print(colored("   [*] Ensure permissions on /etc/passwd are configured",'green'))
        else:
            print(colored("   [*] Ensure permissions on /etc/passwd are not configured",'yellow'))
            print(colored('''   [*] Recommendation:  chown root:root /etc/passwd && chmod 644 /etc/passwd''','green'))

    def PermissionEtcShadow():
        print("[*] Ensure permissions on /etc/shadow are configured checking....")

        cmd = 'stat /etc/shadow'
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
        # print("here")
        (output, err) = p.communicate()
        # print(output.decode('ascii'))
        # print(err)
        rules_pattern = r'Access: \(0640\/\-rw\-r\-\-\-\-\-\)  Uid: \(    0\/    root\)   Gid: \(   42\/  shadow\)'
        search_pattern = re.findall(rules_pattern, output.decode("ascii"))
        # print(search_pattern)
        if len(search_pattern) > 0:
            print(colored("   [*] Ensure permissions on /etc/shadow are configured",'green'))
        else:
            print(colored("   [*] Ensure permissions on /etc/shadow are not configured",'yellow'))
            print(colored('''   [*] Recommendation: chown root:shadow /etc/shadow && chmod o-rwx,g-wx /etc/shadow''','green'))

    def PermissionEtcGroup():
        print("[*] Ensure permissions on /etc/group are configured checking....")

        cmd = 'stat /etc/group'
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
        # print("here")
        (output, err) = p.communicate()
        # print(output.decode('ascii'))
        # print(err)
        rules_pattern = r'Access: \(0644\/\-rw\-r\-\-r\-\-\)  Uid: \(    0\/    root\)   Gid: \(    0\/    root\)'
        search_pattern = re.findall(rules_pattern, output.decode("ascii"))
        # print(search_pattern)
        if len(search_pattern) > 0:
            print(colored("   [*] Ensure permissions on /etc/group are configured",'green'))
        else:
            print(colored("   [*] Ensure permissions on /etc/group are not configured",'yellow'))
            print(colored('''   [*] Recommendation: chown root:root /etc/group && chmod 644 /etc/group''','green'))


    def PermissionHostDeny():
        print("[*] Host deny configured checking....")

        cmd = 'stat /etc/hosts.allow'
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
        # print("here")
        (output, err) = p.communicate()
        # print(output.decode('ascii'))
        # print(err)
        rules_pattern = r'Access: \(0644\/\-rw\-r\-\-r\-\-\)  Uid: \(    0\/    root\)   Gid: \(    0\/    root\)'
        search_pattern = re.findall(rules_pattern, output.decode("ascii"))
        # print(search_pattern)
        if len(search_pattern) > 0:
            print(colored("   [*] Ensure permissions on /etc/hosts.deny are configured ",'green'))
        else:
            print(colored("   [*] Ensure /etc/hosts.deny are not configured",'yellow'))
            print(colored('''   [*] Recommendation: chown root:root /etc/hosts.deny && chmod 644 /etc/hosts.deny''','green'))

class UserandGroupSettings:
    def __init__(self):
        pass