from Modulos import reutilizables as rutil
from BaseDatos import controladorDB as CBD

#FUNCIONES PARA GESTION DEL INVENTARIO  

def MENU_DE_OPCIONES():
    #FUNCION PARA MOSTRAR EL MENU DE OPCIONES
    print("<----------MENU DE OPCIONES -------->")
    print(" 1. AGREGAR NUEVO PRODUCTO")
    print("2. MOSTRAR LISTADO DE PRODUCTOS")                           
    print("3. ACTUALIZAR PRODUCTO")                            
    print("4. ELIMINAR PRODUCTO ")                           
    print("5. BUSCAR PRODUCTO ")                             
    print("6. REPORTE BAJO STOCK ")                               
    print("7. SALIR ") 
    #VALIDAMOS LAS OPCIONES (1,7)
    opcion =   rutil.validar_numeroRango("Ingrese la opcion:",1,7)
    return opcion                   


def MOSTRAR_PRODUCTOS():
    #FUNCION PARA MOSTRAR TODOS LOS PRODUCTOS DE LA BASE DE DATOS
    
    lista = CBD.leer_DB() #FUNCION PARA CONSULTAR LA BASE DE DATOS, RETORNA TODOS LOS ELEMENTOS
    #PRINTEAR TODOS LOS ELEMENTOS 
    for prods in lista:
        print(f"ID: {prods[0]} PRODUCTO:{prods[1]} \n")


def agregar_Producto():
    #FUNCION PARA AGREGAR UN NUEVO PRODUCTO A LA BASE DE DATOS
    agregando = True
    while agregando:
        #VALIDACION DE ENTRADAS ANTES DE INSERTAR EN LA BASE DE DATOS
        name = rutil.validar_TextoVacio("POR FAVOR INGRESE EL NOMBRE DEL PRODUCTO:","NOMBRE")
        descr= rutil.validar_TextoVacio(f"POR FAVOR INGRESE LA DESCRIPCION DEL PRODUCTO:{name} :","DESCRIPCION")
        cant = rutil.validar_numeroMAYORQ(f"POR FAVOR INGRESE LA CANTIDAD DEL PRODUCTO:{name} :",0)
        precio = rutil.validar_numeroFloat(f"POR FAVOR INGRESE EL PRECIO DEL PRODUCTO:{name} :",0)
        cat = rutil.validar_TextoVacio(f"POR FAVOR INGRESE LA CATEGORIA DEL PRODUCTO{name} :","NOMBRE")

        # FUNCION PARA INSERTAR EN LA BASE DE DATOS
        CBD.insertar_FILA_DB(name,descr,cant,precio,cat)

        # OPCION DE SEGUIR AGREGANDO PRODUCTOS
        opc = rutil.validar_TextoVacio("DESEA AGREGAR OTRO PRODUCTO (S/N):","OPCION")
        if(opc == 'N' or opc == 'n'):
            agregando = False

def buscar_producto():
    #FUNCION PARA BUSCAR UN PRODCUTO POR ID
    buscando = True
    while buscando:
        #VALIDACION DE ID > 0
        opID = rutil.validar_numeroMAYORQ("POR FAVOR INGRESE EL ID DEL PRODUCTO :",0)
        # FUNCION PARA CONSULTAR EN LA BD POR ID
        prod = CBD.consultar_DB_ID(opID)
        #SI NO SE ENCONTRO LA FUNCION RETORNA -1
        if (prod != -1):
            print(f"ID: {prod[0]} PRODUCTO:{prod[1]} \n")
        else:
            print("EL ID NO CORRESPONDE CON ALGUN PRODUCTO !!!")
        #OPCION DE SEGUIR BUSCANDO PRODUCTOS
        opc = rutil.validar_TextoVacio("DESEA BUSCAR OTRO PRODUCTO (S/N):","OPCION")
        if(opc == 'N' or opc == 'n'):
            buscando = False

def eliminar_productoID():
    elimi = True
    while elimi:
        opID = rutil.validar_numeroMAYORQ("POR FAVOR INGRESE EL ID DEL PRODUCTO :",0)
        CBD.ocultar_Producto_ID_DB(opID)
        opc = rutil.validar_TextoVacio("DESEA ELIMINAR OTRO PRODUCTO (S/N):","OPCION")
        if(opc == 'N' or opc == 'n'):
            elimi = False

def reporte_bajoStock_BD():
    bajo = True
    while bajo:
        stck = rutil.validar_numeroMAYORQ("POR FAVOR INGRESE EL STOCK MINIMO PARA GENERAR EL REPORTE :",0)
        datos = CBD.bajoStock_BD(stck)
        if datos != -1:
            for prods in datos:
                print(f"ID: {prods[0]} PRODUCTO:{prods[1]} \n")
        else:
            print(f"NO HAY PRODUCTOS CON UN STOCK MENOR QUE : {stck}")

        opc = rutil.validar_TextoVacio("DESEA GENERAR OTRO REPORTE ? (S/N):","OPCION")
        if(opc == 'N' or opc == 'n'):
            bajo = False

def actulizar_producto_ID_BD():
    actu = True
    while actu:
        try:
            OPID = rutil.validar_numeroMAYORQ("POR FAVOR INGRESE EL ID DEL PRODUCTO :",0)
            listActual = CBD.consultar_DB_ID(OPID)
            campo = rutil.MENU_ACTUALIZAR_PROD()
            if campo == 1:
                listActual[1] = rutil.validar_TextoVacio("POR FAVOR INGRESE EL NOMBRE DEL PRODUCTO:","NOMBRE")
            elif campo==2:
                listActual[2] =rutil.validar_TextoVacio(f"POR FAVOR INGRESE LA DESCRIPCION DEL PRODUCTO:","DESCRIPCION")


           
        except listActual == -1:
            print("EL ID NO CORRESPONDE CON ALGUN PRODUCTO !!!")
            

#agregar_Producto()
#MOSTRAR_PRODUCTOS()
#buscar_producto()

#eliminar_productoID()
#reporte_bajoStock_BD()



