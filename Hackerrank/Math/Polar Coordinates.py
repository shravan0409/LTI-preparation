# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath    #cmath module helps us perform functions with complex equations
print(*cmath.polar(complex(input())), sep='\n')     #returns the polar coordinates. given the complex number


#Input: 1+2j

#Output: 2.23606797749979   1.1071487177940904

