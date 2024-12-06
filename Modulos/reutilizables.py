def validar_numeroRango(mensaje, minimo=None, maximo=None):
    while True:
        try:
            numero = int(input(mensaje))
            if (numero < minimo) or (numero > maximo):
                print(f"Por favor, ingrese un número entre {minimo} y {maximo}.")
            else:
                return numero
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")

def validar_numeroMAYORQ(mensaje , mayor):
    while True:
        try:
            numero = int(input(mensaje))
            if (numero < mayor):
                print(f"Por favor, ingrese un número mayor que {mayor}.")
            else:
                return numero
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")

def validar_numeroFloat(mensaje , mayor):
    while True:
        try:
            numero = float(input(mensaje))
            if (numero < mayor):
                print(f"Por favor, ingrese un número mayor que {mayor}.")
            else:
                return numero
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")

def validar_TextoVacio(mensaje,parametro):
    while True:
        try:
            text = input(mensaje)
            if (text==""):
                print(f"Por favor, ingrese un '{parametro}' valido.")
            else:
                return text
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")



def actuliarCampos_BD():
    #FUNCION PARA EFECTUAR LA ACTUALIZACON DEL PRODUCTO 
    print("---------------CAMPOS QUE DESEA ACTUALIZAR------------------\n ")
    print("1. NOMBRE PRODUCTO   \n")
    print("2. PRECIO  \n")
    print("3. CANTIDAD  \n")
    print("4. CATEGORIA  \n")
    print("5. SALIR \n")
    #SE ELIGEN LOS CAMPOS QUE DESEA EFECTUAR LOS CAMBIOS 
