class Animal:                 # <--- CLASSE MÃE

    alive = True

    def eat(self):
        print("This animal is eating")
    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):             # <---  CLASSE FILHA      No caso Rabbit(Animal) a de fora é a filha e a de dentro é a mãe

    def run(self):
        print("This rabbit is running")

class Fish(Animal):

    def swim(self):
        print("This fish is swimming")

class Hawk(Animal):

    def fly(self):
        print("This hawk is flying")

rabbit = Rabbit()         # <--- Aqui são instanciados os objetos
fish = Fish()
hawk = Hawk()

rabbit.run()
fish.swim()
hawk.fly()