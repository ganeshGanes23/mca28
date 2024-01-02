class add3:
    @staticmethod
    def add3(a,b,c,d):
        return a+b+c+d
class add2:
    @staticmethod
    def add2(a,b,c):
        return a+b+c
class add(add3,add2):
    pass

class sub2:
    @staticmethod
    def sub2(a,b):
        return a-b

class cal(add,add2):
    pass

obj=cal()