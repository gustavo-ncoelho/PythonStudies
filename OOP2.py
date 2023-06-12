class Car:
                    # <--- ISSO AQUI É UM ATRIBUTO DA CLASSE        
    wheels = 4      #Aqui é criado um atributo fixo para todos os objetos da classe (por isso está fora do construtor)

    def __init__(self, make, model, year, color):     #__init__ é necessário pois é o construtor
        self.make = make                              # self também é sempre utilizado para dizer que o atributo ou método pertence à classe em si que está trabalhando
        self.model = model
        self.year = year                              # <--- ISSO SÃO ATRIBUTOS DAS INSTÂNCIAS (OBJETOS)
        self.color = color                             

    def drive(self):
        print("This " + self.model + " is driving")   #O self serve para referenciar à cada objeto que será criado

    def stop(self):
        print("This car is stopped")