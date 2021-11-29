
from utils import isNumber
from math import sin, cos

class Vector:

    def __init__(self, *args):

        if not all(map(isNumber, args)):
            raise TypeError('All components of a Vector must be numbers')

        self.__components = args
        self.__dim = len(args)
        self.__norm = sum(args) / len(args)

    @classmethod
    def fromsequence(cls, sequence):
        return cls(*sequence)

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

    # string representations
    def __repr__(self):
        return f'{self.__class__}{self.components}'

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


class Vector2(Vector):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return x

    @property
    def y(self):
        return y

    @staticmethod
    def isVector2(candidate):
        return Vector.isVector(candidate) and candidate.dim == 2

    def __complex__(self):
        return self.x + self.y*1j

    # rotation (in radians) counterclockwise around the origin
    def rotate(self, theta):
        return self.__class__(
            cos(theta)*self.x - sin(theta)*self.y,
            sin(theta)*self.x + cos(theta)*self.y
        )


class Vector3(Vector):

    def __init__(self, x, y, z):
        super().__init__(x, y, z)
        self.__x = x
        self.__y = y
        self.__z = z

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def z(self):
        return self.__z

    @staticmethod
    def isVector3(candidate):
        return Vector.isVector(candidate) and candidate.dim == 3

    def cross(self, vec):
        if not Vector3.isVector3(vec):
            raise TypeError(f'{type(vec)} cannot be treated as a {type(self)}')

        return self.__class__(
            self.y*other.z - self.z*other.y,
            self.z*other.x - self.x*other.z,
            self.x*other.y - self.y*other.x
        )
