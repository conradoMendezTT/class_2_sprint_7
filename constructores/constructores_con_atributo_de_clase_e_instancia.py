class User:
    is_registered = True  # Atributo de clase compartido por todos los objetos

    def __init__(self, name, login_user):
        # Atributos de instancia personalizados
        self.name = name
        self.login_user = login_user

# Crear objetos con valores únicos
user_1 = User("Mark", "mark@gmail.com")
user_2 = User("Alice", "alice@gmail.com")
user_3 = User("Bob", "bob@gmail.com")

# Imprimir los atributos de cada objeto (con referencia directa a la clase para is_registered)
print(f"user_1: name={user_1.name}, login_user={user_1.login_user}, is_registered={User.is_registered}")
print(f"user_2: name={user_2.name}, login_user={user_2.login_user}, is_registered={User.is_registered}")
print(f"user_3: name={user_3.name}, login_user={user_3.login_user}, is_registered={User.is_registered}")
