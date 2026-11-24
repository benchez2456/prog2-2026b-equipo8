import os

from modelo import Alumno, Docente, Materia


class Almacenamiento:
    """Se encarga de convertir el sistema a líneas de texto y viceversa."""

    separador = "|"

    def guardar(self, sistema, ruta):
        """Escribe personas, materias, inscripciones y docentes, una por línea."""
        with open(ruta, "w", encoding="utf-8") as archivo:
            todos = list(sistema.personas.values()) + list(sistema.materias.values())
            for objeto in todos:
                archivo.write(self.separador.join(objeto.campos()) + "\n")
            for materia in sistema.materias.values():
                for alumno in materia.inscritos:
                    partes = ["INSCRIPCION", alumno.codigo, materia.clave]
                    archivo.write(self.separador.join(partes) + "\n")
            for materia in sistema.materias.values():
                if materia.docente:
                    partes = ["IMPARTE", materia.docente.codigo, materia.clave]
                    archivo.write(self.separador.join(partes) + "\n")

    def cargar(self, sistema, ruta):
        """Lee el archivo y rellena el sistema. Regresa cuántas líneas cargó."""
        if not os.path.exists(ruta):
            return 0
        cargadas = 0
        with open(ruta, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = linea.strip().split(self.separador)
                if self.leer_linea(sistema, partes):
                    cargadas += 1
        return cargadas

    def leer_linea(self, sistema, partes):
        """Mete una línea al sistema usando sus propias validaciones."""
        if partes[0] == "INSCRIPCION" and len(partes) == 3:
            return sistema.asignar(partes[1], partes[2])[0]
        if partes[0] == "IMPARTE" and len(partes) == 3:
            return sistema.asignar_docente(partes[1], partes[2])[0]
        objeto = self.crear(partes)
        return objeto is not None and sistema.registrar(objeto)[0]

    def crear(self, partes):
        """Convierte una línea separada en un objeto, o None si está mal."""
        try:
            if len(partes) == 4:
                if partes[0] == "ALUMNO":
                    return Alumno(partes[1], partes[2], partes[3])
                if partes[0] == "DOCENTE":
                    return Docente(partes[1], partes[2], partes[3])
                if partes[0] == "MATERIA":
                    return Materia(partes[1], partes[2], int(partes[3]))
        except ValueError:
            pass
        return None