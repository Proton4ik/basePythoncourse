class Complex:
    def __init__(self, real: int, magic: int):
        self.real = real
        self.magic = magic
        print("{}{}({}){}".format(self.real, '+', self.magic, 'i'))

    def __add__(self, other):
        a = self.real + other.real
        b = self.magic + other.magic
        print('{}{}({}){}'. format(a, '+', b, 'i'))

    def __mul__(self, other):
        a = self.real * other.real - self.magic * other.magic
        b = self.real * other.magic + other.real * self.magic
        print('{}{}({}){}'. format(a, '+', b, 'i'))


n1 = Complex(5, -6)
n2 = Complex(-3, 2)
n1 + n2
n1 * n2

