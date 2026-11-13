class Validador:
    longitud_codigo = 9
    longitud_min_password = 8
    separador = "|"

    def validar_codigo(self, codigo):
        return codigo.isdigit() and len(codigo) == self.longitud_codigo

    def validar_usuario(self, usuario):
        return bool(usuario) and self.separador not in usuario

    def validar_password(self, password):
        return len(password) >= self.longitud_min_password