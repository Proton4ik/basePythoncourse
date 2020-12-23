a = int(input("Введите целое положительное число: "))
x = a
max_num = 0
while a >= 1:
    num = a % 10
    if num > max_num:
        max_num = num
    a = a // 10
print ("Самая большая цифра в числе {}: {}" .format(x, max_num))
print ("Конец программы.")
