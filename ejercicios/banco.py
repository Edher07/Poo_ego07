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

class Banco = Banco(5000,20,10,BancaNet,Citibanamex,8,True,1500000,9:00-16:00,Azul y rojo)

class Banco ():
    def __init__(self):
        print("constructor")
    def retirar(self):
        print("Método uno")
    def prestamo (self.parametro_uno):
        print("Método dos: {parametro_uno}")
    def saldo (self.parametro_uno):
        print("Método tres: {parametro_uno}")
    def afore (self.parametro_uno):
        print("Método cuatro: {parametro_uno}")
    def deuda (self.parametro_uno):
        print("Método cinco: {parametro_uno}")

nombre_objeto= Banco()
nombre_objeto.retirar("3000")
nombre_objeto.prestamo("15000")
nombre_objeto.saldo("5000")
nombre_objeto.afore("2000")
nombre_objeto.deuda("0")




