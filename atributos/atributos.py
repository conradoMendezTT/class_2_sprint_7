class User():
    is_registered = True
    name = "Mark"
    login_user = "mark@gmail.com"


print(User.is_registered)
print(User.name)

#Cambio algun atributo
User.name = "Conrado"

#Imprimo lo mismo que arriba
print(User.is_registered)
print(f"El nuevo nombre asignado es: {User.name}")