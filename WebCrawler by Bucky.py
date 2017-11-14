'''
THIS IS BUCKY WEB CRAWLER EXAMPLES 
'''

'''
HERE PART 1: Fetch all the href link in <a> tag of the page
'''

import requests
from bs4 import BeautifulSoup


def trade_spider():
    url = 'http://www.ckmusic.com.my'  # parent URL, rmb don't end with '/'
    source_code = requests.get(url)    # connect to the web page in url, store all source into source_code
    plain_text = source_code.text      # convert the source code to just Text
    soup = BeautifulSoup(plain_text, "html.parser")  # convert it to beautifulSoup Object, in order to use web crawler
    for link in soup.findAll('a', {'class': 'prodItemPic'}):  # look for tag <a>, where class='prodItemPic'
        href = url + link.get('href')  # from Tag, only take the href item
        print(href)


trade_spider()

input("Code by YH, Press Enter to Terminate =)")

