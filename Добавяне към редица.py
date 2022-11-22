n=int(input("Въведи число за край на редицата"))
s=list(i for i in range(0,n+1))
c=int(input("Въведи 0 или 1"))
if c==0:
    for i in range(0,n,2):
        s[i]+=5
    print(s)
elif c==1:
    for i in range(1,n,2):
        s[i]+=10
    print(s)
else:
    print("Некоректно въведена команда")