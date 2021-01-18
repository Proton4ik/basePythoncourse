i = 0
with open("2.txt", "r", encoding = "utf-8") as f_obj:
    while True:
        content = f_obj.readline()
        if content == "":
            break
        i = i + 1
        user_list = content.split()
        print("Количество слов в {} строке равно {}".format(i, len(user_list)))

print("Количество строк в файле равно ", i)

