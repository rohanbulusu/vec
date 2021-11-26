
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
        return self

    def __next__(self):
        for comp in self.components:
            yield comp
        raise StopIteration

    # mapping protocol (restricted to just the * operator)
    def __len__(self):
        return self.dim
