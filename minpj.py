print('Welcome to BOOK MY SHOW')
name=input("enter your name:")
seats=int(input("Please confirm no of seats:"))
category=(int(input('please select class \n 1-for Diamond \n 2-for Gold \n 3-for Sliver:')))
if category ==1:
    amount=seats*400
elif category ==2:
    amount=seats*200
elif category ==3:
    amount=seats*100
print(f'Hi{name} you cofirm {seats} and in {category} the total amt is{amount}')
