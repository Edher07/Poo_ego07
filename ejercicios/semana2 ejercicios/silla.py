class Silla:
    def __init__ (self.material,ergonomia,portabilidad,no_partes,
                  color,altura,reclinable,tamano,peso,diseno,t
        self.material=material
        self.ergonomia=ergonomia
        self.portabilidad=portabilidad 
        self.no_partes=no_partes  
        self.color=color     
        self.altura=altura
        self.reclinable=reclinable
        self.tamano=tamano
        self.peso=peso
        self.diseno=diseno
        

        print(f"Tipo de material:{self.material}")
        print(f"Es ergonomico:{self.ergonomia}")
        print(f"Es portable:{self.portabilidad}")
        print(f"Número de partes:{self.no_partes}")
        print(f"Color de la silla:{self.color}")
        print(f"Altura total:{self.altura}")
        print(f"Es reclinable:{self.reclinable}")
        print(f"Tamaño total:{self.tamano}")
        print(f"Peso total:{self.peso}")
        print(f"Tipo de diseño:{self.diseno}")

class Silla = Silla (Acolchonado,True,True,5,Negro mate,75 cm , True,5 kg,Moderno gamer)
                   

    def __init__ (self):
        print ("constructor")

    def limpieza(self):
        print ("Método Uno")
    def movilidad(self.parametro.uno):
        print ("Método Dos:{parametro.uno}")
    def plegable (self.parametro.uno):
        print ("Método Tres:{parametro.uno}")
    def descanso (self.parametro.uno):
        print ("Método Cuatro:{parametro.uno}")
    def adaptibilidad (self.parametro.uno):
        print ("Método Cinco:{parametro.uno}")

nombre_objeto= Silla()
nombre_objeto.limpieza()
nombre_objeto.movilidad ("Fácil de mover")
nombre_objeto.plegable("False")
nombre_objeto.descanso ("Permite ser comodo")
nombre_objeto.adaptabilidad ("True")