def busca_preco(loja):
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