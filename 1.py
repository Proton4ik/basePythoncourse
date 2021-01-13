from sys import argv

script_name, hours, money, bonus = argv
result = int(hours) * int(money) + int(bonus)
print("Заработная плата сотрудника равна ", result)


