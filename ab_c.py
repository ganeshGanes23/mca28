from abc import ABC,abstractmethod


class car(ABC):
    def __init__(self,name,color,price,):
        self.name=name
        self.color=color
        self.price=price
        self.speed=0
    @abstractmethod
    def speed_up(self):
        pass
class Bmw(car):
    def speed_up(self):
        self.speed+=5

Bmw1=Bmw('xyz','white',45)
