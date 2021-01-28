class OwnError(Exception):
    def __init__(self, param):
        self.param = param


user_list = []
while True:
    try:
        el = input('Введите элемент списка. Для остановки программы введите stop. ')
        try:
            el = int(el)
        except ValueError:
            pass
        if el == "stop":
            print(user_list)
            break
        elif type(el) == str:
            raise OwnError('Текст не попадет в список')
        else:
            user_list.append(el)
    except OwnError as err:
        print(err)

