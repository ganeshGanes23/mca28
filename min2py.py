print("WELCOME TO BOOK MY SHOW")
print("--------------------------")
name=input('Enter your name: ')
print('Movie Theatres near by you \n Movie_Land \n RK_cinema \n V.V_Mahal')
Thearter=input('Enter the movie theater name:  ')
var='Total seats avil : 50'
a=Thearter
if Thearter<='Movie_Land':
    print('Movies are \n SALAAR \n ANIMAL \n Hi Nanna ')
    movie=str(input('enter movie name: '))
    print(var)
    
    seats=int(input(" please confirm no of seats: "))
    print('class type are \n Daimond \n Gold \n Sliver')
    category=str(input('select type of class: '))
    if 'SALAAR'<=movie<='salaar':
        if 'DAIMOND'<=category<='daimond':
            print("Movie:SALAAR  Type:Diamond class")
            amt=seats*400
        elif 'GOLD'<=category<='gold':
            print("Movie:SALAAR  Type:Gold class")
            amt=seats*200
        elif category==SLIVER or sliver:
            print("Movie:SALAAR  Type:Sliver class")
            amt=seats*100
        else:
            print("OUT OF CLASS")
    elif movie==animal or ANIMAL:
        if category==1:
            print("Movie:ANIMAL  Type:Diamond class")
            amt=seats*400
        elif category==2:
            print("Movie:ANIMAL  Type:Gold class")
            amt=seats*200
        elif category==3:
            print("Movie:ANIMAL  Type:Sliver class")
            amt=seats*100
        else:
            print("OUT OF CLASS")
    elif movie==hinanna or HINANNA:
        if category==1:
            print("Movie:Hi Nanna  Type:Diamond class")
            amt=seats*400
        elif category==2:
            print("Movie:Hi Nanna  Type:Gold class")
            amt=seats*200
        elif category==3:
            print("Movie:Hi Nanna  Type:Sliver class")
            amt=seats*100
        else:
            print("OUT OF CLASS")
    else :
        print("Movie is not avialable")
    a=30
    seatavial=a-seats
    print(f"Hi,{name} you've confirmed {seats}  seats and \n Total amt is = {amt}")
    print(seatavial,' few more seats only left')
print('--------------------------')
print("THANK YOU,VIST AGAIN \n HAPPY NEW YEAR")