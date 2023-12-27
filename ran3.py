def call(a,b):
    yield a+b
    yield a-b
    yield a*b
    yield a/b
call1=call(10,5)
a=list(call1)
print (a)