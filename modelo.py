class Persona:
    """Guarda lo que tienen en común"""

    tipo = "PERSONA"

    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def formato(self):
        return f"[Persona] {self.codigo} | {self.nombre}"

    def campos(self):
        return [self.tipo, self.codigo, self.nombre]


class Alumno(Persona):
    """Estudia una carrera y puede inscribirse"""

    tipo = "ALUMNO"

    def __init__(self, codigo, nombre, carrera):
        super().__init__(codigo, nombre)
        self.carrera = carrera

    def formato(self):
        return f"[Alumno] {self.codigo} | {self.nombre} | Carrera: {self.carrera}"

    def campos(self):
        return super().campos() + [self.carrera]


class Docente(Persona):
    """Una persona que imparte una materia(maestr@)"""

    tipo = "DOCENTE"

    def __init__(self, codigo, nombre, departamento):
        super().__init__(codigo, nombre)
        self.departamento = departamento

    def formato(self):
        return f"[Docente] {self.codigo} | {self.nombre} | Departamento: {self.departamento}"

    def campos(self):
        return super().campos() + [self.departamento]


class Materia:
    """Contenedor con cupo limitado: Alumnos inscritos."""

    tipo = "MATERIA"

    def __init__(self, clave, nombre, cupo_maximo):
        self.clave = clave
        self.nombre = nombre
        self.cupo_maximo = cupo_maximo
        self.inscritos = []  # lista de objetos Alumno

    def hay_cupo(self):
        return len(self.inscritos) < self.cupo_maximo

    def inscribir(self, alumno):
        """Agrega al alumno si hay lugar regresa True o False."""
        if not self.hay_cupo():
            return False
        self.inscritos.append(alumno)
        return True

    def formato(self):
        texto = (f"[Materia] {self.clave} | {self.nombre} | "
                 f"Cupo: {len(self.inscritos)}/{self.cupo_maximo}")
        for alumno in self.inscritos:
            texto += f"\n      - {alumno.codigo} {alumno.nombre}"
        return texto

    def campos(self):
        return [self.tipo, self.clave, self.nombre, str(self.cupo_maximo)]