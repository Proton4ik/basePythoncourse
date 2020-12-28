n = int(input("Введите количество симолов в списке: "))
i = 0
my_list = []
while i < n:
    element = input("Введите значение элемента {}: " .format(i))
    my_list.append(element)
    i += 1
print("Исходный список: ", my_list)
i = 0
if (len(my_list) % 2) == 0:
    while i < len(my_list):
        my_list.insert(i, my_list[i + 1])
        my_list.pop(i + 2)
        i = i + 2
    print("Новый список: ", my_list)
else:
    while i < (len(my_list) - 1):
        my_list.insert(i, my_list[i + 1])
        my_list.pop(i + 2)
        i = i + 2
    print("Новый список: ", my_list)
print("Конец программы")
