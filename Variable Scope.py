nome = "Cabelo"           #ESCOPO GLOBAL (a variável nome existe em todos os lugares)

def name():
    nome = "Cabelera"      #ESCOPO LOCAL (a variável nome só existe dentro desta função)
    print(nome)            # porém se a variavel não fosse setada denovo dentro da função
                           # seguiria sendo a variavel global
print(nome)