i = 0
with open("4_result.txt", "w", encoding = "utf-8") as f_obj1:
    pass
list_words = ["Один", "Два", "Три", "Четыре"]
with open("4.txt", "r", encoding = "utf-8") as f_obj:
    while True:
        content = f_obj.readline()
        if content == "":
            break
        el = content.split()
        el.pop(0)
        el.insert(0, list_words[i])
        result = " ".join(el)
        i = i + 1
        with open("4_result.txt", "a", encoding="utf-8") as f_obj2:
            print(result, file = f_obj2)

