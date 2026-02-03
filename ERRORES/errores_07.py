#clase base de la jerarquía de Errores (excepciones)
class ErrorAplicacion(Exception):
    pass

class ErrorValidacion(ErrorAplicacion):
    pass

class ErrorPermisos(ErrorAplicacion):
    pass

#Usuarios del sistema
lista_de_roles_de_usuarios =["visitante", "admin", "editor", "hacker"]

# Lógica para verificar rol del usuario: sólo usuarios con rol autorizador puede ingresar al sistema: admin y editor
def verificar_usuario(rol):
    if rol == "visitante":
        raise ErrorPermisos("Acceso no autorizado!")
    elif rol not in ["admin", "editor"]: # ["admin", "editor"] usuarios con acceso permitido
        raise ErrorValidacion("Rol no existe en el sistema.")
    else:
        print(f"Bienvenido al sistema con el rol {rol}")


print("Simular verificación de listado de usuarios")

for rol in lista_de_roles_de_usuarios:
    print(f"Intentando ingresar al sistema como: {rol}")
    try:
        verificar_usuario(rol)
    except ErrorPermisos as error:
        print(f"Error: {error}")
    except ErrorValidacion as error:
        print(f"Error: {error}")
    except ErrorAplicacion:
        print("Ocurrio un error inesperado en la aplicación. Contacte al administrador.")

