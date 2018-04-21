import FormaPago
import MenuOpciones

if __name__ == '__main__':
    FormaPago.menuPagos()
    opc = input("Dijite el numero de la opción que desea acceder: ")
    if opc == "1":
        MenuOpciones.OpcionCrear()
    elif opc == "2":
        MenuOpciones.OpcionCambiar()
    
