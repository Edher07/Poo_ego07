class Alumno:
    def __init__(self,nombre, apellido, edad, matricula, carrera,
                 cuatrimestre, promedio, turno, correo, telefono):
        
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.matricula = matricula
        self.carrera = carrera
        self.cuatrimestre = cuatrimestre
        self.promedio = promedio
        self.turno = turno
        self.correo = correo
        self.telefono = telefono

        print(f"Nombre del alumno:{self.nombre}")
        print(f"Apellidos del alumno:{self.apellido}")
        print(f"Edad actual:{self.edad}")
        print(f"Número de matrícula :{self.matricula}")
        print(f"Carrera en curso:{self.carrera}")
        print(f"Cuatrimestre actual:{self.semestre}")
        print(f"Promedio general:{self.promedio}")
        print(f"Turno asignado:{self.turno}")
        print(f"Correo electronico:{self.correo}")
        print(f"Número telefonico:{self.telefono}")

        print("Edher","González Osorio","24","1725110071","Tecnologías de la Información",
               "Tercero","9.2","Matutino","1725110071@utectulancingo.edu.mx","7712137975")

    def __init__(self):
        print("constructor")
    def estudiar(self):
        print("Método Uno")
    def hacerTarea(self, parametro_uno):
        print(f"Método Dos:{parametro_uno}")
    def presentarExamen(self, parametro_uno):
        print(f"Método Tres:{parametro_uno}")
    def asistirClases(self, parametro_uno):
        print(f"Método Cuatro:{parametro_uno}")
    def verCalificaciones(self, parametro_uno):
        print(f"Método Cinco:{parametro_uno}")



nombre_objeto=Alumno()
nombre_objeto.estudiar()
nombre_objeto.hacerTarea("Integradora")
nombre_objeto.presentarExamen("No")
nombre_objeto.asistirClases("Tutoria")
nombre_objeto.verCalificaciones("En el SII")
