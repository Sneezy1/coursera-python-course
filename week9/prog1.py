from sys import stdin
from copy import deepcopy


class Matrix:
    def __init__(self, lol):
        self.lol = deepcopy(lol)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, i)) for i in self.lol])

    def size(self):
        return '({0}, {1})'.format(len(self.lol), len(self.lol[0]))


exec(stdin.read())
