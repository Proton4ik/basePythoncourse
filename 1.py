def dev(a, b):
        return a / b


dev1 = float(input("Введите делимое: "))
dev2 = float(input("Введите делитель: "))
while dev2 == 0:
    dev2 = float(input("Делить на ноль нельзя. Введите делитель: "))
result = dev(dev1, dev2)
print("Результат деления: {:.2f}" .format(result))
print("Конец программы.")

