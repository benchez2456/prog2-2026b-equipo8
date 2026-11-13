import hashlib
import hmac
import os

class Seguridad:
    interaciones = 200_000

    def generar_salt(self):
        return os.urandom(16).hex()

    def calcular_hash(self, password, salt):
        return hashlib.pbkdf2_hmac("sha256", password.encode("utf=8"), bytes.fromhex(salt), self.interaciones).hex()

    def crear_credencial(self, password):
        salt = self.generar_salt()
        return salt, self.calcular_hash(password, salt)

    def verificar(self, password, salt, hash_guardado):
        return hmac.compare_digest(self.calcular_hash(password, salt), hash_guardado)