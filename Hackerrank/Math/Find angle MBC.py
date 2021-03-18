# Enter your code here. Read input from STDIN. Print output to STDOUT   
import math

AB = int(input())
BC = int(input())

H = math.sqrt(AB**2 + BC**2)    #hypotenuse
H = H/2.0   #midpoint
adj = BC/2.0    #adjacent

Output = int(round(math.degrees(math.acos(adj/H))))     #degrees() function returns the degree of the fraction. acos() function returns the cosine inverse of the fraction.

Output = str(Output)

print(Output+"°")
