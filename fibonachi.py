n=int(input("Въведете брой на членовете на редицата"))
s=list(i for i in range(n+2))
s[0]=1
s[1]=1
for i in range(2,n+2):
    s[i]=s[i-1]+s[i-2]
print(s)
