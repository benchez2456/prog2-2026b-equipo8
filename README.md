# Sistema escolar

Programa de consola para registrar alumnos, docentes y materias con cupo limitado,
e inscribir alumnos en materias. La información se guarda en `escuela.txt`.

## Cómo se corre

    python main.py       # el programa
    python pruebas.py    # la suite de pruebas

Solo usa la biblioteca estándar de Python 3.

## Estructura

| Archivo | De qué se encarga |
|---|---|
| `modelo.py` | Las clases `Persona`, `Alumno`, `Docente` y `Materia` |
| `sistema.py` | `SistemaEscolar` (registrar, asignar, listar, guardar, cargar) y `Validador` |
| `almacen.py` | `Almacenamiento`: pasar el sistema a un archivo de texto y de vuelta |
| `main.py` | El menú de consola |
| `pruebas.py` | Las pruebas automáticas |
| `seguridad.py` |Contraseñas con salt y hash (todavía no se usa en el sistema) |

## Jerarquía

- `Alumno` y `Docente` **son una** `Persona` (herencia).
- `Materia` **tiene** una lista de `Alumno` inscritos, limitada por su cupo.
- `SistemaEscolar` **tiene** un `Validador` y un `Almacenamiento`.
- `formato()` y `campos()` se redefinen en cada clase (polimorfismo): `listar()` y
  `guardar()` solo llaman al método y cada objeto responde a su manera.
