import Modules2 as mdl  #Pode-se usar um apelido para a classe, no caso tornamos Modules2 em mdl

mdl.hello()
mdl.bye()

print("-----------------------------")

from Modules2 import hello,bye      #Aqui pode-se chamar apenas os métodos de uma classe, sem necessitar escrever a classe na hra de chamar o método
                                    # SE USAR import * IRÁ CHAMAR TODOS OS MÉTODOS DA CLASSE
hello()
bye()