'''col=int(input('no of col: '))
row=int(input('no of row: '))
for i in range(row):
    for j in range(col):
        if i==0 or i==row-1 :
            print('+',end=' ')
        else:
            if j==0 or j==col-1 or j==i:
                print('+',end=' ')
          
                
            else:
                print(' ',end=' ')
    print('')'''


'''col=int(input('no of col: '))
row=int(input('no of row: '))
for i in range(row):
    for j in range(col):
        if i==0 or i==row-1 :
            if j==0 or  j==col-1:
                print('$',end=' ')

            else:
                print('*',end=' ')
        else:
            if  j==i or row-i-1==j:
                print('$',end=' ')
            else:
                print('*',end=' ')
    print('')'''


'''col=int(input('no of col: '))
row=int(input('no of row: '))
for i in range(row):
    for j in range(col):
        if i==0 or i==row-1 :
            print('+',end=' ')
        else:
            if j==0 or j==col-1 or j==i:
                print('+',end=' ')
          
                
            else:
                print(' ',end=' ')
    print('')'''

row=int(input('no of row: '))
for i in range(1,row+1):
    print('+ '*i)
    

