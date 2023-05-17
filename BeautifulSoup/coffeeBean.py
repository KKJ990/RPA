import requests
from bs4 import BeautifulSoup

i=1
while(True):
    request =requests.get(f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={i}".encode("UTF-8"))
    soup = BeautifulSoup(request.content,'html.parser')


    for tag in soup.find_all(class_="center_t"):
        print(tag.string)



    if soup.find(class_="on") ==None:
        break

    i=i+10

