import requests
from bs4 import BeautifulSoup


page=requests.get("https://www.youtube.com/watch?v=M_4PwhOiStU")

# print(page.status_code)
# print(page.content)

soup=BeautifulSoup(page.content,'html.parser')
# print(soup.prettify())
# print(list(soup.children)[1])

today=soup.find('div',class_="ytp-chapters-container")
print(today)
# today1=today.find_all(class_="ytp-chapter-hover-container")
# print(today1[0])
