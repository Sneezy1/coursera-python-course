from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, obj, other):
        self.matrix1 = obj
        self.matrix2 = other


class Matrix:
    @staticmethod
    def transposed(matrix):
        return Matrix([[matrix.lol[j][i] for j in range(len(matrix.lol))]
                       for i in range(len(matrix.lol[0]))])

    def __init__(self, lol):
        self.lol = deepcopy(lol)

    def __str__(self):
        return '\n'.join('\t'.join(map(str, i)) for i in self.lol)

    def __add__(self, other):
        if len(self.lol) == len(other.lol):
            return Matrix([[self.lol[x][y] +
                            other.lol[x][y] for y in range(len(self.lol[0]))]
                           for x in range(len(self.lol))])
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Matrix([[i * other for i in j] for j in self.lol])
        elif isinstance(other.lol, list):
            if len(self.lol[0]) == len(other.lol):
                elem = 0
                arro = []
                res = []
                for i in range(len(self.lol)):  # строк в 1 матрице
                    for j in range(len(other.lol[0])):  # количество столбцов во 2ой матрице
                        for k in range(len(self.lol[0])):  # количество столбцов в 1ой матрице
                            elem += self.lol[i][k] * other.lol[k][j]
                        arro.append(elem)
                        elem = 0
                    res.append(arro)
                    arro = []
                return Matrix(res)
            else:
                err = MatrixError(self, other)
                raise err
        elif isinstance(other, int) or isinstance(other, float):
            return Matrix([[i * other for i in j] for j in self.lol])

    __rmul__ = __mul__

    def transpose(self):
        self.lol = [[self.lol[j][i] for j in range(len(self.lol))]
                    for i in range(len(self.lol[0]))]
        return Matrix(self.lol)

    def size(self):
        return '({0}, {1})'.format(len(self.lol), len(self.lol[0]))


exec(stdin.read())
