# eval function is used for evaluating any expression

eval(input()) #this line alone prints any expression

#ATHELETE'S SORT
N,M = map(int,input().split())
rows = [list(map(int,input().split())) for i in range(N)]
i = int(input())
rows = sorted(rows, key=lambda x:x[i])
for i in rows:
    print(*i)
    
    
#INPUT FORMAT:
# The first line contains N and M separated by a space.
# The next N lines each contain M elements.
# The last line contains K.

#OUTPUT FORMAT:
# Print the  lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity.
    
    
#SAMPLE INPUT
# 5 3
# 10 2 5
# 7 1 0
# 9 9 9
# 1 23 12
# 6 5 9
# 1

# SAMPLE OUT
# 7 1 0
# 10 2 5
# 6 5 9
# 9 9 9
# 1 23 12
