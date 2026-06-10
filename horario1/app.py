from tabulate import tabulate

# Definición de las columnas (Días de la semana)
headers = ["HORARIO", "LUNES", "MARTES", "MIERCOLES", "JUEVES", "VIERNES", "SABADO"]

# Datos estructurados por filas (Materia \n Profesor)
data = [
    [
        "07:00 - 09:00",
        "CÁLCULO INTEGRAL\n(Oscar R. Salas)",
        "DESARROLLO PENSAMIENTO\n(María del Carmen)",
        "CÁLCULO INTEGRAL\n(Oscar R. Salas)",
        "PROG. ORIENTADA OBJETOS\n(Salvador Hernández)",
        "TÓPICOS DE CALIDAD\n(Rigoberto García)",
        ""
    ],
    [
        "09:00 - 10:00",
        "TÓPICOS DE CALIDAD\n(Rigoberto García)",
        "PROG. ORIENTADA OBJETOS\n(Salvador Hernández)",
        "BASES DE DATOS\n(Oscar Lira)",
        "INGLÉS III\n(Jetsabel Arianna)",
        "BASES DE DATOS\n(Oscar Lira)",
        ""
    ],
    [
        "10:00 - 11:00",
        "TÓPICOS DE CALIDAD\n(Rigoberto García)",
        "PROG. ORIENTADA OBJETOS\n(Salvador Hernández)",
        "BASES DE DATOS\n(Oscar Lira)",
        "PROYECTO INTEGRADOR I\n(Elizabeth García)",
        "BASES DE DATOS\n(Oscar Lira)",
        ""
    ],
    [
        "11:00 - 12:00",
        "INGLÉS III\n(Jetsabel Arianna)",
        "TUTORÍA\n(Oscar Lira)",
        "INGLÉS III\n(Jetsabel Arianna)",
        "PROYECTO INTEGRADOR I\n(Elizabeth García)",
        "PROG. ORIENTADA OBJETOS\n(Salvador Hernández)",
        ""
    ],
    [
        "12:00 - 13:00",
        "INGLÉS III\n(Jetsabel Arianna)",
        "PROYECTO INTEGRADOR I\n(Elizabeth García)",
        "INGLÉS III\n(Jetsabel Arianna)",
        "DESARROLLO PENSAMIENTO\n(María del Carmen)",
        "PROG. ORIENTADA OBJETOS\n(Salvador Hernández)",
        ""
    ],
    [
        "13:00 - 14:00",
        "BASES DE DATOS\n(Oscar Lira)",
        "PROYECTO INTEGRADOR I\n(Elizabeth García)",
        "TÓPICOS DE CALIDAD\n(Rigoberto García)",
        "DESARROLLO PENSAMIENTO\n(María del Carmen)",
        "",
        ""
    ],
    [
        "14:00 - 15:00",
        "PROG. ORIENTADA OBJETOS\n(Salvador Hernández)",
        "",
        "",
        "TÓPICOS DE CALIDAD\n(Rigoberto García)",
        "",
        ""
    ]
]

# Imprimir la tabla con formato de cuadrícula (grid)
print(tabulate(data, headers=headers, tablefmt="grid"))