def value_1(a):
    if a%2==0:
        return 2**a
    else:
        return 3**a

a=map(value_1,[1,4,27,16])
print((list(a)))