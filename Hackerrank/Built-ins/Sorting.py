# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()
li_l = list()
li_u = list()
li_o = list()
li_e = list()
for i in s:
    if i.islower():
        li_l.append(i)
        
    elif i.isupper():
        li_u.append(i)
        
    elif int(i)%2==0:
        li_e.append(i)
        
    elif int(i)%2!=0:
        li_o.append(i)
        
        
li_e = sorted(li_e)
li_o = sorted(li_o)
li_u = sorted(li_u)
li_l = sorted(li_l)

# print(str(li_l),str(li_u),li_o,li_e)

res=[]

res = li_l+li_u+li_o+li_e

ss = ""
s="".join(res)

print(s)
