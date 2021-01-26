class Micro:
    def __init__(self, numbers):
        self.numbers = numbers

    def __add__(self, other):
        new = Micro(self.numbers + other.numbers)
        print('Новая клетка. количество ячеек ')
        return new.numbers

    def __sub__(self, other):
        if (self.numbers - other.numbers) > 0:
            new = Micro(self.numbers - other.numbers)
            print('Новая клетка. количество ячеек ')
            return new.numbers
        else:
            print('Отрицательное количество ячеек ')

    def __mul__(self, other):
        new = Micro(self.numbers * other.numbers)
        print('Новая клетка. количество ячеек ')
        return new.numbers

    def __truediv__(self, other):
        new = Micro(self.numbers // other.numbers)
        print('Новая клетка. количество ячеек ')
        return new.numbers

    def make_order(self, param):
        i = 0
        self.param = param
        c = []
        while i < (self.numbers // self.param):
            n = 0
            c.append([])
            while n < self.param:
                c[i].append('*')
                n = n + 1
            i = i + 1
        x = self.numbers - (i * self.param)
        j = 0
        c.append([])
        while j < x:
             c[i].append('*')
             j = j + 1
        return '\n'.join(map(str, c))


m1 = Micro(3)
m2 = Micro(2)
m3 = Micro(15)
print(m1 + m2)
print(m1 - m2)
print(m1 * m2)
print(m1 / m2)
print(m3.make_order(4))

