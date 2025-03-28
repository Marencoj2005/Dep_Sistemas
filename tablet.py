class Tablet():
    serial = None
    tamano = None
    marca = None
    precio = None
    nombre_usuario = None
    disponible = None
    cantidad = None

    def __init__(self):
        pass
    
    def set_serial(self, serial):
        self.serial = serial
    def set_marca(self, marca):
        self.marca = marca
    def set_precio(self, precio):
        self.precio = precio
    def set_nombre_usuario(self, nombre_usuario):
        self.nombre_usuario = nombre_usuario
    def set_disponible(self, disponible):
        self.disponible =disponible
    def set_tamano(self, tamano):
        self.tamano =tamano
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    ## getters
    def get_serial(self):
        return self.serial
    def get_marca(self):
        return self.marca
    def get_precio(self):
        return self.precio
    def get_nombre_usuario(self):
        return self.nombre_usuario
    def get_disponible(self):
        return self.disponible
    def get_tamano(self):
        return self.tamano
    