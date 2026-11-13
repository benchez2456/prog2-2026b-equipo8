from getpass import getpass
from usuarios import SistemaUsuarios

sistema = SistemaUsuarios()

def menu_usuarios(usuario_actual):
    while True:
        print("\n===== MENÚ DE USUARIOS =====")
        print("1.- Consultar\n2.- Actualizar\n3.- Eliminar\n4.- Cambiar contraseña\n5.- Cerrar sesion")
        op = input("\nSeleccione una opción: ")

        if op == "1":
            for u in sistema.listar():
                print(f"Usuario: {u}")
        elif op == "2":
            u = input("Usuario a modificar: ").strip()
            nu = input("Nuevo usuario: ").strip()
            nc = input("Nuevo código: ").strip()
            print(sistema.actualizar(u, nu, nc)[1])
        elif op == "3":
            u = input("Usuario a eliminar: ").strip()
            if input("¿Está seguro? (s/n): ").lower() == "s":
                print(sistema.eliminar(u)[1])
        elif op == "4":
            actual = getpass("Contraseña actual: ")
            nueva = getpass("Nueva contraseña: ")
            print(sistema.cambiar_password(usuario_actual, actual, nueva)[1])
        elif op == "5":
            print("Cerrando sesion...")
            break
        else:
            print("Opción no válida.")

def main():
    while True:
        print("\n===== SISTEMA DE USUARIOS =====")
        print("1.- Iniciar sesión\n2.- Registrarse\n3.- Salir")
        op = input("\nSeleccione una opción: ")

        if op == "1":
            usuario = input("Usuario: ").strip()
            ok, msg = sistema.iniciar_sesion(usuario, getpass("Contraseña: "))
            print(msg)
            if ok:
                menu_usuarios(usuario)

        elif op == "2":
            usuario = input("Usuario: ").strip()
            codigo = input("Codigo de estudiante: ").strip()
            password = getpass("Contraseña (min. 8 caracteres): ")
            if getpass("Confirme la contraseña: ") != password:
                print("Las contraseñas no coniciden")
            else:
                print(sistema.registrar(usuario, codigo, password)[1])
        elif op == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()