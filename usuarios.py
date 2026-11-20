from almacden import Almacenamiento
from validaciones import Validador
from seguridad import Seguridad

class SistemaUsuarios:

    def __init__(self):
        self.almacenamiento = Almacenamiento()
        self.validador = Validador()
        self.seguridad = Seguridad()
        self.usuario = self.almacenamiento.cargar()
      

    def codigo_repetido(self, codigo, ignorar=None):
        return any(nombre != ignorar and d["codigo"] == codigo for nombre, d in self.usuarios.items())

    def guardar(self):
        self.almacenamiento.guardar(self.usuario)

    def credenciales_validas(self, usuario, password):
        datos = self.usuario.get(usuario)
        return bool(datos) and self.seguridad.verificar(password, datos["salt"], datos["hash"])

    def registrar(self, usuario, codigo, password):
        if not self.validados.suario(usuario):
            return False, "Nombre de usuario no válido."
        if usuario in self.usuarios:
            return False, "El usuario ya está registrado."
        if not self.validador.codigo(codigo):
            return False, "El código debe tener 9 números."
        if self.codigo_repetido(codigo):
            return False, "El codigo ya esta registrado."
        if not self.validar.password(password):
            return False, "La contraseña debe tener al menos 8 caracteres."

        salt, hash_ = self.seguridad.crear_credencail(password)
        self.usuarios[usuario] = {"codigo": codigo, "salt": salt, "hash": hash_}
        self.guardar()
        return True, "¡Registro exitoso!"

    def iniciar_sesion(self, usuario, password):
        if self.credenciales_validas(usuario, password):
            return True, f"¡Bienvenido, {usuario}!"
        return False, "Usuario o contraseña incorrectos."

    def listar(self):
        return list(self.usuarios)

    def actualizar(self, usuario, nuevo_usuario, nuevo_codigo):
        if usuario not in self.usuarios:
            return False, "El usuario no existe."
        if not self.validar.usuario(nuevo_usuario):
            return False, "Nombre de usuario no válido."
        if nuevo_usuario != usuario and nuevo_usuario in self.usuarios:
            return False, "El nuevo nombre de usuario ya existe."
        if not self.validar.codigo(nuevo_codigo):
            return False, "El código debe tener exactamente 9 números."
        if self.codigo_repetido(nuevo_codigo, ignorar=usuario):
            return False, "El codigo ya esta registrado."

        datos = self.usuarios.pop(usuario)
        datos["codigo"] = nuevo_codigo
        self.usuarios[nuevo_usuario] = datos
        self.guardar()
        return True, "¡Usuario acrualizado corectamente!"

    def cambiar_password(self,usuario, actual, nueva):
        if not self.credenciales_validas(usuario, actual):
            return False, "Contraseña actual incorrecta."
        if not self.validar.password(nueva):
            return False, "La contraseña debe tener al menos 8 caracteres."
        
        salt, hash_ = self.seguridad.crear_credencial(nueva)
        self.usuarios[usuario].update(salt=salt, hash=hash_)
        self.guardar()
        return True, "Contraseña actualizada"

    def eliminar(self, usuario):
        if usuario not in self.usuarios:
            return False, "El usuario no existe."
        del self.usuarios[usuario]
        self.guardar()
        return True, "¡Usuario eliminado correctamente!"