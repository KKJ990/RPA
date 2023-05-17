import requests
from bs4 import BeautifulSoup

requests =requests.get("https://finance.naver.com/sise/sise_quant.naver".encode("UTF-8"))
soup = BeautifulSoup(requests.content,'html.parser')

for tag in soup.find_all(class_="tltle"):
    print(tag.string)