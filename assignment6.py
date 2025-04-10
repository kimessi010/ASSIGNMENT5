class car:
    def __init__(self, type, color, engine):
        self.type=type
        self.color=color
        self.engine=engine
    
car1=car('Ferrari', 'Red', 'diesel')
print(car1.engine)

#an example of inheritance
class car2():
    def __init__(self, wheels):
        self.wheels=wheels
class vehicle(car2):
    pass

vehicle2=car2 (4)
print(vehicle2.wheels)

#an example of polymorphism
class Ferrari:
    def driver(self):
        return('Lewis Hamilton and Charles Leclerc')
class Mclaren:
    def driver(self ):
        return('Lando Noris and Oscar Piastri')
class Mercedes:
    def driver(self):
        return ('George Russel and Kimi Antonelli')
class RB:
    def driver(self):
        return('Max Vertsappen and whoever Horner decides')

for drivers  in [Ferrari(), Mclaren(), Mercedes(), RB()]:
    print(drivers.driver())
    
#an example of encapsulation

class color:
    def __init__(self):
        self.__color='Blue'

    def choose_color(self):
        if self.__color=='Blue':
            return ('Color is blue')
        else:
            return('Nah, choose another color')
    
guess=color()
print( guess.choose_color())

