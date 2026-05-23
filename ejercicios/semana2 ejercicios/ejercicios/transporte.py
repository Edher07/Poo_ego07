class Transporte ():
    def __init__(self,no_asientos,no_puertas,velocidad,no_llantas,material,
                 peso,marca,modelo,precio,tamano): 
   
        self.no_asientos= no_asientos
        self.no_puertas = no_puertas
        self.velocidad = velocidad
        self.no_llantas = no_llantas
        self.material = material
        self.peso = peso
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.tamano = tamano
        
        print(f" Número de asientos: {self.no_asientos}")
        print(f" Número de puertas: {self.no_puertas}")
        print(f" Velocidad: {self.velocidad}")
        print(f" Número de llantas: {self.no_llantas}")
        print(f" Material: {self.material}")
        print(f" Peso:{self.peso}")
        print(f" Marca:{self.marca}")
        print(f" Modelo: {self.modelo}")
        print(f" Precio {self.precio}")
        print(f" Tamaño {self.tamano}")

        print("50","2","80 km/h","4","Acero","5,500 kg",
               "Dina","MX2026","1500000","8 mts")

    def __init__(self):
        print ("constructor")
    def arrancar (self):
        print ("Metodo Uno")
    def frenar (self,parametro_uno):
        print (f"Método Dos:{parametro.uno}")
    def cargarCombustible (self,parametro_uno):
        print (f"Método Tres:{parametro.uno}")
    def CargarPasaje (self,parametro_uno)
        print (f"Método Cuatro:{parametro.uno}")
    def definirDestino(self,parametro_uno):
        print (f"Método Cinco:{parametro.uno}")
                          
nombre_objeto = Transporte
nombre_objeto.arrancar ()
nombre_objeto.frenar("Freno de mano")
nombre_objeto.cargarCombustible ("Gasolina regular")
nombre_objeto.cargarPasaje ("25 personas")
nombre_objeto.definirDestino("CDMX a Tijuana")
