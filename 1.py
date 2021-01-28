class Date:
    @classmethod
    def magic(cls, date: str):
        date_list = date.split('-')
        i = 0
        while i < len(date_list):
            date_list[i] = int(date_list[i])
            i = i + 1
        return date_list

    @staticmethod
    def valid(date):
        if date[0] < 1 or date[0] > 31:
            print('Неверное число дня')
        elif date[1] < 1 or date[1] > 12:
            print('Неверное число месяца')
        elif date[2] < 0:
            print('Неверное число года')
        else:
            print('Валидация прошла успешно')


x = Date.magic("25-01-2020")
print(x)
Date.valid(x)

