class Animal:

    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):
    
    def eat(self):                                  #Aqui mesmo Rabbit sendo uma subclasse de Animal, o método eat foi reestabelecido para a classe Rabbit (Mesmo sua classe mãe ja tendo o método eat)
        print("This rabbit is eating a carrot")  

rabbit = Rabbit()
rabbit.eat()