def fact():
    a=int(input('enter the number:  '))
    out=1
    for i in range(1,a+1):#while a>0:
        out*=a
        a-=1
    print(out)
fact()