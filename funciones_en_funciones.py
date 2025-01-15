#Datos de manera manual
def procesar_datos_con_token_manual():
    # Token establecido manualmente
    token = "abc1sasdfdfg23"
    print(f"Procesando datos con el token: {token}")

procesar_datos_con_token_manual()


#Funcion dentro de funcion
import random
import string

# Función que genera un token aleatorio
def generar_token():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

#Funcion que procesa el token y lo imprime
def procesar_datos():
    token = generar_token()  # Se llama a la función para obtener un nuevo token
    print(f"Procesando datos con el token: {token}")

# Llamada a la función
procesar_datos()


