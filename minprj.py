print("Welcome to BOOKMYSHOW")
a=str(input("Please enter your name: "))
b=int(input('enter no.of seats : '))
seat=eval(input('select your seat \n 1-for Diamond \n 2-for Gold \n 3-for Sliver: '))
if 1>=seat<=1: 
    print('1-Diamond seat at cost of :400')
    if 1>=seat<=1:
        print('total amt is:')
        print(b,400,sep='*',end="=")
        print(b*400)
        print('Name:Ganesh \n seats:2 \n amt:800')
elif 2>=seat<=2:
    print('1-Gold seat  at cost of :200')
    if 2>=seat<=2:
        print('total amt is:')
        print(b,200,sep='*',end="=")
        print(b*400)
        print('Name:Ganesh \n seats:2 \n amt:400')
elif 3>=seat<=3:
        print('1-Sliver seat at cost of :100')
        if 3>=seat<=3:
            print('total amt is:')
            print(b,100,sep='*',end="=")
            print(b*200)
            print('Name:Ganesh \n seats:2 \n amt:200')
else:
    print('no seat is selected')

print("Thanks for booking")


