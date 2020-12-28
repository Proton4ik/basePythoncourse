print("Решение через list")
month_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
user_month = int(input("Введите номер месяца: "))
while user_month <= 0 or user_month > 12:
    user_month = int(input("Такого месяца не существует. Еще разок: "))
if user_month == month_list[0] or user_month == month_list[1] or user_month == month_list[11]:
    print ("Зима нынче")
elif user_month == month_list[2] or user_month == month_list[3] or user_month == month_list[4]:
    print("Весна нынче")
elif user_month == month_list[5] or user_month == month_list[6] or user_month == month_list[7]:
    print("Лето нынче")
elif user_month == month_list[8] or user_month == month_list[9] or user_month == month_list[10]:
    print("Осень нынче")
print("Решение через dict: ")
month_dict = {1 : 'зима', 2 : 'весна', 3 : 'лето', 4 : 'осень'}
user_month = int(input("Введите номер месяца: "))
while user_month <= 0 or user_month > 12:
    user_month = int(input("Такого месяца не существует. Еще разок: "))
if user_month == 1 or user_month == 2 or user_month == 12:
    print (month_dict.get(1))
elif user_month == 3 or user_month == 4 or user_month == 5:
    print(month_dict.get(2))
elif user_month == 6 or user_month == 7 or user_month == 8:
    print(month_dict.get(3))
else:
    print(month_dict.get(4))
print("Конец программы")
