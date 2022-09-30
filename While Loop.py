
name = ""

while len(name) == 0:                     #while (função ENQUANTO) len (comprimento do nome) for igual a 0, irá repetir a mensagem "Enter your name"
    name = input("Enter your name: ")
                                          #Depois q o nome for digitado, o len(name) == 0 não será mais satisfeito e sairá do loop, e seguirá para o print "Hello "+name
print("Hello "+name)

#OBS: EXISTEM DIFERENTES MODOS DE FAZER A FUNÇÃO ACIMA, COMO:

name1 = None

while not name1:
    name1 = input("Enter your name: ")

print("Hello "+name1)