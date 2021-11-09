"""
#
# File        : L00169734_Q3.py
# Created     ：08/11/2021 18:37
# Author      ：Angela Brennan
# Version     ：v1.0.0
# Licencing   : (C) 2021 Angela Brennan, LYIT
#            Available under GNU Public License (GPL)
# Description ：Q1. Connect to virtual machine using ssh port
#
"""

if __name__ == '__main__':
    '''
      Main method of application

      Using paramiko to connect to VM

      Parameters:
        none

      Returns:
        none
    '''
    #  Use paramiko to connect to vm

    import paramiko
    import time
    import re


    def ssh_connection(ip):
        """

        :param ip:
        """
        try:
            username = "l00169734"  # In an automation script read data from file
            password = "l00169734"  # never hard code finally
            print("Establishing a connection...")
            session = paramiko.SSHClient()
            session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            session.connect(ip.rstrip("\n"), username=username,
                            password=password)
            connection = session.invoke_shell()
            connection.send(b"ls > dir_contents.txt\n")  # unix command to list  directory contents and save to file
            time.sleep(1)
            vm_output = connection.recv(65535)
            if re.search(b"% Invalid input", vm_output):
                print("There was an error on vm {}".format(ip))
            else:
                print("Commands successfully executed on {}".format(ip))
                session.close()
        except paramiko.AuthenticationException:
            print("Authentication Error")
        ssh_connection("192.168.1.7")  # ip address of my VM, adjust to suit
