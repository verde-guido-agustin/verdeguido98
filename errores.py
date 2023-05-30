edad = None
peso = 10
while edad == None:
    try:
        edad = int(input("Ingrese su edad: "))
        inverso = 1/edad
    except ValueError:
        print("No entendi ese nro, ingresa devuelta")
    except(ZeroDivisionError, NameError):
        print("Algo salió mal ...")
    else:
        print("Salio todo bien, ninguna excepcion")
    finally:
        print("Se ejecuta siempre, haya habido o no excepción")
        print("Limpieza ...")
print(edad)
    
    
