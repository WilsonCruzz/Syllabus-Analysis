import urllib.request
from bs4 import BeautifulSoup
import re
import ssl

# 忽略對SSL證書的驗證
ssl._create_default_https_context = ssl._create_unverified_context
webUrl=urllib.request.urlopen("https://barrie.ca")
html=webUrl.read()

soup=BeautifulSoup(html,"html.parser")
displayedText=soup.get_text()
listOfText=displayedText.split()
for word in listOfText:
    digits='0123456789'
    count=0
    for i in range (len(word)):
        if word[i] in digits:
            count=count+1
    if count==10:
        print(word)
    else:
        pass
