#uma função dentro da outra, sendo q a de dentro irá retornar um valor que será argumento para a função externa

num = input("Digite qualquer número inteiro positivo: ")
num = float(num)
num = abs(num)                                                          #PODE-SE SUBSTITUIR TODAS ESSAS LINHAS
num = round(num)
print(num)

print("-------------------------------")

print(round(abs(float(input("Digite qualquer número inteiro positivo: "))))) # EM UMA LINHA SÓ <<<<<<<<