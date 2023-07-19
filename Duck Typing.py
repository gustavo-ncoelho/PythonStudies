# duck typing = concept where the class of an object is less important than the methods/attributes
#               class type is not checked if minimum methods/attributes are present
#               “If it walks like a duck, and it quacks like a duck, then it must be a duck.”

class Duck:

    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is qwuacking")

class Chicken:

    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")

class Person():

    def catch(self, duck):                   #AQUI no método catch, é utilizado o objeto duck como argumento do método
        duck.walk()                          #sendo utilizados os métodos walk e talk da classe duck
        duck.talk()
        print("You caught the critter!")


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)                       #Porém aqui se eu colocar como argumento um objeto chicken (QUE
                                            #CONTÉM MÉTODOS COM MESMO NOME DOS MÉTODOS DE duck), irá rodar 
                                            # normalmente porém com os métodos/atributos de chicken (mesmo não
                                            # sendo o argumento esperado pelo método catch) 