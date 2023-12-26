def vowel_count(a,b):
    list_1=[]
    i=0
    for i in range(0,len(a)):#while i<len(a):
        if a[i] in b:#'aeiouAEIOU':
            list_1=list_1+[i]
            i=i+1
    return list_1
c=vowel_count("good morning",'aeiouAEIOU')
print(c)
        