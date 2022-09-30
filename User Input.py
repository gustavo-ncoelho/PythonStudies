name = input("What is your name ?: ")             #Variável name vai ser atribuída ao valor digitado pelo usuário
age = int(input("How old are you ?: "))           #Como idade é um número inteiro, deve-se especificar antes do input que a variável é int CASO QUEIRA FAZER OPERAÇÃO MATEMÁTICA COM A VARIÁVEL
height = float(input("How tall are you ?: "))     #Mesma coisa do exemplo de cima porém com variável float. SÓ É NECESSÁRIO FAZER ESSA MUDANÇA CASO QUEIRA FAZER OPERAÇÃO MATEMÁTICA

print("Hello "+name)
print("You are "+str(age)+" years old")          #str só pode ser printada com str, logo a variável age que antes era int, foi transformada em str para ser printada junto com as outras frases (que são str)
print("You are "+str(height)+"m tall")