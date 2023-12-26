'''def add(*args):
    out=0
    for i in args:
        out+=1
    return out
res=add(1,23,43,54,5,86)
print(res)'''

'''def add(*args,b=0,**kwargs):
    print(b,args)
    print(kwargs)
add(30,34,9)'''

'''def add(a,b,c):
    print(a,b,c)
add(**{'b':3,'c':4,'a':5,})'''

'''# WAP to get sum of numbers 1 to 10 using while loop

count=0
i=1
while i <=10:
        count+=i
        i+=1

print(count)'''

def sum(st,end):
    if st==end:
        return st
    return st+ sum(st+1,end)
out=sum(1,10)
print(out)