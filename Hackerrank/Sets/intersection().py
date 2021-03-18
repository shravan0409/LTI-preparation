# Enter your code here. Read input from STDIN. Print output to STDOUT
n_e = int(input())
r_e = map(int, input().split())

n_f = int(input())
r_f = map(int, input().split())

s = set(r_e)
print(len(s.intersection(r_f)))        #returns the count of common elements between lists


#Simpler way
# for i in r_f:
#     s.add(i)

# print(len(s))
