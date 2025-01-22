class User:
    is_registered = True  # Atributo de clase compartido por todos los objetos

    def __init__(self, name, login_user):
        # Atributos de instancia personalizados
        self.name = name
        self.login_user = login_user

    def describe(self):
        print(f"user_1: name={self.name}, login_user= {self.login_user}, is_registered={User.is_registered}\n")

# Crear objetos con valores únicos
user_1 = User("Conrado", "mark@gmail.com")
user_2 = User("Cohorte", "alice@gmail.com")
user_3 = User("20", "bob@gmail.com")

# Imprimimos los atribtuos de cada objeto con un metodo
user_1.describe()
user_2.describe()
user_3.describe()