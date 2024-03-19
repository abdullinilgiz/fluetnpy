import random

import numpy as np


class Matrix:
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

A_add_B = A + B
A_mul_B = A * B
A_matmull_B = A @ B

f = open("matrix@.txt", "w")
f.write(str(A_matmull_B))
f.close()
f = open("matrix+.txt", "w")
f.write(str(A_add_B))
f.close()
f = open("matrix*.txt", "w")
f.write(str(A_mul_B))
f.close()
