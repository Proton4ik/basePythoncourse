def my_func(x, y):
    i = 1
    while i < abs(y):
            x = x * x
            i = i + 1
    return 1 / x


base = float(input("Введите действительное положительное число: "))
while base <= 0:
    base = float(input("Число не может быть отрицательным или нулевым. Введите действительное положительное число: "))
up_num = int(input("Введите целое отрицательное число: "))
while up_num >= 0:
    up_num = int(input("Число не может быть положительным или нулевым. Введите целое отрицательное число: "))
result = my_func(base, up_num)
print("Возведение {} в степень {} дает результат: {:.2f}" .format(base, up_num, result))
print("Конец программы.")



