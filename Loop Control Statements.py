#  Loop Control Statements  =  Maneiras de mudar o loop de sua execução natural

# break =       used to terminate the loop entirely
# continue =    skips to the next iteration of the loop
# pass =        does nothing, acts as a placeholder

#while True:
#    name = input("Enter your name: ")
#    if name != "":                     # Se name for diferente de "", continue, se não irá ativar o break
#        break                          # Comando break: Quando a condição é satisfeita, irá parar de rodas o código


phone_number = "(51)985150804"

for i in phone_number:         # for i in: irá pegar a string separar por caracter (transformou em lista)
    if i == "(":
        continue               # continue irá pular o armarinho onde o "(" está armazenado.
    if i == ")":
        continue
    print(i, end="")           #OBS: end="" fará com que o print saia todo na mesma linha


# for y in range(1,21):
#
#    if y == 13:
#        pass                      # pass irá passar (não fazer nada)
#    else:
#        print(y)






