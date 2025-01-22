sheep = [1, 2, 3, 4, 5]

for i in sheep: # Bucle exterior
    if i == 1:
        print(i, ' oveja')
    elif i == 3:  # Sentencia if anidada: si la variable es igual a 3,
        continue  # omite la iteraciónaa
    else:
        print(i, ' ovejas')


print('¿Adónde se fue una oveja?') # Esta línea está fuera del bucle