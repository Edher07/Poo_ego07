class NombreClase:
    def __init__(self):
        print("constructor")
    def metodoUno(self):
        print("Método uno")
    def metodoDos(self,parametro.uno):
        print(f"Método Dos:{self.parametro.uno}")

nombre_objeto=NombreClase()
nombre_objeto.metodoUno()
nombre_objeto.metodoDos("Hola")
