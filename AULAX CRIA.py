# age = ""
# while age == "":
#     age = input("how old are u?")
#
# age = int(age)
#
# if age > 100:
#     print("damn u r too old")
# elif age < 0:
#     print("u r not born yet")
# else:
#     age += 1
#     print("next year u'll be " + str(age))
#
# height = ""
# while height == "":
#     height = input("how tall r u ?")
#
# height = float(height)
#
# if height >= 1.75 and height < 2:
#     print("u r tall")
# elif height <= 1.75 and height > 1:
#     print("u r small")
# elif height > 2:
#     print("wtf u r so tall")
# elif height < 1:
#     print("u r a mini person hehe")
#
# local = ""
# while local == "":
#     local = input("what is the name of the city u live in ?")
#
# if local == "torres":
#     print("U live in the best beach of this fcking wrld")
# else:
#     print("hm ok, u live in " + local)

name = input("Qual seu nome ?: ")
weight = float(input("Digite seu peso: "))
height = float(input("Digite sua altura: "))
imc = weight/pow(height,2)
print(name + ", seu imc é: " + str(imc))



