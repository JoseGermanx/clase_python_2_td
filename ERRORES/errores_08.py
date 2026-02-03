
class ErrorRegistro(Exception):
    pass

#Simulación de registro de usuarios por medio de un email

#lógica para validar que una email sea un email: tenga @
def validar_email(email):
    if "@" not in email:
        raise ValueError("El email no contiene @.")



# lógica para registrar al usuario y utilizará a la función de validar_email para verificar que el email sea correcto
def registrar_usuario(email):
    try:
        validar_email(email)
        #lógica del para resgistrar al usuario
        return email
    except ValueError as error:
        print(f"Log ---- Hubo un fallo al intentar registrar al usuario. Detalle: {error}")
        raise ErrorRegistro("Hubo un error al registrar, correo inválido.")


# Registro de usuarios (Front)

print("Bienvenido al sistema de registro")
email = input("Ingrese el email para registrar: ")

try:
    print(f"Usuario registrado con el email: {registrar_usuario(email)}")
except ErrorRegistro as error:
    print(error)