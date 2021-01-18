i = 1
with open("1.txt", "w") as f_obj:
    while True:
        user_str = input("Введите строку {}: ".format(i))
        if user_str == "":
            break
        print(user_str, file=f_obj)
        i = i + 1
