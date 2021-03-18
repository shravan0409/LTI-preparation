# Enter your code here. Read input from STDIN. Print output to STDOUT


a = int(input())
b = int(input())

print(a//b)     #floor division i.e returns the quotient to the nearest number
print(a%b)
print(divmod(a,b))  #divmod() returns a tuple with the quotient and the remainder
