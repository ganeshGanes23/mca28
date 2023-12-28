a=[1,2,3,4]
b=[5,6,7,8]
c=[10,20,30,40]
out=[]
for i,j,k in zip(a,b,c):
    out=out+[i]+[j]+[k]
print(out)