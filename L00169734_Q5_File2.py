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
import re


def ssh_connection():
    try:
        ip = "192.168.61.129"  # vm details
        user_name = "l00169734".rstrip("\n")  # normally you would use getpass or hide the details
        user_password = "NeedThatPaper!21".rstrip("\n")
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        session.connect(ip.rstrip("\n"), username=user_name, password=user_password)
        connection = session.invoke_shell()
        session.exec_command("echo NeedThatPaper!21 | sudo -S apt install curl\n")  # install curl
        session.exec_command("mkdir Labs\n mkdir Labs/Lab1\n mkdir Labs/Lab2\n")  # create directories
        stdin, stdout, stderr = session.exec_command("ls -l --time=atime")  # detail last accessed times for files
        for line in iter(stdout.readline, ""):
            print(line, end="")

        vm_output = connection.recv(65535)
        if re.search(b"% Invalid input", vm_output):
            print("There was an error on vm {}".format(ip))
        else:
            print("Commands successfully executed on {}".format(ip))
        session.close()  # important to ensure session is closed

    except paramiko.AuthenticationException:
        print("Authentication Error")


ssh_connection()  # uses IP address above
