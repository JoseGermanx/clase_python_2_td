
class ErrorRegistro(Exception):
    pass

# Que el nombre no esté vacío
class NombreVacioError(ErrorRegistro):
    pass

# Que la edad sea mayor a 0
class EdadInvalidadError(ErrorRegistro):
    pass

# Que el email contenga @
class EmailInvalidoError(ErrorRegistro):
    pass

# Tipo de literal en edad
class TipoDeDatoEdadError(ErrorRegistro):
    pass


#función para validar datos
def validar_campos(nombre, edad, email):
    #Validación de nombre
   if not nombre or len(nombre.strip()) == 0:
       raise NombreVacioError("El campo nombre es obligatorio.")
   
   #Validación de edad ->> revisar validación
   if not isinstance(int(edad), int):
       raise TipoDeDatoEdadError("La edad debe ser un tipo válido")
   if int(edad) < 0:
       raise EdadInvalidadError("La edad debe ser mayor a cero.")
   
   #Validación de email
   if "@" not in email:
       raise EmailInvalidoError("Email debe ser un formato válido (@)")
   
   return True
   

#función con lógico de regsitro de usuario
def registrar_usuario(nombre, edad, email):
   
   try:
       if validar_campos(nombre, edad, email):
           #se crea el nuevo usuario
           new_user = {
           "nombre": nombre,
           "edad": edad,
           "email": email
            }

            # Se imprime el resultado del registro
           print(f"Ok. Usuario registrado correctamente con los datos {new_user['nombre']}, edad: {new_user['edad']} y email {new_user["email"]}")
   except Exception as error:
       print(f"Error en registro_usuario: {error}")
       

#Lógica menú básico de registro
print("===== Inicio Registro =====")
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
email = input("Ingrese su email: ")


try:
    registrar_usuario(nombre, edad, email)
except NombreVacioError as error:
    print(f"Error en el campo nombre: {error}")
except EdadInvalidadError as error:
    print(f"Error en el campo edad: {error}")
except EmailInvalidoError as error:
    print(f"Error en el campo email: {error}")
except ErrorRegistro as error:
    print(f"Error general: {error}")
finally:
    print("====Fín proceso de registro====")