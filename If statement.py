
age = int(input("How old are you ?: "))

if age == 100:                            #Para igualdade em alguma condição deve-se usar "==", pois se usar somente "=" o sistema irá entender que vc está adicionando outro valor a variável (age neste caso)
    print("You are a century old!!!")
elif age >= 18:                           #Condição SE, se a condição for satisfeita, fará a ação seguinte
    print("You are an adult!!!")          #OBS: É necessário ":" para indicar qual a condição do if,else,...
elif age < 0:                             #elif (else if) É uma condição intermediária (entre o if e o else), se for falsa irá para a próxima condição
    print("You haven't been born yet!")
else:                                     #Condição SE NÃO, se a condição não for satisfeita, fará outra ação
    print("You are a child!!!")           #else não acompanha condição, pois é satisfeito caso nenhuma conidção anterior tenha sido satisfeita

# LOGICAL OPERATORS: (and,or,not)

temp = int(input("What is the temperature outside?: "))

if temp >= 0 and temp <= 30:                   #O and significa que as DUAS condições TEM que ser verdadeiras
    print("The temperature is good today!")
    print("go outside!")
elif temp < 0 or temp > 30:                    #O or significa que UMA OU OUTRA condição (nunca as duas) devem ser verdadeiras
    print("the temperature is bad today!")
    print("stay inside!")

#OBS: O not irá inverter a condição, ou seja, se ela for true, será interpretada como false e vice versa. Como se o not fosse um -1
#É escrito assim:
# if not(temp >= 0 and temp <= 30):







