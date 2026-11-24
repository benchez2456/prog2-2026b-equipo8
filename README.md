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

## Contrato de `SistemaEscolar`

| Método | Qué hace |
|---|---|
| `registrar(objeto)` | Da de alta un `Alumno`, `Docente` o `Materia`; valida antes de aceptar |
| `asignar(identificador, clave)` | Inscribe al alumno con ese código en la materia con esa clave |
| `listar()` | Imprime todo, cada tipo con su propio formato |
| `guardar(ruta)` | Escribe la información en un archivo (usa `Almacenamiento.guardar(sistema, ruta)`) |
| `cargar(ruta)` | La recupera del archivo (usa `Almacenamiento.cargar(sistema, ruta)`) |

Validaciones: código de 9 dígitos, nombre y demás datos no vacíos (y sin `|`), códigos
no repetidos, claves de materia no repetidas, cupo entero mayor que 0 y no pasarse del cupo.

## Responsabilidades

| Clase | Se encarga de |
|---|---|
| `Persona` | Guardar el código y el nombre que comparten alumnos y docentes |
| `Alumno` | Representar a una persona que estudia una carrera |
| `Docente` | Representar a una persona que pertenece a una Materia |
| `Materia` | Guardar a sus alumnos inscritos sin pasarse del cupo |
| `Validador` | Decir si un código, un texto o un cupo son aceptables |
| `Almacenamiento` | Convertir el sistema a líneas de texto y regresarlo del archivo |
| `SistemaEscolar` | Coordinar el registro, la inscripción y el listado de todo lo anterior |

## Activación
Solo se ejecutan `main.py` y `pruebas.py`; los demás archivos se importan solos.

## Integrantes

- `Sanchez Castañon Benjamin Amadeo`
- `Carrillo Jacome Edwin Gabriel`