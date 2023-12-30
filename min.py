print("WELCOME TO BOOK MY SHOW")
print("--------------------------")
name=input('Enter your name: ')
print('Total seats avialable: 30')
seats=int(input(" please confirm no of seats: "))
totseats=30
seatavial=totseats-seats
cinema=eval(input('Choose movie \n 1--SALAAR \n 2--ANIMAL \n 3--Hi Nanna : '))
category=int(input('Please select class type \n 1.Diamond class\n 2.Gold class\n 3.Sliver class :'))
if cinema==1:
    if category==1:
        print("SALAAR in Diamond class")
        amt=seats*400
    elif category==2:
        print("SALAAR in Gold class")
        amt=seats*200
    elif category==3:
        print("SALAAR in Sliver class")
        amt=seats*100
    else:
        print("OUT OF CLASS")
elif cinema==2:
    if category==1:
        print("ANIMAL in Diamond class")
        amt=seats*400
    elif category==2:
        print("ANIMAL in Gold class")
        amt=seats*200
    elif category==3:
        print("ANIMAL in Sliver class")
        amt=seats*100
    else:
        print("OUT OF CLASS")
elif cinema==3:
    if category==1:
        print("Hi Nanna in Diamond class")
        amt=seats*400
    elif category==2:
        print("Hi Nanna in Gold class")
        amt=seats*200
    elif category==3:
        print("Hi Nanna in Sliver class")
        amt=seats*100
    else:
        print("OUT OF CLASS")
elif cinema >=3:
    print("Movie is not avialable")
print(seatavial,'seats only few more left')

print(f"Hi,{name} you've confirmed {seats}  seats and \n Total amt is = {amt}")
print('--------------------------')
print("THANK YOU,VIST AGAIN \n HAPPY NEW YEAR")