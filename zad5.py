n=int(input(""))
l=list(i for i in range(0,n))
for i in range(n):
    l[i]=int(input(""))
a=int(input("Въведи команда"))
if(a==0):
    for i in range(0,n,2):
        l[i]=l[i]+5
elif(a==1):
    for i in range(1,n,2):
        l[i]=l[i]+10
else:
    print("Некоректно въведена команда")
print(l)