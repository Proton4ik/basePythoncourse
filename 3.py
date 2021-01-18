i = 0
sum_salary = 0
with open("3.txt", "r", encoding = "utf-8") as f_obj:
    content = f_obj.readlines()
    while i < len(content):
        el = content[i].split()
        salary = int(el[1])
        if salary < 20000:
            print(el[0], "получает меньше 20000")
        sum_salary = sum_salary + salary
        i = i + 1
average_salary = sum_salary / len(content)
print("Средний доход сотрудников равен {:.2f}" .format(average_salary))

