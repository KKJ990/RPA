import requests
from bs4 import BeautifulSoup


request=requests.get("https://library.gabia.com/")
soup = BeautifulSoup(request.content,'html.parser')
tags= soup.find_all(class_="eg-grant-element-0")



for tag in tags:
    print(tag.string)
    print(tag["href"])

