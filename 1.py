a = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
b = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
result = []


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        i = 0
        while i < len(self.matrix):
            self.matrix[i] = str(self.matrix[i])
            ' '.join(self.matrix[i])
            i = i + 1
        return '\n'.join(self.matrix)

    def __add__(self, other):
        i = 0
        while i < len(self.matrix):
            n = 0
            result.append([])
            while n < len(self.matrix[i]):
                result[i].append(int(self.matrix[i][n + 1]) + int(other.matrix[i][n + 1]))
                n = n + 3
            i = i + 1
        return '\n'.join(map(str, result))


m1 = Matrix(a)
m2 = Matrix(b)
print(m1,'\n')
print(m2,'\n')
print(m1 + m2)

