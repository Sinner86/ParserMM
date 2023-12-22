import scrapy as scrapy

scrapy shell
url = 'https://megamarket.ru/catalog/details/monitor-sunwind-chernyy-sun-m27bg130-100045194336/#?details_block=prices'
r = scrapy.Request(url)
fetch(r)
# d