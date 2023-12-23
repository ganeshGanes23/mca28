a=input('enter a char   ')
vowel_count=0
cons_count=0
for var in a:
    if 'a'<=var<='z' or 'A'<=var<='Z':
        if var in 'aeiouAEIOU':
           vowel_count+=1
        else:
            cons_count+=1
print(vowel_count,cons_count)