# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
T = int(input())
for i in range(T):
    x = input()
    try:
        print(bool(re.compile(x)))    #compile() function is used to compile the regex expression and check if it is true or not.
    except re.error:    #if there is a  compilation error, it means the expression is wrong.
        print('False')
        
        
        
        
# INPUT:
# 2
# .*\+
# .*+

#OUTPUT:
# True
# False
