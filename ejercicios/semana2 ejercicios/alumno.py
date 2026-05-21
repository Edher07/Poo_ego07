class Alumno():
    def __init__(self.nombre, apellido, edad, matricula, carrera, 
                 semestre, promedio, turno, correo, telefono):

    
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.matricula = matricula
        self.carrera = carrera
        self.semestre = semestre
        self.promedio = promedio
        self.turno = turno          
        self.correo = correo
        self.telefono = telefono
        

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

class Alumno():
    def __init__(self, nombre, apellido, edad, matricula, carrera, 
                 semestre, promedio, turno, correo, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.matricula = matricula
        self.carrera = carrera
        self.semestre = semestre
        self.promedio = promedio
        self.turno = turno          
        self.correo = correo
        self.telefono = telefono

    def presentarse(self):
        print(f"Hola, soy {self.nombre} {self.apellido}, matrícula {self.matricula}")

    def mostrarPromedio(self):
        print(f"Mi promedio actual es: {self.promedio}")

    def inscribirMateria(self, materia):
        print(f"{self.nombre} se inscribió en: {materia}")

    def entregarTarea(self, tarea):
        print(f"{self.nombre} entregó la tarea: {tarea}")

    def solicitarBeca(self):
        if self.promedio >= 9.0:
            print(f"{self.nombre} puede solicitar beca ")
        :
            print(f"{self.nombre} no cumple el promedio para beca ")


# --- Crear objeto ---
alumno1 = Alumno("Carlos", "López", 20, "A12345", "Ingeniería",
                  3, 9.2, "matutino", "carlos@mail.com", "5512345678")

alumno1.presentarse()
alumno1.mostrarPromedio()
alumno1.inscribirMateria("Matemáticas")
alumno1.entregarTarea("Ejercicios de POO")
alumno1.solicitarBeca()