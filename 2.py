class OwnError(Exception):
    def __init__(self, param):
        self.param = param


a = float(input('Введите делимое: '))
try:
    b = float(input('Введите делитель: '))
    if b == 0:
        raise OwnError('Делить на ноль нельзя')
    print('Результат: ', a / b)
except OwnError as err:
    print(err)

