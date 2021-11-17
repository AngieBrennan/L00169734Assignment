"""
#
# File        : L00169734_Q5_File2.py
# Created     ：17/11/2021 19:06
# Author      ：Angela Brennan
# Version     ：v1.0.0
# Licencing   : (C) 2021 Angela Brennan, LYIT
#            Available under GNU Public License (GPL)
# Description ：Create Dir structures & find when last accessed
#
"""

if __name__ == '__main__':
    '''
      Main method of application

      Create Dir structures & find when last accessed

      Parameters:
        none

      Returns:
        none
    '''

import paramiko
import time
import re


# Open SSH connection to the device
# first install ssh-server on the VM
#           sudo apt install openssh-server openssh-client
#
def ssh_connection(ip):
    """
    """
    try:
        username = "l00169734"
        password = "NeedThatPaper!21"
        print("Establishing a connection...")
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip.rstrip("\n"), username=username, password=password)
        connection = session.invoke_shell()
        connection.send(b"ls -al > longList.txt\n")  # unix command to list directory contents and save to file
        time.sleep(1)

        vm_output = connection.recv(65535)
        if re.search(b"% Invalid input", vm_output):
            print("There was at least one IOS syntax error on device {}".format(ip))
        else:
            print("Commands successfully executed on {}".format(ip))
        session.close()
    except paramiko.AuthenticationException:
        print("Authentication Error")


if __name__ == "__main__":
    # ssh_connection("192.168.61.129") #ip address of my VM, adjust to suit
    ssh_connection("192.168.61.129")
