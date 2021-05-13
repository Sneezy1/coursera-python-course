from sys import stdin
from copy import deepcopy


class Matrix:
    def __init__(self, lol):
        self.lol = deepcopy(lol)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, i)) for i in self.lol])

    def size(self):
        return '({0}, {1})'.format(len(self.lol), len(self.lol[0]))

    def __add__(self, other):
        return Matrix([[self.lol[x][y] +
                        other.lol[x][y] for y in range(len(self.lol[0]))]
                       for x in range(len(self.lol))])

    def __mul__(self, num):
        return Matrix([[i * num for i in j] for j in self.lol])

    __rmul__ = __mul__


exec(stdin.read())
