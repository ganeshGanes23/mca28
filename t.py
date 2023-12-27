'''y=6
z=lambda x:x*y
print(z(8))'''
'''def foo():
    try:
        return 1
    finally:
            return 2
    k=foo()
print(k)'''

'''def generate():
    var2=5
    while var2:
        yield var2
        var2-=1
    for b in generate():
        print(b,end="")'''

'''def fn(var1):
    var1.pop(1)
var1=[1,2,3]
fn(var1)
print(var1)'''

'''print(list((pow(i,2)for i in range(1,5))))'''

'''def function1(var1):
    var1=var1+10
    print(var1)
var1=12
function1(var1)
print(var1)'''

'''def add(a,b):
    return a+5,b+5
result=add(3,2)
print(result)'''

var=(i for i in range(1))
next(var)
print(next(var))
