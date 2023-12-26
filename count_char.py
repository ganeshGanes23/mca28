def fact_(a):
    out=1
    i=1
    while i<=a:
        out*=i
        i+=1
    return out
b=fact_(5)
print(b)