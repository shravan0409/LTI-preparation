# Python program to print all permutations 

from itertools import permutations 
print [''.join(p) for p in permutations('ABCDEF')] 

#With the in-built function permutations(), all the possible patterns of a string can be printed.
