
from collections import namedtuple

from vectors import Vector
from utils import isNumber

_dimension = namedtuple('dim', ['rows', 'cols'])

class Matrix:

    def __init__(self, *rows):
        self.__rows = rows
        self.__cols = [[row[i] for row in rows] for i in len(rows)]
        self.__dim = _dimension(len(rows), len(self.__cols))

    @property
    def rows(self):
        return self.__rows

    @property
    def cols(self):
        return self.__cols

    @property
    def dim(self):
        return self.__dim

    # iterator protocol
    def __iter__(self):
        return next(self)

    def __next__(self):
        yield from self.rows

    # mapping protocol
    def __len__(self):
        return len(self.__rows)*len(self.__cols)

    def __getitem__(self, index):
        if not isNumber(index):
            raise TypeError('Matrix index must be a number')
        return self.rows[index]

    def __setitem__(self, index, val):
        raise IndexError(f'Matrix index \'{index}\' does not exist')

    # Matrix utilities
    @staticmethod
    def isMatrix(other):
        return isinstance(other, Matrix)

    # string representation
    def __repr__(self):
        return f'{type(self)}{tuple(self.rows)}'

    # unary operators
    def __pos__(self):
        return Matrix(*self)

    def __neg__(self):
        return -1 * self

    # arithmetic operators
    def __add__(self, other):
        if not Matrix.isMatrix(other):
            raise TypeError(f'Cannot add Matrix to {type(other)}')
        if self.dim != other.dim:
            raise ValueError(f'Cannot add matrices of differing dimension')

        return self.__class__(*[
            [s + o for s, o in zip(s_row, o_row)]
            for s_row, o_row in zip(self.rows, other.rows)
        ])

    def __sub__(self, other):
        if not Matrix.isMatrix(other):
            raise TypeError(f'Cannot add Matrix to {type(other)}')
        if self.dim != other.dim:
            raise ValueError(f'Cannot subtract matrices of differing dimension')

        return self.__class__(*[
            [s - o for s, o in zip(s_row, o_row)]
            for s_row, o_row in zip(self.rows, other.rows)
        ])

    def __mul__(self, other):

        # matrix-vector multiplication
        if Vector.isVector(other):
            if other.dim != self.dim.cols:
                raise ValueError(f'{other} has incompatible dimension with {self} for multiplication')
            return other.__class__(*[
                sum([other[i]*row[i] for i in range(other.dim)])
                for row in self.rows
            ])

        # matrix-matrix multiplication
        if Matrix.isMatrix(other):
            if other.dim != self.dim:
                raise ValueError(f'{other} has incompatible dimension with {self} for multiplication')

            # O(self.dim.rows * self.dim.cols * self.dim.rows) algorithm
            _new = [[0 for _ in range(other.dim.cols)] for _ in range(self.dim.rows)]
            for i in range(self.dim.rows):
                for j in range(self.dim.cols):
                    _new[i][j] = sum([
                        self[i][k]*other[k][j] for k in range(self.dim.cols)
                    ])
            return self.__class__(*_new)

        # matrix-scalar multiplication
        if isNumber(other):
            return self.__class__(*[
                [other*c for c in row] for row in self.rows
            ])

        raise TypeError(f'Cannot multiply Matrix with {type(other)}')

    def __div__(self, other):
        if isNumber(other):
            return self * (1/other)
        raise ArithmeticError(f'Cannot divide {type(self)} by a {type(other)}')


# Identity matrices
_identity_wrapper = namedtuple('identity_wrapper', ['S2', 'S3', 'S4'])

Identity = _identity_wrapper(
    Matrix(
        [1, 0],
        [0, 1]
    ),
    Matrix(
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ),
    Matrix(
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    )
)
