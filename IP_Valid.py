"""
#
# File        : IP_Valid.py
# Created     ：09/11/2021 21:42
# Author      ：Angela Brennan
# Version     ：v1.0.0
# Licencing   : (C) 2021 Angela Brennan, LYIT
#            Available under GNU Public License (GPL)
# Description ：Validate IP address is reachable
#
"""

if __name__ == '__main__':
    '''
      Main method of application

      Script to essentially ping a vm

      Parameters:
        none

      Returns:
        none
    '''
import sys

# Checking each of the 4 octets that make up a valid ip address

    def ip_addr_valid(list):
        """
        """
    for ip in list:
        ip = ip.rstrip("\n")
        octet_list = ip.split('.')

        if (len(octet_list) == 4) and (1 <= int(octet_list[0]) <= 223) and (int(octet_list[0]) != 127) and (
                int(octet_list[0]) != 169 or int(octet_list[1]) != 254) and (
                0 <= int(octet_list[1]) <= 255 and 0 <= int(octet_list[2]) <= 255 and 0 <= int(octet_list[3]) <= 255):
            continue

        else:
            print('\nThe invalid IP address is: {}\n'.format(ip))
            sys.exit()


if __name__ == "__main__":
    ip_addr_valid(["192.168.1.10", "270.10.5.60"])