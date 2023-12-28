'''def change(i=1,j=2):
    i+=j
    j+=1
    print(i,j)
change(j=1,i=2)'''

def foo(i,x=[]):
    x.append(i)
    return x
for i in range(3):
    print(foo(i))