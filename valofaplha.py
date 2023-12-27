def asc_2(a):
    if 'a'<=a<='z':
        return a
    
def asnum(b):
    c=ord(b)
    return c
mal=map(asnum,filter(asc_2,'a1b2c3D3f12@#9Z'))
print(list(mal))
    