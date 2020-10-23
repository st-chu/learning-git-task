shopping_list = {
    'piekarnia' : ['chleb', 'bułka', 'pączek'],
    'warzywniak' : ['marchew', 'seler', 'rukola']
}
for shop, products in shopping_list.items():
    shop = shop.capitalize()
    for i in range(len(products)):
        products[i] = products[i].capitalize()
    print(f'Idę do {shop} i kupuję tam : {products}.')