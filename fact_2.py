def fact_1(x,out=1):
    if x==out:
        return out
    return out*fact_1(x,out+1)
c=fact_1(5)
print(c)