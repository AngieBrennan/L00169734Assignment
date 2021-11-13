"""
#
# File        : L00169734_Q2.py
# Created     ：08/11/2021 21:45
# Author      ：Angela Brennan
# Version     ：v1.0.0
# Licencing   : (C) 2021 Angela Brennan, LYIT
#            Available under GNU Public License (GPL)
# Description ：Scrape the LYIT web page - parse it minimally for later processing
#
"""

if __name__ == '__main__':
    '''
      Main method of application

      Use  BeautifulSoup to scrape the LYIT web page

      Parameters:
        none

      Returns:
        none
    '''
    """Print the external IP Address"""

import urllib.request


def read_page_contents():

    """ scrape web page contents """
    print("Contents of Page")


url = "http://www.lyit.ie"

request2 = urllib.request.urlopen(url)
request = request2.read()


print(request)

if __name__ == "__main__":
    read_page_contents()
