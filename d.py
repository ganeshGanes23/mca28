x=50
def func():
    global x
print('x ix',x)
x=2
print('Changed global x to',x)
func()
print('Value of x  is',x)

