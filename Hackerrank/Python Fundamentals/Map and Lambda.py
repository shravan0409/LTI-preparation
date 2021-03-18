# The map() function applies a function to every member of an iterable and returns the result. It takes two parameters: first,the function that is to be applied and 
# secondly, the iterables.

# Let's say you are given a list of names, and you have to print a list that contains the length of each name.

# >> print (list(map(len, ['Tina', 'Raj', 'Tom'])))  
# [4, 3, 3]  
# Lambda is a single expression anonymous function often used as an inline function. In simple words, it is a function that has only one line in its body. It proves very handy in functional and GUI programming.

# >> sum = lambda a, b, c: a + b + c
# >> sum(1, 2, 3)
# 6


#Fibbonacci

cube = lambda x:x*x*x # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    n1, n2 = 0, 1
    l = list()
    count = 0
    if n <= 0:
        # print("Please enter a positive integer")
        return l
    elif n == 1:
        # print("Fibonacci sequence upto",n,":")
        # print(n1)
        l.append(n1)
    else:
        # print("Fibonacci sequence:")
        
        while count < n:
            l.append(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1
    return l
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
    
    
    
#Input:   5
#OUTPUT:  [0, 1, 1, 8, 27]
