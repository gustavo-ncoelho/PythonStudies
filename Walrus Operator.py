# walrus operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

#print(happy = True)              <- isso aqui não funcionaria pois não é possível criar um variável dentro do print

print(happy := True)             #<- Porém usando o operador :=, isso é possível

#-------------------------------------------------------------------------------------------------------------------#

# foods = list()
# while True:
#   food = input("What food do you like?: ")          
#       if food == "quit":
#           break
#   foods.append(food)

foods = list()
while food := input("What food do you like?: ") != "quit":        #<- ISSO É IGUAL AO CÓGIDO DE CIMA ^^, porém utilizando o operador de walrus
    foods.append(food)                                            #Tudo que estava no While de cima ^^ foi escrito neste como condicional