#function = a block of code which is executed only when it is called

def hello():
    print("hello!")

hello()

def hello1(name):                   # Aqui mostra que a função hello1 tem uma variável "vazia" que poderá ser preenchida
    print("Hello " + name)          # IMPORTANTE: Essas variáveis dentro das função são chamadas de "arguments"
    print("Have a nice day")

hello1("Cabelera")                  # Aqui a variável name irá receber a string "Cabelera" TEMPORARIAMENTE

def hello2(name1):
    print("Hello " + name1)
    print("Have a good night")

my_name = "Gustavo"

hello2(my_name)                     # Aqui variável name1 recebe TEMPORARIAMENTE o valor da variável my_name

def hello3(first_name,last_name):
    print("Hello " + first_name + " " + last_name)
    print("Have a fucking big good day")

hello3("Gustavo","Coelho")          # Aqui é o mesmo caso porém com duas variáveis

def hello4(first_name,last_name,age):
    print("Hello " + first_name + " " + last_name)
    print("You are " + str(age) + " years old")           #OBS: Quando uma variável irá receber int ou float, deve ser convertida para str caso esteja num print
    print("Have a fucking big good day")

hello4("Gustavo","Coelho",24)