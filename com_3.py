'''a=[len(i) for i in ["abcd",{1:2},[4,5,6],{4,6},(9,8,7)]]
print(a)'''
'''a=[i**3 for i in range(1,26) if i%3==0]
print(a)'''
'''a=[i for i in ([1,2,4,6],(1,2),{4,6,7},{2:1,4:2,1:3},'efgh') if len(i)>2]
print(a)'''
'''a=[i for i in range(1,100) if i%3==0 if i%2==0 if i%5==0]
print(a)'''
'''a=[i**2 if i%2==0 else i**3 for i in range(1,20) if type(i)==int ]
print(a)
'''
'''b=([i*j for j in range(1,11)]for i in [2,3,4])
print(b)'''
'''a='xyz'
b=[1,4,9]
d={i:j for i,j in zip(a,b)}
print(d)'''
a='ABCDEF'
'''b={j:i for i,j in enumerate(a) if i%2==0} 
print(b)'''
seats=int(input('confirm no of seats: '))
option=int(input('select the type of class:'))
match option:
    case 1:
        print("diamond")
        amt=seats*200
    case 2:
        print("Golden")
        amt=seats*150
    case 3:
        print("sliver")
        amt=seats*100
    case _:
        print("invalid option")
        amt=None
print(amt)