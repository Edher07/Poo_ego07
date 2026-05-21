class Libro:
    def __init__(self, titulo, autor, genero, editorial, anio,
                 paginas, idioma, disponible, isbn, ubicacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.editorial = editorial
        self.anio = anio
        self.paginas = paginas
        self.idioma = idioma
        self.disponible = disponible
        self.isbn = isbn
        self.ubicacion = ubicacion

        print(f"Título:{self.titulo}")
        print(f"Autor:{self.autor}")
        print(f"Género:{self.genero}")
        print(f"Editorial:{self.editorial}")
        print(f"Año:{self.anio}")
        print(f"Páginas:{self.paginas}")
        print(f"Idioma:{self.idioma}")
        print(f"Disponible:{self.disponible}")
        print(f"ISBN:{self.isbn}")
        print(f"Ubicación:{self.ubicacion}")

    def prestar(self):
        print("Método Uno")
    def devolver(self, parametro_uno):
        print(f"Método Dos:{parametro_uno}")
    def reservar(self, parametro_uno):
        print(f"Método Tres:{parametro_uno}")
    def buscarInfo(self, parametro_uno):
        print(f"Método Cuatro:{parametro_uno}")
    def renovarPrestamo(self, parametro_uno):
        print(f"Método Cinco:{parametro_uno}")


nombre_objeto = Libro("Cien años de soledad","Gabriel García Márquez",
                       "Novela","Diana",1967,471,"Español",
                       True,"978-0307474728","Estante A3")

nombre_objeto.prestar()
nombre_objeto.devolver("15 días")
nombre_objeto.reservar("Sala de lectura")
nombre_objeto.buscarInfo("Realismo mágico")
nombre_objeto.renovarPrestamo("7 días más")