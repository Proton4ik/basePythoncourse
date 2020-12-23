a = float(input("Введите значение выручки: "))
b = float(input("Введите значение издержек: "))
if a > b:
    plus = a - b
    rent = plus / a
    print ("Ваша фирма успешна. Прибыль составляет: {:.2f}  Рентабельность составляет: {:.2f} ".format(plus, rent))
    pers = int(input("Введите количество сотрудников: "))
    plus_pers = plus / pers
    print ("На каждого сотрудника приходится прибыль в размере {:.2f}".format(plus_pers))
else:
    minus = b - a
    print ("Ваша фирма убыточна. Убыток составляет {:.2f}".format(minus))
print ("Конец программы.")

