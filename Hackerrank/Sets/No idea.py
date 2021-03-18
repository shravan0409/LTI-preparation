# There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. 
# You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. For each  integer in the array, if , you add  to your happiness. 
# If , you add  to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

n, m = input().split()

arr = input().split()

A = set(input().split())
B = set(input().split())
# print(sum([(i in A) - (i in B) for i in arr]))    #one line answer.

#how it works:

happy=0
sad = 0
for i in arr:
    if i in A:
        happy +=1
        
    if i in B:
        sad +=1
        
print(happy-sad)
