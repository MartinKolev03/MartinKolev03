n=int(input("Въведи брой елементи в речника"))
d={}
for i in range(0,n):
    k=input("")
    val=input("")
    d[k]=val
m=int(input("Въведи брой елементи в списъка"))
l=[]
s=d.keys()
for i in range(0,m):
    val=input("")
    if(val in s):
        l.append(d[val])
        d.pop(val)
    else:
        l.append(val)
print(d)
print(l)
