def OpcionCrear():
    import os.path
    h = False
    while h == False:
        com = os.path.isfile("pagos.txt")
        if com == False:
            with open("pagos.txt", "w") as file:
                file.close()
                h = True
        elif os.stat("pagos.txt").st_size == 0:
            h = True 

        with open ("pagos.txt") as file:
            id = input ("Ingrese el ID de la forma de pago: ")
            for linea in file.readlines():
                lista = linea. strip().split(", ")
                if id in lista[0]:
                    h = False
                else:
                    h = True

            if h == True:
                forma = input("Ingrese la forma de pago (efectivo, tarjerta o cupon): ")
                asc = input("Ascii para totalizar la transacción: ")
                archivo = open('pagos.txt', 'w')
                archivo.write(id + ", " + forma + ", " + asc + "\n")
                archivo.close()
                print("Datos agregados con exitos")
            else:
                print("Los datos ya existen")
def OpcionCambiar():
    import os.path
    com = os.path.isfile("pagos.txt")
    if com == False:
        print ("Ingrese los datos")
    else:
        with open("pagos.txt") as file:
            datos = ''
            iidd = input("Ingrese el ID de la transacciónn a cambiar: ")
            for linea in file:
                id = linea[0]
                if id in iidd:
                    forma = ("Ingrese la nueva forma de pago (efectivo, tarjerta o cupon): ")
                    asc = input("Ascii para totalizar la transacción: ")
                    cambio = (id + ", " + forma + ", " + asc + "\n")
                    linea = cambio
                datos += linea
            file.cloase()
        with open("pagos.txt", "w") as file: 
            file.write(datos)
            file.close()