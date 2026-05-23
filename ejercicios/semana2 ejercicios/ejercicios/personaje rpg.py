class MarioBros:
     
    def __init__(self,nombre,vidas,monedas,nivel,puntos,
                 velocidad,salto,poder,energia,color):

        self.nombre=nombre
        self.vidas=vidas
        self.monedas=monedas
        self.nivel=nivel
        self.puntos=puntos
        self.velocidad=velocidad
        self.salto=salto
        self.poder=poder
        self.energia=energia
        self.color=color

        print(f"Nombre:{self.nombre}")
        print(f"Vidas:{self.vidas}")
        print(f"Monedas:{self.monedas}")
        print(f"Nivel:{self.nivel}")
        print(f"Puntos:{self.puntos}")
        print(f"Velocidad:{self.velocidad}")
        print(f"Salto:{self.salto}")
        print(f"Poder:{self.poder}")
        print(f"Energia:{self.energia}")
        print(f"Color:{self.color}")

        print("Mario","8 vidas","500","9-5","30","Rápido",
         "Medio","Volar","6","Azul y Rojo")


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
