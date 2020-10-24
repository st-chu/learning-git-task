shopping_list = {
    'piekarnia' : ['chleb', 'bułka', 'pączek'],
    'warzywniak' : ['marchew', 'seler', 'rukola']
}
number_off_products = 0


for shop, products in shopping_list.items():
    for product in products:
        if product.lower() == 'pączek':
            products.remove('pączek')


for shop, products in shopping_list.items():
    if shop == 'warzywniak':
        shopping_list[shop].append('szparagi')


for shop, products in shopping_list.items():
    number_off_products += len(products)
    shop = shop.capitalize()
    for i in range(len(products)):
        products[i] = products[i].capitalize()
    print(f'Idę do {shop} i kupuję tam : {products}.')


print(f'W sumie kupuję {number_off_products} produktów')