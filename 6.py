num_key = 0
sub_dict = {}
with open("6.txt", "r", encoding = "utf-8") as f_obj:
    while True:
        content = f_obj.readline()
        if content == "":
            break
        el = content.split()
        i = 1
        result = 0
        while i < len(el):
            if el[i] == "—":
                i = i + 1
                continue
            else:
                el_hour = el[i].split("(")
                result = result + int(el_hour[0])
            i = i + 1
        sub_dict.update({el[num_key]: result})
    num_key = num_key + 1
print(sub_dict)

