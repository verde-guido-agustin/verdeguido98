FILAS = 8
COLUMNAS = 8

CHAU="9"

CASILLERO_VACIO = "_"
REINA_BLANCA = "R"

"""
tablero = [[[CASILLERO_VACIO] * COLUMNAS] * FILAS]


for f in range(FILAS):
    for c in range(COLUMNAS):
        print(tablero[f][c])
    print("")
print(tablero)
"""
"""
#Otra forma de Python de generar listas:
tablero = [[CASILLERO_VACIO for i in range(FILAS)] for j in range(COLUMNAS)]
print(tablero)
"""

tablero = [[CASILLERO_VACIO for i in range(FILAS)] for j in range(COLUMNAS)]

tablero[2][5] = REINA_BLANCA

for f in range(FILAS):
    for c in range(COLUMNAS):
        print(f"{tablero[f][c]} ", end= "")
    print()
    

        