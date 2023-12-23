'''num=int(input('enter s number  '))
i=1
count=0
while  i<=num:
    if num%i==0:
        count+=1
    i+=1
if count==2:
    print(num,'is prime')
else:
    print(num,'is not a prime')'''

num=int(input('enter   '))
i=1
temp=False
while i<=num:
    if num%i==0 and i!=1 and i!=num:
        temp=True
    i+=1
if not temp:
    print('num is prime')
else:
    print('num is not a prime')