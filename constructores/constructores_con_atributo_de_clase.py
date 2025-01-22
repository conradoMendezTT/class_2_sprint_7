class User:
    is_registered = True
    name = "Mark"
    login_user = "mark@gmail.com"

    def __init__(self):
        # Imprimir los atributos de clase
        print(f"Atributos de clase: name={User.name}, login_user={User.login_user}, is_registered={User.is_registered}")

# Crear un objeto
user_1 = User()
user_2 = User()
user_3 = User()