def my_func():
    result = 0
    while True:
        user_str = input("Введите числа через пробел: ")
        user_str = user_str.split()
        i = 0
        while i < len(user_str):
            if user_str[i] == "q":
                print("Программа остановлена. Результат: ", result)
                return
            else:
                result = result + float(user_str[i])
                i = i + 1
        print("Сумма элеменотов равна ", result)


my_func()







