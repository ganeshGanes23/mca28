a=input('enter a character to check   ')
i=0
count=0
while i<len(a):
    if a[i]in 'aeiouAEIOU':
        count+=1
    i+=1
print(count)