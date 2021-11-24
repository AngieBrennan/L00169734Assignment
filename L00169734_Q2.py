"""
#
# File        : L00169734_Q2.py
# Created     ：08/11/2021 21:45
# Author      ：Angela Brennan
# Version     ：v1.0.0
# Licencing   : (C) 2021 Angela Brennan, LYIT
#            Available under GNU Public License (GPL)
# Description ：Scrape the 192.168.61.129 page - parse it minimally for later processing
#
"""

if __name__ == '__main__':
    '''
      Main method of application

      Use  BeautifulSoup to scrape the 192.168.61.129 web page

      Parameters:
        none

      Returns:
        none
    '''
    """ scrape web page contents """

    """Print the external IP Address"""
import urllib.request

from bs4 import BeautifulSoup


def read_page_contents():
    """ scrape web page contents """
    print("Contents of Page")


url = "http://192.168.61.129"

request2 = urllib.request.urlopen(url)
request = request2.read()

if __name__ == "__main__":
    read_page_contents()

    print(request)
    """define soup and print"""
soup = BeautifulSoup(request, "html.parser")
print(soup.prettify())

"""pull out the number of times Apache is used"""
headings = soup.find_all("div", {"class": "section_header"})
print(headings)

word = soup.find_all("p", attrs={"class": "nav", "data-foo": "Apache2"})
print(word)
occurrences = word.count(word)
print('Number of occurrences of the word:', occurrences)
