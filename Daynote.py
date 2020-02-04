import re
import requests
import os
from bs4 import BeautifulSoup
 
url = 'https://baidu.com/'
html = requests.get(url).text 
#获取网页内容
print(html)
