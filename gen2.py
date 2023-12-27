def range_1(st,ed):
    for i in range(st,ed+1):
        yield i**2
        yield i*2
out=range_1(5,15)
print(list(out))

