
from utils import isNumber

class Vector:

    def __init__(self, *args):

        if not all(map(isNumber, args)):
            raise TypeError('All components of a Vector must be numbers')

        self.__components = args
        self.__dim = len(args)
        self.__norm = sum(args) / len(args)

    @property
    def components(self):
        return self.__components

    @property
    def dim(self):
        return self.__components

    @property
    def norm(self):
        return self.__norm

    # iterator protocol
    def __iter__(self):
        return next(self)

    def __next__(self):
        yield from self.components

    # mapping protocol (restricted to just the * operator)
    def __len__(self):
        return self.dim

    # Vector utilities
    @staticmethod
    def isVector(candidate):
        return isinstance(candidate, Vector) or issubclass(type(vec), Vector)

    # unary operators
    def __pos__(self):
        return Vector(*self.components)

    def __neg__(self):
        return Vector(*[-comp for comp in self.components])

    # arithmetic operators
    def __add__(self, vec):
        if not Vector.isVector(vec):
            raise TypeError(f'{type(self)} and {type(vec)} have incompatible types')

        if self.dim != vec.dim:
            raise ValueError(f'Vectors have incompatible dimensions')

        return self.__class__(
            *[s + v for s, v in zip(self.components, vec.components)]
        )

    def __sub__(self, vec):
        if not Vector.isVector(vec):
            raise TypeError(f'{type(self)} and {type(vec)} have incompatible types')

        if self.dim != vec.dim:
            raise ValueError(f'Vectors have incompatible dimensions')

        return self.__class__(
            *[s - v for s, v in zip(self.components, vec.components)]
        )

    # scalar and dot products
    def __mul__(self, other):
        # scalar multiplication if 'other' is an ordinary
        if isNumber(other):
            return self.__class__(
                *[other*comp for comp in self.components]
            )
        # dot product if 'other' is some kind of vector
        elif Vector.isVector(other):
            return self.__class__(
                *[s * o for s, o in zip(self.components, other.components)]
            )
        # if 'other' is neither a vector nor a scalar, it has a bad type
        else:
            raise TypeError(f'{type(self)} and {type(other)} have incompatible types')

    def __div__(self, other):
        if Vector.isVector(other):
            raise ArithmeticError(f'Cannot divide by a {type(self)}')
        return self * (1 / other)
