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

      Use  BeautifulSoup to scrape the lyit web page

      Parameters:
        none

      Returns:
        none
    '''
    """ scrape web page contents """

    import requests
    from bs4 import BeautifulSoup

    """  LYIT Webpage """
    url = "https://www.lyit.ie/"

    the_word = "LYIT"
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    """  creating a list of all common heading tags"""

   ##  headings = ["h1", "h2", "h3", "h4", "h5", "h6"]
    ##for tags in doc.find_all(headings):
      ##  print(tags.name + ' -> ' + tags.text.strip())

    """  searching for the number of times the word Apache appears on the webpage """
    words = doc.find(text=lambda text: text and the_word in text)
    print(words)
    count = len(words)
    print('\nUrl: {}\ncontains {} occurrences of word: {}'.format(url, count, the_word))
