def MenuOptions():
    print("MENU DE GESTION DE PRODUCTOS")
    print("\n1. REGISTRO: Ata de nuevo productos")
    print("\n2. Visualización: Consulta de datos de productos")
    print("\n3. Actualización: Modificar la cantidad en stock de los productos")
    print("\n4. Eliminacion: Dar de baja los productos ")
    print("\n5. Listado completo de los productos")
    print("\n6. Reporte de Bajo Stock")
    print("\n7. Salir ")
    nOption = int( input("\nPor favor, selecciona una opción (1-7): "))
    while (nOption <=0  or nOption > 7 ):
        print("\n Has Seleccinado un opcion invalida ")
        nOption = int( input("\nPor favor, selecciona una opción (1-7): "))
    print("\nHas seleccionado la opcion:",nOption)

    return nOption 

def calculoIVA(precio, porcentaje):
    pFinal =float( ((precio*porcentaje) / 100)+precio )
    return pFinal

def calculoDescuento(precio2,porcentaje2):
    montDesc =float( (precio2*porcentaje2) / 100)
    p_final = float(precio2-montDesc)
    return p_final

def costoTotalCompra(precio,cantProd):
    return float( precio * cantProd  )