#Pattern printing
# You are given a positive integer N.
# Your task is to print a palindromic triangle of size N.

# For example, a palindromic triangle of size  is:

# 1
# 121
# 12321
# 1234321
# 123454321


for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print (int((10**i-1)/(9))**2)     #the logic given below is implemented here.
    
    
#Logic
# 1*1=1
# 11*11=121
# .
# .
# .
# .

# (10**1/9) = 1
# (10**2/9) = 11
