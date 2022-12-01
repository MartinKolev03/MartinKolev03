def input_nums(n):
    l=[]
    for i in range(0,n):
        val=input("Enter a list element:")
        if(val.isnumeric()):
            l.append(int(val))
    return l
def sum_list(lst):
    sum=0
    for i in lst:
        if(type(i) == int or type(i) == float):
            sum+=i
        elif(i.isnumeric()):
            sum+=float(i)
    return sum
def max_of_two(a,b):
    if(type(a)!=int and type(a)!=float):
        if(type(b)!=int and type(b)!=float):
            return
        else:
            return b
    elif(type(b)!=int and type(b)!=float):
        return a
    elif(a>=b):
        return a
    else:
        return b
print(max_of_two(sum_list(input_nums(4)),sum_list(input_nums(3))))
print(max_of_two(sum_list([4,"AA@",3.12,"1"]),"9.2"))