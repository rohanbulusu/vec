
from utils import isNumber

class Vector:

    def __init__(*args):

        if not all(isNumber, args):
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

    
