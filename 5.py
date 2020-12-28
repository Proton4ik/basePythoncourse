start_list = [7, 5, 3, 3, 2]
while True:
    i = 0
    user_el = int(input("Введите натуральное число: "))
    while i < len(start_list):
        if user_el > start_list[i]:
           start_list.insert(i, user_el)
           print("Обновленный список: ", start_list)
           break
        elif user_el == start_list[i]:
           start_list.insert(i + 1, user_el)
           print("Обновленный список: ", start_list)
           break
        elif user_el < start_list[i] and i == (len(start_list) - 1):
            start_list.append(user_el)
            print("Обновленный список: ", start_list)
            break
        elif user_el < start_list[i]:
            i = i + 1
