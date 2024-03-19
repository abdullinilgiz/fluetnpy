import random

import numpy as np


class FileOutputMixin:
    def to_file(self, filename):
        with open(filename, "w") as f:
            f.write(str(self))


class MatrixHashMixin:
    def __hash__(self) -> int:
        """This hash return equal values for equal size matrices"""
        return self.rows * self.cols


class Matrix(MatrixHashMixin, FileOutputMixin):
    def __init__(self, data):
        try:
            self.data = data
            self.rows = len(data)
            self.cols = len(data[0])
        except TypeError:
            raise ValueError()

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError()
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)]
        return Matrix(result)

    def __mul__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError()
        result = [
            [self.data[i][j] * other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)]
        return Matrix(result)

    def __matmul__(self, other):
        if self.cols != other.rows:
            raise ValueError()
        result = [[
            sum(self.data[i][k] * other.data[k][j]
                for k in range(self.cols))
            for j in range(other.cols)]
            for i in range(self.rows)
            ]
        return Matrix(result)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.data])


random.seed(0)
A = Matrix(np.random.randint(0, 10, (10, 10)))
B = Matrix(np.random.randint(0, 10, (10, 10)))
C = Matrix(np.random.randint(0, 10, (10, 10)))
D = B

print((hash(A) == hash(C)) and (A != C) and (B == D) and (A @ B != C @ D))

A.to_file('A.txt')
B.to_file('B.txt')
C.to_file('C.txt')
D.to_file('D.txt')

AB = A @ B
AB.to_file('AB.txt')
CD = C @ D
CD.to_file('CD.txt')

with open('hash.txt', "w") as f:
    f.write('hash AB: ' + str(hash(AB)) + '\n')
    f.write('hash CD: ' + str(hash(CD)) + '\n')
