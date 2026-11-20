from almacen import Almacenamiento
from modelo import Alumno, Materia, Persona


class Validador:
    """Se encarga de decir si un dato es aceptable o no."""

    longitud_codigo = 9
    separador = "|"

    def validar_codigo(self, codigo):
        return codigo.isdigit() and len(codigo) == self.longitud_codigo

    def validar_texto(self, texto):
        return bool(texto.strip()) and self.separador not in texto

    def validar_cupo(self, cupo):
        return isinstance(cupo, int) and cupo > 0


class SistemaEscolar:
    """Guarda personas y materias"""

    def __init__(self):
        self.personas = {}
        self.materias = {}
        self.validador = Validador()
        self.almacenamiento = Almacenamiento()

    def registrar(self, objeto):
        """Da de alta una persona o una materia. Regresa ok + mensaje."""
        if isinstance(objeto, Persona):
            return self.registrar_persona(objeto)
        if isinstance(objeto, Materia):
            return self.registrar_materia(objeto)
        return False, "Tipo de objeto no reconocido."

    def registrar_persona(self, persona):
        if not self.validador.validar_codigo(persona.codigo):
            return False, "El código debe tener 9 dígitos."
        if not all(self.validador.validar_texto(c) for c in persona.campos()[2:]):
            return False, "El nombre y los demás datos no pueden ir vacíos ni llevar '|'."
        if persona.codigo in self.personas:
            return False, "Ese código ya está registrado."
        self.personas[persona.codigo] = persona
        return True, f"{persona.nombre} registrado correctamente."

    def registrar_materia(self, materia):
        if not self.validador.validar_texto(materia.clave):
            return False, "La clave no puede ir vacía ni llevar '|'."
        if not self.validador.validar_texto(materia.nombre):
            return False, "El nombre no puede ir vacío ni llevar '|'."
        if not self.validador.validar_cupo(materia.cupo_maximo):
            return False, "El cupo debe ser un número entero mayor que 0."
        if materia.clave in self.materias:
            return False, "Esa clave de materia ya existe."
        self.materias[materia.clave] = materia
        return True, f"Materia {materia.nombre} registrada correctamente."

    def asignar(self, identificador, clave):
        """Inscribe al alumno (por su código) en la materia (con clave)."""
        persona = self.personas.get(identificador)
        materia = self.materias.get(clave)
        if persona is None:
            return False, "No existe una persona con ese código."
        if not isinstance(persona, Alumno):
            return False, "Solo los alumnos pueden inscribirse a una materia."
        if materia is None:
            return False, "No existe una materia con esa clave."
        if persona in materia.inscritos:
            return False, "El alumno ya está inscrito en esa materia."
        if not materia.inscribir(persona):
            return False, "La materia ya no tiene cupo."
        return True, f"{persona.nombre} inscrito en {materia.nombre}."

    def listar(self):
        """Imprime todo; cada objeto usa su propio formato."""
        print("\n--- Personas ---")
        for persona in self.personas.values():
            print(persona.formato())
        if not self.personas:
            print("(sin registros)")
        print("\n--- Materias ---")
        for materia in self.materias.values():
            print(materia.formato())
        if not self.materias:
            print("(sin registros)")

    def guardar(self, ruta="escuela.txt"):
        self.almacenamiento.guardar(self, ruta)

    def cargar(self, ruta="escuela.txt"):
        return self.almacenamiento.cargar(self, ruta)