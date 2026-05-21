class MarioBros:

    def __init__(self):
        print ("constructor")
    def saltar (self):
        print ("Método Uno")
    def lanzarFuego (self, parametro_uno):
        print(f"Método Dos:{parametro_uno}")
    def recogerMoneda (self, parametro_uno):
        print(f"Método Tres:{parametro_uno}")
    def perderVidas (self,parametro_uno):
        print(f"Método Cuatro:{parametro_uno}")
    def cambiarNivel (self,parametro_uno):
        print(f"Método Cinco:{parametro_uno}")

nombre_objeto= MarioBros ()
nombre_objeto.saltar ()
nombre_objeto.lanzarFuego("Bola de fuego")
nombre_objeto.recogerMoneda("50 monedas")
nombre_objeto.perderVidas ("Vidas restantes: 3")
nombre_objeto.cambiarNivel ("Mundo 2-1")
