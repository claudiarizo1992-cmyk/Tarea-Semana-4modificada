class Producto:
    def __init__(self, id_producto:int, nombre:str,precio: float):
# Atributos del producto
        self.id_producto = id_producto
        self.nombre =nombre
        self.precio = precio

    def __str__(self):
            #Retorna una representacion en texto del producto
            return f"[{self.id_producto}] {self.nombre} - ${ self .precio:.2f}"

