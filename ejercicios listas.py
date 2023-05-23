#atomicas(solo tienen 1 valor)
a = 10
texto = "Hola"
es_feriado = False

#estructuradas, compuestas (tengo más de 1 valor)
dias_semana = ["lunes", "martes", "miercoles", "jueves", "viernes"] #homogenea
print(dias_semana[-1])
#print(dias_semana[5])------>  error: off-by-one
print(dias_semana[2])

datos_participante = ["juan", 25000, True, 225.4, (60, 140, 100, 600), "rojo"] #heterogenea

NOMBRE = 0
PUNTOS = 1
ES_PREMIUM = 2
VEL_MAX = 3
SEGUNDOS_POR_NIVEL = 4
COLOR_TRAJE = 5

NIVEL_AIRE = 1
NIVEL_TIERRA = 2
NIVEL_AGUA = 3
NIVEL_FUEGO = 4

#print(f"Bienvenido, {datos_participante[NOMBRE]}!")
#print(f"Tenes {datos_participante[PUNTOS]} puntos")

#Puedo usar desempaquetado de esta forma:
#nombre, puntos, es_premium, vel_max = datos_participante

print(datos_participante[SEGUNDOS_POR_NIVEL][NIVEL_AGUA])
