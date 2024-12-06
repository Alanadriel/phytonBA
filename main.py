from Modulos import funcionesMBD as func
import os



activo = True

while activo:
    opcion =func.MENU_DE_OPCIONES()
    if opcion == 1:
        func.agregar_Producto()
        opcion =func.MENU_DE_OPCIONES()
        os.system('cls')
    elif opcion==2:
        func.MOSTRAR_PRODUCTOS()
        opcion =func.MENU_DE_OPCIONES()
        os.system('cls')
    elif opcion ==3:
        print("En este momento esta opcion no se encuentra disponible, disculpe las molestias")
        opcion =func.MENU_DE_OPCIONES()
        os.system('cls')
    elif opcion == 4:
        func.eliminar_productoID()
        opcion =func.MENU_DE_OPCIONES()
        os.system('cls')
    elif opcion == 5:
        func.buscar_producto()
        opcion =func.MENU_DE_OPCIONES()
        os.system('cls')
    elif opcion == 6:
        func.reporte_bajoStock_BD()
        opcion =func.MENU_DE_OPCIONES()
        os.system('cls')
    elif opcion == 7:
        activo = False



      
    
