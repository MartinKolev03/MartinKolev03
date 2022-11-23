a=int(input("Въведи число"))
s=0
for i in range(1,a+1):
    n=0
    for j in range(0,i):
        n=n*10+a
        print(a,end="")
    print("+",end="")
    s+=n
print("="+str(s))
