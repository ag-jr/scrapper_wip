from datetime import date

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sqlite3

# DB Connection and cursor configuration.
db = sqlite3.connect('favorites.db')
db.row_factory = lambda cursor, row: row[0]
cursor = db.cursor()
# cursor.execute("CREATE TABLE product_list (loja text,serial text,name text, price text, date date)")

# selenium browser configuration.
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
d = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
d.implicitly_wait(10)

data = date.today()
data_atual = f'{data.day}/{data.month}/{data.year}'


def salvar_banco(loja, serial, name, price, data_atual):
    cursor.execute("INSERT INTO product_list VALUES (?,?,?,?,?)", (loja, serial, name, price, data_atual))

def extrator_id():
    # to add a new single product url to the DB/Favorites list, while also performing the first search.
    print('Endereço do produto desejado: ')
    url = input()

    if 'aliexpress' in url:
        serial = url.split('/item/', 1)[1].split('.html?', 1)[0]
        d.get(f'https://www.aliexpress.com/item/{serial}.html')
        price = d.find_element_by_class_name('product-price-value')
        name = d.find_element_by_class_name('product-title-text')
        loja = 'aliexpress'
        price = price.text
        name = name.text
        salvar_banco(loja, serial, name, price, data_atual)

    elif 'amazon' in url:
        serial = url.split('/dp/', 1)[1].split('/ref=sr_1', 1)[0]
        d.get(f'https://www.amazon.com.br//dp/{serial}/')
        price = d.find_element_by_id('price_inside_buybox')
        name = d.find_element_by_id('productTitle')
        loja = 'amazon'
        price = price.text
        name = name.text
        salvar_banco(loja, serial, name, price, data_atual)

    else:
        print('Url não suportada, tente Amazon ou Aliexpress.')

    print(f'{loja},{serial},{name},{price},{data_atual}')

def gera_lista(loja):
    # Searches the DB/Favorites for every item on a store and generates a set for group search for price update.
    search = loja
    cursor.execute("SELECT serial FROM product_list WHERE loja LIKE (?)",('%'+search+'%',))
    result = cursor.fetchall()
    result = list(set(result))
    return result


def busca_preco(loja):
    # Goes through the list for mass updates and saves the new info as a new item.

    if loja == 'aliexpress':
        for serial in gera_lista(loja):
            d.get(f'https://www.aliexpress.com/item/{serial}.html')
            price = d.find_element_by_class_name('product-price-value')
            price = price.text
            name = d.find_element_by_class_name('product-title-text')
            name = name.text
            print(name, price)
            salvar_banco(loja, serial, name, price, data_atual)
    elif loja == 'amazon':
        for serial in gera_lista(loja):
            d.get(f'https://www.amazon.com.br//dp/{serial}/')
            price = d.find_element_by_id('price_inside_buybox')
            price = price.text
            name = d.find_element_by_id('productTitle')
            name = name.text
            print(name, price)
            salvar_banco(loja, serial, name, price, data_atual)

