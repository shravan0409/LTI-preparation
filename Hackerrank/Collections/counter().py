from collections import Counter
X = input()     #Number of shoes
S = Counter(map(int,input().split()))   #Shoe sizes in shop
N = int(input())     #Number of customers
      
earnings = 0
for customer in range(N):
    size, x_i = map(int,input().split())  #Shoes desired by the customer and the price of the shoe
    if size in S and S[size] > 0:
        S[size] -= 1
        earnings += x_i
            
print(earnings)


#myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
# print Counter(myList)
# Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
