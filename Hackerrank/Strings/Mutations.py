#There are two methods for this

#String slicing is used here.
def mutate_string(string, position, character):
    x = string[:position] + character + string[position+1:]     
    
    return x

    
#The string is converted into a list and then the character is changed
def mutate_string(string, position, character):
    x = list()
    for i in string:
        x.append(i)
    
    x[position] = character
    s = ""
    s = "".join(x)
    
    return s

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
