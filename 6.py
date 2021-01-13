from itertools import count
from itertools import cycle
count_list = []
user_count = int(input("Введите число начала отсчета: "))
for i in count(user_count):
    count_list.append(i)
    if i >= 10:
        break
print("Результат Скрипт 1: ", count_list)
my_list = [1, 2, 3]
c = 0
for el in cycle(my_list):
    my_list.append(el)
    if c >= 10:
        break
    c = c + 1
print("Результат Скрипт 2: ", my_list)

