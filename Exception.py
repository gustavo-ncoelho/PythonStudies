try:
    numerator = int(input("Enter a number to divide: ")) 
    denominator = int(input("Enter a number to divide by: "))   #Aqui o except fará com que o código não encerre caso de um erro
    result = numerator / denominator                            
except ZeroDivisionError as e:      # Aqui é usado um método diferente, que irá ignorar apenas o erro de divisão por zero
    print(e)
    print("You can't divide by zero!!! Idiot!!!")
except ValueError as e:             # Ignora erro de tipo de variável errada
    print(e)
    print("Enter only numbers please")
except Exception as e:         #O Exception é um método que faz com que sejam ignoradas todos os tipos de exceção, e não um tipo específico
    print(e)
    print("Something went wrong ;-;")
else:                                                    #OBS: pode-se atribuir o erro a uma variável e printar o erro
    print(result)     #Aqui, só irá mostrar o resultado caso não haja erros
finally:
    print("This will always execute")      #O finaally, irá rodar mesmo com os erros ignorados(útil para fechar algum arquivo caso tenha sido aberto)
