n = int(input("Введите общее количество наименований товаров на складе: "))
while n <= 0:
    n = int(input("Введите общее количество всех товаров на складе. Их больше 0: "))
i = 0
products_list = []
while i < n:
    name = input("Введите название товара {}: " .format(i + 1))
    cost = float(input("Введите цену товара {}: " .format(i + 1)))
    while cost <= 0:
            cost = float(input("Мы не работаем в убыток. Введите цену товара {}: ".format(i + 1)))
    num = int(input("Введите количество товара {}: " .format(i + 1)))
    while num <= 0:
        num = int(input("Введите количество товара {}. Их больше 0: ".format(i + 1)))
    value = input("Введите единицу измерения количества товара {}: " .format(i + 1))
    product_cort = (i + 1, {'название': name, 'цена': cost, 'количество': num, 'ед': value})
    products_list.append(product_cort)
    i += 1
for x in products_list: print(x)
name_list = []
cost_list = []
num_list = []
value_list = set()
i = 0
while i < len(products_list):
    name_list.append(products_list[i][1].get('название'))
    cost_list.append(products_list[i][1].get('цена'))
    num_list.append(products_list[i][1].get('количество'))
    value_list.add(products_list[i][1].get('ед'))
    i += 1
dict_analyze = {'название' : name_list, 'цена' : cost_list, 'количество' : num_list, 'ед' : value_list}
print("Аналитика: ")
for key in dict_analyze:
    print(key, ":", dict_analyze[key])
print("Конец программы.")


