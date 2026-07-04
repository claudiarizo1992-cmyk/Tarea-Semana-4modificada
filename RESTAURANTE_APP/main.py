from SERVICIOS.Restaurante import Restaurante
from MODELOS.producto import Producto
from MODELOS.cliente import Cliente
def ejecutar_sistema():
    print("===INICIANDO SISTEMA DE GESTION DE RESTAURANTE ===\n")
    #1. Instanciar el servicio principal
    mi_restaurante = Restaurante("La Sazon Amazonica")
    # 2.Crear objetos de la clase Producto
    print("--- Registrando Productos ""---")
    platillo1 = Producto(1, "El Maito",8.50)
    platillo2 = Producto(2,"Ayampaco", 6.00)
    bebida1 = Producto(3, "Chicha de Chonta", 1.50)
    # Agregar productos al sistema
    mi_restaurante.registrar_producto(platillo1)
    mi_restaurante.registrar_producto(platillo2)
    mi_restaurante.registrar_producto(bebida1)
    # 3. Crear objetos de la clase Cliente
    print("\n--- Registrando Clientes ---")
    Cliente1 = Cliente("0941035859", "claudia rizo")
    Cliente2 = Cliente("0924438138", "kleber rivas")
    # Agregar cliente al sistema
    mi_restaurante.registrar_cliente(Cliente1)
    mi_restaurante.registrar_cliente(Cliente2)
    # 4. Mostrar la informacion organizada en la consola
    mi_restaurante.mostrar_menu()
    mi_restaurante.mostrar_clientes()
    print("\n=== PROCESO FINALIZADO CON EXITO ===")
if __name__ == "__main__":
            # Garantizada que el codigo solo se ejecute si este archivo es corrido directamente
     ejecutar_sistema()