from bs4 import BeautifulSoup
import requests

url = 'https://megamarket.ru/catalog/details/monitor-sunwind-chernyy-sun-m27bg130-100045194336/#?details_block=prices'
url2 = 'https://www.banki.ru'

# соединение с сайтом ММ
page = requests.get(url2)
print(page.status_code)

filteredNews = []
allNews = []
soup = BeautifulSoup(page.text, "html.parser")
print(soup)
# f = open('MM.txt', 'w')
# f.write(str(soup))
# f.close()
# allNews = soup.findAll('span', class_='bonus-amount')
# print(allNews)