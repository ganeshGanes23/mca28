a=eval(input('enter a value:-'))

if type(a)== str:
 if str(chr(a))==a and a%2==0:
    print('the values is even')
else:
    print('the values is odd')
