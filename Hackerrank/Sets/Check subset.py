# Enter your code here. Read input from STDIN. Print output to STDOUTT = int(input())
T = int(input())
for _ in range(T):
    a = input()
    A = set(input().split())
    b = int(input())
    B = set(input().split())
    print(A.issubset(B))    #this is a very useful function which is used for checking if the set a is a subset of set b
    
    
#OUTPUT:

#A = [1,2,3,4,5,6,7]
#B = [1,2,3,4]

# OUTPUT:
#   TRUE
