shopping_list = {
    'piekarnia' : ['chleb', 'bułka', 'pączek'],
    'warzywniak' : ['marchew', 'seler', 'rukola']
}
for shop, products in shopping_list.items():
    print(f'Idę do {shop} i kupuję tam : {products}.')