# In this challenge, the user enters a string and a substring. 
# You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

def count_substring(string, sub_string):
    count = 0 #number of times
    for i in range(len(string)):
        if string[i:].startswith(sub_string):   #startswith is a built in function which can be used to check if the string starts with the value specified
            count+=1
        
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
