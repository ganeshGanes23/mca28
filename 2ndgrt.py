num1=(input('enter num1 value   '))
num2=(input('enter num2 value   '))
num3=(input('enter num3 value  '))
if num1>num2 and num1>num3:
   if num2>num3:
      print(num2,'num2 is second greater')
   else:
    print(num3,'is second greatest') 
elif num2>num3:
   if num1>num3:
     print(num1,'is second greatest')
   else:
     print('num3 is greater')
else:
   if num1>num2:
     print(num1,'is second greatest')
   else: 
     print(num2 ,' is second greatest')
