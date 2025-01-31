class User():
    is_registered = True
    name = "Mark"
    login_user = "mark@gmail.com"


print(f"Registrado --- {User.is_registered}")
print(f"Nombre del usuario --- {User.name}")
print(f"Email de usuario --- {User.login_user}\n")

#Cambio algun atributo
User.name = "Conrado"
User.is_registered = False

#Imprimo lo mismo que arriba
print("CAMBIANDO LOS ATRIBUTOS\n")

print(f"Registrado --- {User.is_registered}")
print(f"Nombre del usuario --- {User.name}")
print(f"Email de usuario --- {User.login_user}")