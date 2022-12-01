def list_avg(lst,multiplier=1):
    if (type(multiplier) !=int):
        print("Некоректно подаден параметър")
        return
    sum=0
    count=0
    for i in lst:
        if (type(i)==int or type(i)==float):
            i=i*multiplier
            sum+=i
            count+=1
    if(count==0):
        print("Error: Division by zero")
        return
    else:
        return sum/count