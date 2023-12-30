class Base:
    x=10
    y=20
    def __init__(self,name):
        self.name=name
class found(Base):
    a=30
    b=40
    def __init__(self,name,a,b):
        super().__init__(name)
        self.a=a
        self.b=b
class heap(found):
    def __init__(self,name,a,b,d):
        super().__init__(name,a,b)
        self.d=d
obj= heap(5,6,7,4)