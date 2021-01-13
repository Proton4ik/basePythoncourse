from functools import reduce

new_list = [i for i in range(100, 1002, 2)]
print("Cписок: ", new_list)
print("Проиведение всех элементов списка равно ", reduce(lambda x, y: x * y, new_list))

