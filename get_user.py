import users

LOGIN_WITH_NAME = "nombre"
LOGIN_WITH_NUMBER = "numero"
REGISTER = "registrarme"


def get_user():
    print("nombre, numero, registrarme")
    opcion = input("Escribe la opcion con la que te quires loguear : ")

    user_manager = users.Users()

    if opcion == LOGIN_WITH_NAME:
        name = input("Escribe tu nombre de usuario: ")
        return user_manager.get_user_by_name(name)
    elif opcion == LOGIN_WITH_NUMBER:
        number = input("Escribe tu numero de celular :")
        return user_manager.get_user_by_number(number)
    elif opcion == REGISTER:
        name = input("Escribe tu nombre : ")
        number = input("Escribe tu numero de telefono : ")
        return user_manager.create_user(name, number)
    else:
        print("Opcion no valida")
        return get_user()
