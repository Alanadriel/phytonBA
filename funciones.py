import os
def MenuOptions():
    print("\n\n------------------    MENU DE GESTION DE PRODUCTOS--------------    \n")
    print("\n 1. REGISTRO: AGREGAR NUEVO PRODUCTO")
    #print("\n 2. Visualización: Consulta de datos de productos")
    #print("\n 3. Actualización: Modificar la cantidad en stock de los productos")
    #print("\n 4. Eliminacion: Dar de baja los productos ")
    print("\n 2. LISTADO: MOSTRAR TODOS LOS PRODUCTOS")
    #print("\n 6. Reporte de Bajo Stock")
    print("\n 3. SALIR ")
    while True:
        try:
            nOption = int( input("\nPor favor, selecciona una opción (1-3): "))
            if 3>=nOption>=1 :
                break
            else:
                print("Entrada inválida. Por favor, ingrese un número válido.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")
    return nOption 

def fagregarProds(mi_lista):
    Agregando = True
    while Agregando:
        nProduct = input("Ingrese el nombre del producto: ")
        while True:
            try:
                precioProd = float(input("Ingrese el precio del producto:") )
                if type(precioProd)== float and precioProd > 0 :
                    break
            except ValueError:
                print("\nIngrese un precio de producto correcto\n")
        while True:
            try:
                cantProduct = int(input("ingrese la cantidad del producto: "))
                if type(cantProduct)== int and cantProduct > 0:
                    break
            except ValueError:
                print("\nIngrese una Cantidad Valida\n")
        s_n = input("\n¿Desea Agregar mas productos ? (s/n): ")
        if s_n == 'n':
            Agregando = False



    

    mi_lista.append({"Producto":nProduct,"Precio":precioProd, "Cantidad":cantProduct})
    
def fmostrarProductos(mi_lista):
    print("\n--------------Lista de Productos---------------- \n")
    print("%-16s|%-13s|%-14s\n"%("PRODUCTOS","PRECIOS","CANTIDAD" ) )

    for producto in mi_lista:
       print("%-15s | $%10.2f | %6d" %(producto["Producto"],producto["Precio"],producto["Cantidad"] ) )