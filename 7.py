def fact(x):
    for i in range(1, x + 1):
        yield i


n = int(input("Введите число: "))
result = 1
num = 1
for el in fact(n):
    print(num, " число равно ", el)
    result = result * el
    num = num + 1
print("Факториал числа ", n, " равен ", result)

