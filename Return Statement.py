# return statement = Functions send Python values/objects back to the caller.
#                    These valeus/objects are known as the function's return value

def mutiply(n1,n2):               # Para uma função retornar um resultado, usa-se o return
    result = n1 * n2
    return result

print(mutiply(6,8))


def multiply1(n1,n2):             # Pode-se colocar o return direto sem declarar a variável result antes
    return n1 * n2

print(multiply1(7,8))


def multiply2(n1,n2):
    return n1 * n2

x = multiply2(9,2)               # Pode-se declarar uma variável com a função, como nesse caso o x

print(x)