
# Codio Duplicado
def A():
    a = 10
    b = 20
    suma = a + b
    print(f"El resultado de A es: {suma}")

def B():
    a = 10
    b = 20
    suma = a + b
    print(f"El resultado de B es: {suma}")

# Llamadas a las funciones
A()
B()


#Codigo sin duplicar
def calcular_suma():
    a = 10
    b = 20
    return a + b

def A():
    suma = calcular_suma()
    print(f"El resultado de A es: {suma}")

def B():
    suma = calcular_suma()
    print(f"El resultado de B es: {suma}")

# Llamadas a las funciones
A()
B()
