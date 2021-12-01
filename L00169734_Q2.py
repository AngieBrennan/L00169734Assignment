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

    import requests
    from bs4 import BeautifulSoup

    """  my ubuntu server address """
    url = "http://192.168.61.129/"

    """  searching for the number of times the word Apache appears on the webpage """
    the_word = "Apache"
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    words = doc.find(text=lambda text: text and the_word in text)
    print(words)
    count = len(words)
    print('\nUrl: {}\ncontains {} occurrences of word: {}'.format(url, count, the_word))
