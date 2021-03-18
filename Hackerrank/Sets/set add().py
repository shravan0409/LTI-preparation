# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
stamp_set = set()
for i in range(N):
    x = input()
    stamp_set.add(x)        #used to add new element to the set. if already exists, no change
    
print(len(stamp_set))
