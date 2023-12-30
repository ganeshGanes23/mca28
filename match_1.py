op1=int(input('enter op1 value:'))
op2=int(input('enter op2 value:'))
cal=eval(input('enter arithmetic experssion to perform:'))
match cal:
    case 1:
        op3=op1+op2
        print(op3)
    case 2:
        op3=op1-op2
        print(op3)
    case 3:     
        op3=op1*op2
        print(op3)
    case 4:    
        op3=op1/op2
        print(op3)
    case _:
        print('No more calculation')


        