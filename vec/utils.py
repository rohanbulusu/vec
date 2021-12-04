
from numbers import Complex
from collections.abc import Iterable

def isNumber(candidate):
    return isinstance(candidate, Complex)

def isSinglyNestedList(candidate):
    return all(map(
        lambda c: isinstance(c, Iterable) and not isinstance(c[0], Iterable),
        candidate
    ))
