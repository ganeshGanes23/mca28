a='xyz'
b='abc'
'''out=''
for i in range(len(a)):
    out+=a[i]+b[i]
print(out)'''
out=''
for i,j in zip(a,b):
    out=out+i+j
print(out)