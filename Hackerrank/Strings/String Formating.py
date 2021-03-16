def print_formatted(number):
    width=len(bin(number)[2:])
    for i in range(1,number+1):
        deci=str(i) #Normal decimal form
        octa=oct(i)[2:]     #Octal form 
        hexa=(hex(i)[2:]).upper()   #Hexadecimal value Capitalized
        bina=bin(i)[2:]     #Binary form
        print(deci.rjust(width),octa.rjust(width),hexa.rjust(width),bina.rjust(width))

#without the slicing of the answer, the Output will look like this:  1 0o1 0X1 0b1
    
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
