import os

class Almacenamiento:

    def __init__(self, archivo="usuarios.txt"):
        self.archivo = archivo

    def cargar(self):
        usuarios = {}
        if os.path.exists(self.archivo):
            with open(self.archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    registro = self.parsear(linea)
                    if registro:
                        usuario, datos = registro
                        usuarios[usuario] = datos
        return usuarios

    def guardar(self, usuarios):
        with open(self.archivo, "w", encoding="utf-8") as f:
            for usuario, d in usuarios.items():
                f.write (self.formatear(usuario, d))

    def parsear(self, linea):
        datos = linea.strip().split("|")
        if len(datos) != 4:
            return None
        usuario, codigo, salt, hash_ = datos
        return usuario, {"codigo": codigo, "salt": salt, "hash": hash_}
    
    def formatear(self, usuario, d):
        return f"{usuario}|{d['codigo']}|{d['salt']}|{d['hash']}\n"