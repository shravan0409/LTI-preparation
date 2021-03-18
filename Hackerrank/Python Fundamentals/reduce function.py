# Concept
# The reduce() function applies a function of two arguments cumulatively on a list of objects in succession from left to right to reduce it to one value. 
# Say you have a list, say [1,2,3] and you have to find its sum.


# Basic fraction multiplication program

from fractions import Fraction
from functools import reduce
# import operator

def product(fracs):
    t = reduce(lambda x, y : x * y, fracs)# complete this line with a reduce statement
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
