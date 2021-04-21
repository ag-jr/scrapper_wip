from bs4 import BeautifulSoup

import requests

html = requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/370/torres-rs").content
soup = BeautifulSoup(html, 'html.parser')

# print(soup.prettify())

temperatura_min = soup.find("span", class_="_margin-r-20")
temperatura_max = soup.find(id="max-temp-1")

print(f'Previsao do tempo para torres Torres é Min {temperatura_min.string} e Max {temperatura_max.string}')

# html = requests.get(
#     'https://pt.aliexpress.com/item/33059383439.html?spm=a2g03.12010612.0.0.66531f'
#     '07TVW8WC&gps-id=pcStoreJustForYou&scm=1007.23125.1'
#     '37358.0&scm_id=1007.23125.137358.0&scm-url=1007.23125.'
#     '137358.0&pvid=1d2d97a7-4387-4f7d-86b9-b530c7b2953a').content
#
# soup = BeautifulSoup(html, 'html.parser')
#
# valor = soup.find("h1", class_='product-price-value')
#
# print(valor)

# <span class="product-price-value" itemprop="price" data-spm-anchor-id="a2g0o.detail.1000016.i4.765f5b21Mn3RID">
#R$ 1.254,30 - 1.260,51
# </span>