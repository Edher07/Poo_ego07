class Alumno:
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

        print(f"Nombre:{self.nombre}")
        print(f"Apellido:{self.apellido}")
        print(f"Edad:{self.edad}")
        print(f"Matrícula:{self.matricula}")
        print(f"Carrera:{self.carrera}")
        print(f"Semestre:{self.semestre}")
        print(f"Promedio:{self.promedio}")
        print(f"Turno:{self.turno}")
        print(f"Correo:{self.correo}")
        print(f"Teléfono:{self.telefono}")

    def presentarse(self):
        print("Método Uno")
    def mostrarPromedio(self, parametro_uno):
        print(f"Método Dos:{parametro_uno}")
    def inscribirMateria(self, parametro_uno):
        print(f"Método Tres:{parametro_uno}")
    def entregarTarea(self, parametro_uno):
        print(f"Método Cuatro:{parametro_uno}")
    def solicitarBeca(self, parametro_uno):
        print(f"Método Cinco:{parametro_uno}")


nombre_objeto = Alumno("Carlos","López",20,"A12345","Ingeniería",
                        3,9.2,"Matutino","carlos@mail.com","5512345678")

nombre_objeto.presentarse()
nombre_objeto.mostrarPromedio("9.2")
nombre_objeto.inscribirMateria("Matemáticas")
nombre_objeto.entregarTarea("Tarea de POO")
nombre_objeto.solicitarBeca("Promedio mayor a 9")