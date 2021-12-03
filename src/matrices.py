
from vectors import Vector, Vector2, Vector3, Vec2, Vec3
from utils import isNumber


class Matrix:
    
    def __init__(self, *rows):
        self.__rows = rows
        self.__cols = [[row[i] for row in rows] for i in len(rows)]
       
    @property
    def rows(self):
        return self.__rows
    
    @property
    def cols(self):
        return self.__cols
    
    # iterator protocol
    def __iter__(self):
        return next(self):
       
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
        raise IndexError('Matrix index \'{index}\' does not exist')
    
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
    
    
    
    
    
    
    
