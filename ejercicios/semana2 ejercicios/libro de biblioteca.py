class LibroBiblioteca:
    
    def __init__(self, titulo, autor, genero, editorial, anio,
                 paginas, idioma, disponible,distribuidor, ubicacion):
        self.titulo=titulo
        self.autor=autor
        self.genero=genero
        self.editorial=editorial
        self.anio=anio
        self.paginas=paginas
        self.idioma=idioma
        self.disponible=disponible
        self.distribuidor=distribuidor
        self.ubicacion=ubicacion

        print(f"Título:{self.titulo}")
        print(f"Autor:{self.autor}")
        print(f"Género:{self.genero}")
        print(f"Editorial:{self.editorial}")
        print(f"Año:{self.anio}")
        print(f"Páginas:{self.paginas}")
        print(f"Idioma:{self.idioma}")
        print(f"Disponible:{self.disponible}")
        print(f"Distribuidor:{self.distribuidor}")
        print(f"Ubicación:{self.ubicacion}")

        print("Avatar The Last Airbender","Gene Luen Yang","Fantasia","Dark House Books",
              "2019","75 páginas","Español","True","Editorial Kamite","Ciudad de México")
    
    def prestar(self):
        print("Método Uno")
    def devolver(self, parametro_uno):
        print(f"Método Dos:{parametro_uno}")
    def reservar(self, parametro_uno):
        print(f"Método Tres:{parametro_uno}")
    def buscarInformación(self, parametro_uno):
        print(f"Método Cuatro:{parametro_uno}")
    def renovarPrestamo(self, parametro_uno):
        print(f"Método Cinco:{parametro_uno}")

nombre_objeto=LibroBiblioteca
nombre_objeto.prestar()
nombre_objeto.devolver("15 días")
nombre_objeto.reservar("Sala de lectura")
nombre_objeto.buscarInformacion("México en el mundo")
nombre_objeto.renovarPrestamo("7 días más")


