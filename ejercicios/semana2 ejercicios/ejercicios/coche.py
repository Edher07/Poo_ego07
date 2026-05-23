class Coche:
    def __init__(self, marca, modelo, color, no_puertas,
                 capacidad, combustible, transmision,
                 peso, tamano, material):

        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.no_puertas = no_puertas
        self.capacidad = capacidad
        self.combustible = combustible
        self.transmision = transmision
        self.peso = peso
        self.tamano = tamano
        self.material = material

        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Color: {self.color}")
        print(f"No. puertas: {self.no_puertas}")
        print(f"Capacidad: {self.capacidad}")
        print(f"Combustible: {self.combustible}")
        print(f"Transmisión: {self.transmision}")
        print(f"Peso: {self.peso}")
        print(f"Tamaño: {self.tamano}")
        print(f"Material: {self.material}")

        print("Toyota","Corolla","Azul metalico","4 puertas","5 personas",
              "Hibrido","Automatico","1,350 kg","4,37 mts","Acero")

class Coche:

    def __init__(self):
        print ("constructor")
    def arrancar (self):
        print ("Método Uno")
    def frenar (self,parametro_uno):
        print  (f" Método Dos: {parametro_uno}")
    def acelerar (self,parametro.uno):
        print  (f" Método Tres:{parametro_uno}")
    def combustible (self,parametro.uno):
        print (f" Método Cuatro:{parametro_uno}")
    def marcha (self,parametro.uno):
        print (f" Método Cinco: {parametro_uno}")

nombre_objeto = Coche()
nombre_objeto.arrancar()
nombre_objeto.frenar("Freno de mano")
nombre_objeto.acelerar("En primera")
nombre_objeto.combustible ("Híbrido")
nombre_objeto.marcha ("Drive")