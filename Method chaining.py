#method chaining = you can call multiple methods sequentially

class Car:

    def turnOn(self):
        print("You start the Engine")
        return self                      #OBS: se não usar o return self, o método não terá retorno (None),
    
    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You setp on the brakes")
        return self  
    def turnOff(self):
        print("You turn off the engine")
        return self  
    
car = Car()
car.turnOn().drive().brake().turnOff()   #Só é possível chamar em sequência métodos não nulos (None), por isso devemos botar o return em cada método