def split_and_join(line):
    # write your code here
    x = line.split(" ")     #line = "this is a string"
    # print(x)          #Output: ['this', 'is', 'a', 'string']
    x = '-'.join(x)
    # print(x)      #Output: "this-is-a-string"
    return x

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
