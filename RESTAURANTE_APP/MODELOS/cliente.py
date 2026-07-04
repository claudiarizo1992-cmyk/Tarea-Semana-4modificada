class Cliente:
    def __init__(self, cedula: str, name:str):
        # Atributos del cliente
        self.cedula = cedula
        self.nombre = name
        
    def __str__(self):
        #Retorna una representacion en texto del cliente 
        return f"Cliente: {self.nombre} (C.I.: {self.cedula})"
    
    