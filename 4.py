user_str = input("Введите несколько слов через пробел: ")
user_list = user_str.split()
i = 0
while i < len(user_list):
    if len(user_list[i]) < 11:
        print(i + 1, user_list[i])
    else:
        print(i + 1, user_list[i][0:10])
    i = i +1
print("Конец программы")
