class Banco:
    def __init__(self,no_clientes,no_elementos_seguridad,
               no_edificios,sistema_informatico,
               nombre_banco,no_cajeros,fiable,capital,
               horario_atencion,color_banco): 
   
        self.no_clientes = no_clientes
        self.no_elementos_seguridad = no_elementos_seguridad
        self.no_edificios = no_edificios
        self.sistema_informatico = sistema_informatico
        self.nombre_banco = nombre_banco
        self.no_cajeros = no_cajeros
        self.fiable = fiable
        self.capital = capital
        self.horario_atencion = horario_atencion
        self.color_banco = color_banco
        
    def mostrar_info(self):
        print(f" Número de clientes {self.no_clientes}")
        print(f" Número de elementos de seguridad {self.no_elementos_seguridad}")
        print(f" Número de edificios {self.no_edificios}")
        print(f" Sistema informatico {self.sistema_informatico}")
        print(f" Nombre del banco {self.nombre_banco}")
        print(f" Fiable {self.fiable}")
        print(f" Capital {self.capital}")
        print(f" Horario de atención {self.horario_atencion}")
        print(f" Color del banco {self.color_banco}")

banco1 = Banco(
    no_clientes=5000,
    no_elementos_seguridad=20,
    no_edificios=10,
    sistema_informatico="BancaNet",
    nombre_banco="CitiBanamex",
    no_cajeros=50,
    fiable=True,
    capital=15000000,
    horario_atencion="9:00-16:00",
    color_banco="Azul y Rojo"
)

banco1.mostrar_info()
