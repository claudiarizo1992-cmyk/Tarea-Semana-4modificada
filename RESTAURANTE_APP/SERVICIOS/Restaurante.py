from  MODELOS.cliente import Cliente
from  MODELOS.producto import Producto
class Restaurante:
    def __init__(self, nombre_restaurante: str):
        self.nombre_restaurante = nombre_restaurante
#Listas para almacenar las instancias de objetos
        self.lista_productos = []
        self.lista_clientes = []
    def registrar_producto(self, producto: Producto):
        """Agrega un objeto Producto a la lista del restaurante""" 
        self.lista_productos.append(producto)
        print(f"Producto registrado con exito: {producto.nombre}")
    def registrar_cliente(self, cliente: Cliente):
        """Agrega un objeto Cliente a la lista del restaurante."""
        self.lista_clientes.append(cliente)
        print(f"Cliente registrado con exito: {cliente.nombre}")
    def mostrar_menu(self):
        """Muestra en consola todos los productos disponibles."""
        print(f"\n---MENU DE {self.nombre_restaurante.upper()} ---")
        if not self.lista_productos:
         print("No hay productos registrados en el menu.")
        for prod in self.lista_productos:
#Aqui se ejecuta automaticamente el metodo __str__() de 
                print(prod)
    def mostrar_clientes(self):
           """Muestra en consola todos los clientes registrados"""
           print("\n---CLIENTES REGISTRADOS")
           if not self.lista_clientes:
              print("No hay cliente registrados.")
           for cli in self.lista_clientes:
               #Aqui se ejecuta automaticamente el metodo __str__() de Cliente
               print(cli)