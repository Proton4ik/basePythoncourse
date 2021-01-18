import json
i = 0
firm_dict = {}
sum = 0
count_str = 0
with open("7.txt", "r", encoding = "utf-8") as f_obj:
    while True:
        content = f_obj.readline()
        if content == "":
            break
        el = content.split()
        profit = int(el[i + 2]) - int(el[i + 3])
        if int(el[i + 2]) - int(el[i + 3]) >= 0:
            sum = sum + profit
            count_str = count_str + 1
        firm_dict.update({el[i]: profit})
average = sum / count_str
average_dict = {'average_profit': average}
firm_list = [firm_dict, average_dict]
print(firm_list)
with open("7_json.json", "w") as write_f:
    json.dump(firm_list, write_f)




