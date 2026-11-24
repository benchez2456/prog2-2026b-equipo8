from modelo import Alumno, Docente, Materia
from sistema import SistemaEscolar

RUTA = "escuela.txt"


def responder(sistema, resultado):
    """Muestra el mensaje y guarda en el archivo si la operación funcionó."""
    ok, mensaje = resultado
    print(mensaje)
    if ok:
        sistema.guardar(RUTA)


def pedir(texto):
    return input(texto).strip()


def main():
    sistema = SistemaEscolar()
    sistema.cargar(RUTA)
    while True:
        print("\n===== SISTEMA ESCOLAR =====")
        print("1.- Registrar alumno\n2.- Registrar docente\n3.- Registrar materia")
        print("4.- Inscribir alumno en materia\n5.- Asignar docente a materia")
        print("6.- Listar todo\n7.- Salir")
        op = pedir("\nSeleccione una opción: ")

        if op == "1":
            alumno = Alumno(pedir("Código: "), pedir("Nombre: "), pedir("Carrera: "))
            responder(sistema, sistema.registrar(alumno))
        elif op == "2":
            docente = Docente(pedir("Código: "), pedir("Nombre: "), pedir("Departamento: "))
            responder(sistema, sistema.registrar(docente))
        elif op == "3":
            clave, nombre = pedir("Clave: "), pedir("Nombre: ")
            try:
                cupo = int(pedir("Cupo máximo: "))
            except ValueError:
                print("El cupo debe ser un número entero.")
                continue
            responder(sistema, sistema.registrar(Materia(clave, nombre, cupo)))
        elif op == "4":
            responder(sistema, sistema.asignar(pedir("Código del alumno: "),
                                               pedir("Clave de la materia: ")))
        elif op == "5":
            responder(sistema, sistema.asignar_docente(pedir("Código del docente: "),
                                                       pedir("Clave de la materia: ")))
        elif op == "6":
            sistema.listar()
        elif op == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()