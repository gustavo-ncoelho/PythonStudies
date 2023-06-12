from OOP2 import Car

car1 = Car("Chevy", "Corvette", 2021, "Blue")
car2 = Car("Ford", "Mustang", 2022, "Red")

car1.wheels = 2      #Aqui é alterado o aributo da classe

print(car1.wheels)
print(car2.wheels)

print(car1.make)
print(car1.model)
print(car1.year)
print(car1.color)

car1.drive()
car1.stop()

print(Car.wheels)     #Pode-se acessar atributos da classe chamando-os pelo nome da própria classe, e não necessariamente dos objetos