def oddsq(a):
    if a%2!=0:
        return True
    else:
        return False                                                                                                               
def square(b):
    return b**2
b=map(square,filter(oddsq,range(1,100)))
print(list(b))
