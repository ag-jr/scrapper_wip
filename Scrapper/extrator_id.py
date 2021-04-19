def extrator_id():
    print('Endereço do produto desejado: ')
    url = input()

    if 'aliexpress' in url:
        serial = url.split('/item/', 1)[1].split('.html?', 1)[0]
        loja = aliexpress
        price = d.find_element_by_class_name('product-price-value')
        name = d.find_element_by_class_name('product-title-text')
    elif 'amazon' in url:
        serial = url.split('/dp/', 1)[1].split('/ref=sr_1', 1)[0]
        price = d.find_element_by_id('price_inside_buybox')
        name = d.find_element_by_id('productTitle')
    else:
        print('Url não suportada, tente Amazon ou Aliexpress.')

