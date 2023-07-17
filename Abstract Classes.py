from abc import ABC, abstractmethod      # abc = abstract brasic class

class Vehicle(ABC):        #Com a biblioteca ABC, se vc fizer uma classe filha de ABC, ela será abstrata e será necessário o @abstractmethod para seus métodos abstratos (e vazios, usando pass) 
                           # A classe filhad e ABC só se tornará abstrata se tiver no mínimo um método abstrato
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):                     #Classes filhas de classes abstratas são OBRIGADAS a implementar todos os métodos abstratos da classe mãe

    def go(self):
        print("You drive the car")

    def stop(self):
        print("This car is stopped")

class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("This motorcycle is stopped")


#vehicle = Vehicle()         não é possível instanciar objetos de classes abstratas
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()

#vehicle.stop()
car.stop()
motorcycle.stop()