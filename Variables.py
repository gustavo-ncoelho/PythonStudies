print("i love pizza")             #print para mostrar algo
print("its really good")          #tudo entre "" será mostrado exatamente como foi digitado

   #VARIÁVEIS:
   #string:                                    #string é uma variável de texto

first_name = "Gustavo"                         #first_name é uma variável "string"
last_name = "Coelho"
full_name = first_name +" "+ last_name         #usa-se o espaço entre "" para colocar espaço na junção das variáveis

print(type(first_name))                #a função "type" irá mostrar o tipo da variável desejada

print("Hello "+full_name)

   #integer:

age = 23               #int é uma variável numérica (NUMERO INTEIRO) que pode ser usada em operações matemáticas
age += 1               # "age += 1"     é um atalho para     "age = age + 1"
print(age)
print(type(age))

#print("your age is "+age)        # <--- isso não pode acontecer pois não se pode juntar string com int
   #para resolver isso deve-se transformar o int em str da seguinte forma:

print("your age is "+str(age))           #str antes da variável int irá transformá-la em str

#float:               #Float é uma variável de NÚMERO DECIMAL

height = 1.75
print(height)
print(type(height))
print("your height is " + str(height) + "m")

#boolean              #Variável que armazena apenas "true" ou "false"

human = False
print(type(human))
print("are you a human ? " + str(human))         #Sempre transformar em string para aparecer em print