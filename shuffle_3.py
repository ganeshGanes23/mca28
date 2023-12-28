''''a='ABC'
b=[4,5,6]
out={}
for i,j in zip(a,b):
    out[i]=j
print(out)'''

a='abcd'
out=''
for i,j in enumerate(a):
    out=out+j+str(i)
print(out)