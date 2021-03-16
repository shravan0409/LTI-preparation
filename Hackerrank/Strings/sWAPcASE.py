def swap_case(s):
    x = s.swapcase() #swapcase is a function which is used to change the cases
    return x

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
