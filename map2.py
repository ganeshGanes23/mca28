def map2(a):
    if type(a) in [list,set,dict,str,tuple]:
        return len(a)
    else:
        return a
    
    
a=map(map2,[1,(4,5),[7,9],{1:2}])
print(list(a))