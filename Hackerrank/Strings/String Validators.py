#any() function is used to check for True or False


if __name__ == '__main__':
    s = input()
    print(any(a.isalnum() for a in s))    #checks if the string consists of only alphabets or numbers
    print(any(a.isalpha() for a in s))    #checks if the string consists of only alphabets
    print(any(a.isdigit() for a in s))  #checks if the string consists of only numbers
    print(any(a.islower() for a in s))    #checks if the string consists of only Upper case
    print(any(a.isupper() for a in s))    #checks if the string consists of only Lower case
    





