class AnilInterrupt(Excetion):
    pass
    try:
        a=input('enter some value: ')
        if a[0] in 'aeiouAEIOU':
        print("first letter should not be vowel")
except AnilInterrupt:
    print('error handled')