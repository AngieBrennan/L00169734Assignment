"""
#
# File        : L00169734_Q4.py
# Created     ：14/11/2021 21:31
# Author      ：Angela Brennan
# Version     ：v1.0.0
# Licencing   : (C) 2021 Angela Brennan, LYIT
#            Available under GNU Public License (GPL)
# Description ：Which ports are open - Display in a tidy format
#
"""

if __name__ == '__main__':
    '''
      Main method of application

      Find ports open and display data in a tidy format

      Parameters:
        none

      Returns:
        none
    '''
    """ #!/usr/bin/env python #include this shebang if running in a *nix environment """

    ''' Sockets code to carry out a port scan '''
    ''' Modified from:  '''

import socket
import subprocess
import sys
from datetime import datetime


def port_scan():
    """
    """
    # Clear the screen  #use clear if running in  *nix
    subprocess.call("cls", shell=True)

    # Ask for input
    remoteserver = input("Enter a remote host to scan: ")
    remoteserverip = socket.gethostbyname(remoteserver)

    # Print a nice banner with information on which host we are about to scan
    print("-" * 60)
    print("Please wait, scanning remote host", remoteserverip)
    print("-" * 60)

    # Check what time the scan started
    t1 = datetime.now()

    # Using the range function to specify ports (here it will scans all ports between 1 and 1024)
    # We also put in some error handling for catching errors

    try:
        #  try 1, 1025 if you have time
        for port in range(1, 81):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteserverip, port))
            if result == 0:
                print("Port {}: 	 Open".format(port))
            sock.close()
    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

    # Checking the time again
    t2 = datetime.now()

    # Calculates the difference of time, to see how long it took to run the script
    total = t2 - t1

    # Printing the information to screen
    print('Scanning Completed in: ', total)


if __name__ == "__main__":
    port_scan()
