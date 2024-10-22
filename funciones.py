def MenuOptions():
    print("MENU DE GESTION DE PRODUCTOS")
    print("\n 1. REGISTRO: Alta de nuevo productos")
    #print("\n 2. Visualización: Consulta de datos de productos")
    #print("\n 3. Actualización: Modificar la cantidad en stock de los productos")
    #print("\n 4. Eliminacion: Dar de baja los productos ")
    print("\n 2. Listado completo de los productos")
    #print("\n 6. Reporte de Bajo Stock")
    print("\n 3. Salir ")
    nOption = int( input("\nPor favor, selecciona una opción (1-3): "))
    while (nOption <=0  or nOption > 3 ):
        print("\n Has Seleccinado un opcion invalida ")
        nOption = int( input("\nPor favor, selecciona una opción (1-3): "))
    print("\n Has seleccionado la opcion:",nOption,"\n")

    return nOption 

def fagregarProds(mi_lista):
    nProduct = str(input("Ingrese el nombre del producto: "))
    precioProd = float(input("Ingrese el precio del producto:") )
    cantProduct = int(input("ingrese la cantidad del producto: "))

    mi_lista.append([nProduct,precioProd,cantProduct])

def fmostrarProductos(mi_lista):
    for mi_lista in mi_lista:
        print( "Descripción:", mi_lista[0], "Precio:", mi_lista[1],
        "Cantidad:", mi_lista[2])