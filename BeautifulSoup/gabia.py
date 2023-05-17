import requests
from bs4 import BeautifulSoup

requests = requests.get("https://webhosting.gabia.com/container/service")
soup =BeautifulSoup(requests.content,"html.parser")

python = soup.find_all(id="_tab1-2")
tags = python[0].div.div.p.next_element.next_element.next_element.next_element.next_element.next_element


print(tags)