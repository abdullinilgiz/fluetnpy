import random

import numpy as np


class FileOutputMixin:
    def to_file(self, filename):
        with open(filename, "w") as f:
            f.write(str(self))


class StrMixin:
    def __str__(self):
        return str(self.data)


class GetterSetterMixin:
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data):
        self._data = new_data


class Matrix(np.lib.mixins.NDArrayOperatorsMixin,
             FileOutputMixin,
             StrMixin,
             GetterSetterMixin):
    def __init__(self, value):
        self.data = np.asarray(value)

    _HANDLED_TYPES = (np.ndarray, )

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())
        for x in inputs + out:
            if not isinstance(x, self._HANDLED_TYPES + (Matrix,)):
                return NotImplemented

        inputs = tuple(x.data if isinstance(x, Matrix) else x
                       for x in inputs)
        if out:
            kwargs['out'] = tuple(
                x.data if isinstance(x, Matrix) else x
                for x in out)
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            return None
        else:
            return type(self)(result)

    def __repr__(self):
        return '%s(%r)' % (type(self).__name__, self.data)


random.seed(0)
A = Matrix(np.random.randint(0, 10, (10, 10)).tolist())
B = Matrix(np.random.randint(0, 10, (10, 10)).tolist())

A_add_B = A + B
A_mul_B = A * B
A_matmull_B = A @ B

A_add_B.to_file("matrix+.txt")
A_mul_B.to_file("matrix*.txt")
A_matmull_B.to_file("matrix@.txt")
