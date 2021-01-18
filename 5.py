i = 0
result = 0
user_num = input("Введите числа через пробел: ")
num = user_num.split()
while i < len(num):
    el = int(num[i])
    result = result + el
    i = i + 1
with open("5.txt", "w", encoding = "utf-8") as f_obj:
    print(user_num, file = f_obj)
print("Сумма всех чисел введеных чисел в файл равна: ", result)

