n = int(input())

arr = input().split(" ")

print(all(int(i)>=0 for i in arr) and any(i == i[::-1]for i in arr))  
#all() returns true only when all the conditions are true.
#any() returns true even if one of the condition is matched.
