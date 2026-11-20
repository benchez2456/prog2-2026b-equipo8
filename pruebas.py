import contextlib
import io
import os
import tempfile
import unittest

from modelo import Alumno, Docente, Materia, Persona
from seguridad import Seguridad
from sistema import SistemaEscolar


class PruebasModelo(unittest.TestCase):
    def prueba_herencia(self):
        self.assertTrue(issubclass(Alumno, Persona))
        self.assertTrue(issubclass(Docente, Persona))

    def prueba_formato(self):
        alumno = Alumno("123456789", "Ana", "INCO").formato()
        docente = Docente("987654321", "Luis", "Sistemas").formato()
        self.assertIn("Carrera", alumno)
        self.assertIn("Departamento", docente)
        self.assertNotEqual(alumno.split("|")[0], docente.split("|")[0])


class PruebasSistema(unittest.TestCase):
    def setUp(self):
        self.s = SistemaEscolar()
        self.s.registrar(Alumno("123456789", "Ana", "INCO"))
        self.s.registrar(Materia("IL350", "Programación 2", 1))

    def prueba_registro_valido(self):
        self.assertTrue(self.s.registrar(Docente("111111111", "Luis", "Sistemas"))[0])

    def prueba_codigo_invalido(self):
        for codigo in ["12345678", "1234567890", "abcdefghi", ""]:
            self.assertFalse(self.s.registrar(Alumno(codigo, "Beto", "INCO"))[0])

    def prueba_nombre_vacio(self):
        self.assertFalse(self.s.registrar(Alumno("222222222", "  ", "INCO"))[0])

    def prueba_codigo_repetido_incluso_entre_tipos(self):
        self.assertFalse(self.s.registrar(Docente("123456789", "Luis", "Sistemas"))[0])

    def prueba_clave_repetida(self):
        self.assertFalse(self.s.registrar(Materia("IL350", "Otra", 5))[0])

    def prueba_cupo_invalido(self):
        self.assertFalse(self.s.registrar(Materia("X1", "Mate", 0))[0])

    def prueba_objeto_desconocido(self):
        self.assertFalse(self.s.registrar("hola")[0])

    def prueba_inscribir(self):
        self.assertTrue(self.s.asignar("123456789", "IL350")[0])
        self.assertEqual(len(self.s.materias["IL350"].inscritos), 1)

    def prueba_no_pasarse_del_cupo(self):
        self.s.registrar(Alumno("222222222", "Beto", "INCO"))
        self.s.asignar("123456789", "IL350")
        self.assertFalse(self.s.asignar("222222222", "IL350")[0])

    def prueba_no_doble_inscripcion(self):
        self.s.registrar(Materia("IL351", "Grande", 10))
        self.s.asignar("123456789", "IL351")
        self.assertFalse(self.s.asignar("123456789", "IL351")[0])

    def prueba_asignar_inexistentes(self):
        self.assertFalse(self.s.asignar("000000000", "IL350")[0])
        self.assertFalse(self.s.asignar("123456789", "NOEXISTE")[0])

    def prueba_docente_no_se_inscribe(self):
        self.s.registrar(Docente("111111111", "Luis", "Sistemas"))
        self.assertFalse(self.s.asignar("111111111", "IL350")[0])

    def prueba_listar_imprime_todo(self):
        salida = io.StringIO()
        with contextlib.redirect_stdout(salida):
            self.s.listar()
        self.assertIn("Ana", salida.getvalue())
        self.assertIn("Programación 2", salida.getvalue())


class PruebasArchivo(unittest.TestCase):
    def prueba_guardar_y_cargar(self):
        original = SistemaEscolar()
        original.registrar(Alumno("123456789", "Ana", "INCO"))
        original.registrar(Docente("111111111", "Luis", "Sistemas"))
        original.registrar(Materia("IL350", "Programación 2", 2))
        original.asignar("123456789", "IL350")
        with tempfile.TemporaryDirectory() as carpeta:
            ruta = os.path.join(carpeta, "prueba.txt")
            original.guardar(ruta)
            copia = SistemaEscolar()
            self.assertEqual(copia.cargar(ruta), 4)
        self.assertEqual(list(copia.personas), ["123456789", "111111111"])
        self.assertEqual(copia.materias["IL350"].cupo_maximo, 2)
        self.assertEqual(copia.materias["IL350"].inscritos[0].nombre, "Ana")

    def prueba_cargar_archivo_inexistente(self):
        self.assertEqual(SistemaEscolar().cargar("no_existe.txt"), 0)


class PruebasSeguridad(unittest.TestCase):
    def prueba_verificar_password(self):
        seg = Seguridad()
        salt, hash_ = seg.crear_credencial("secreta123")
        self.assertTrue(seg.verificar("secreta123", salt, hash_))
        self.assertFalse(seg.verificar("otra", salt, hash_))


if __name__ == "__main__":
    unittest.TestLoader.testMethodPrefix = "prueba"
    unittest.main()