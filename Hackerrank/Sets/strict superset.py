A = set(map(int, input().split()))
for _ in range(int(input())):
    X = set(map(int, input().split()))
    if A.issuperset(X) != True or len(A) == len(X):     #returns true if the set is a perfect super set
        print(False)
        break 
else: print(True)
