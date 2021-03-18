def average(array):
    # your code goes here
    x = set(array)  #set stores only distinct elements. It can be easy to get them
    # print(x)
    
    avg = sum(x)/len(x)
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
