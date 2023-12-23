'''i=1
while i<=100:
    print(i, end='   ')
    i=i+2'''
i=1
out=0
while i<=100:
    if i%2 != 0:
        out =out+i
    i+=1
print(out)
