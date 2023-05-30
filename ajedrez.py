FILAS = 8
COLUMNAS = 8
CASILLERO_VACIO = "_"
REINA_BLANCA = "R"


tablero = [[[CASILLERO_VACIO] * COLUMNAS] * FILAS]


for f in range(FILAS):
    for c in range(COLUMNAS):
        print(tablero[f][c])
    print("")
print(tablero)

for f in range(FILAS):
    for c in range(COLUMNAS):
        print(f"{tablero[f][c]} ", end= "")
    print()
    

        