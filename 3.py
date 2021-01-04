def my_func(a, b, c):
   if a >= b and c >= b:
       return a + c
   elif b >= a and c >= a:
       return b + c
   elif a >= c and b >= c:
       return a + b


x1 = float(input("Введите первое число: "))
x2 = float(input("Введите второе число: "))
x3 = float(input("Введите третье число: "))
result = my_func(x1, x2, x3)
print("Сумма наибольших двух числе равна: ", result)
print("Конец программы.")



