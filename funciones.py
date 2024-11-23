def MenuOptions():
    print("\n\n------------------    MENU DE GESTION DE PRODUCTOS--------------    \n")
    print("%-30s\n%-30s\n%-30s\n%-30s\n%-30s\n%-30s\n%-30s"%("1. AGREGAR NUEVO PRODUCTO",
                               "2. MOSTRAR LISTADO DE PRODUCTOS",
                                "3. ACTUALIZAR PRODUCTO",
                                 "4. ELIMINAR PRODUCTO",
                                  "5. BUSCAR PRODUCTO",
                                   "6. REPORTE BAJO STOCK" ,
                                    "7. SALIR" ))
    while True:
        try:
            opcion = int( input("\nPor favor, selecciona una opción (1-7): "))
            if 1<= opcion <=7 : 
                return opcion
            else:
                print("Por favor, ingrese un número dentro del rango (1-7).") 
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")
        
     
#RegistarProductos
def fagregarProds(mi_lista):
    Agregando = True
    print("--------------GESTION NUEVOS PRODUCTOS------------\n")
    while Agregando:
        nProduct = input("Ingrese el nombre del producto: ")
        cat_prod = input("Ingrese la Categoria del producto:")
        while True:
            try:
                precioProd = float(input("Ingrese el precio del producto:") )
                if precioProd > 0 :
                    break
            except ValueError:
                print("\nIngrese un precio de producto correcto\n")
        while True:
            try:
                cantProduct = int(input("ingrese la cantidad del producto: "))
                if cantProduct > 0:
                    break
            except ValueError:
                print("\nIngrese una Cantidad Valida\n")
        ultima_clave = list(mi_lista.keys())[-1]
        nueva_clave = ultima_clave+1
        mi_lista[nueva_clave] = {"Producto":nProduct,"Precio":precioProd, "Cantidad":cantProduct,"Categoria":cat_prod,"Estado":True }
        s_n = input("\n¿Desea Agregar mas productos ? (s/n): ")
        if s_n == 'n'or s_n == 'N':
            Agregando = False

    
def fmostrarProductos(mi_lista):
    print("\n--------------Lista de Productos---------------- \n")
    print("%-6s|%-16s|%-15s|%-14s|%-14s\n"%("CODIGO","PRODUCTOS","PRECIOS","CANTIDAD","CATEGORIA") )

    for codigo, producto in mi_lista.items():
       if producto["Estado"] == True :
            print("%-6d|%-16s | $%15.2f | %14d | %14s" %(codigo,producto["Producto"],producto["Precio"],
                                            producto["Cantidad"],producto["Categoria"] ) )
            
def factualizar_Producto(diccionario):
    actu = True
    while actu:
        try:
            codProd = int(input("ingrese el Codigo  del producto: "))
            Factualizacion(diccionario[codProd])
            actu = False
        except ValueError:
                print("\nIngrese un codigo Valido\n")
        except KeyError:
            print("\n NO EXISTE UN PRODCUTO CON ESE CODIGO, POR FAVOR INGRESE UN CODIGO VALIDO")
        except type(codProd)== int and codProd > 0:
            print("\nIngrese un codigo Valido\n")

    
def Factualizacion(producto):
    print("---------------CAMPOS QUE DESEA ACTUALIZAR------------------\n ")
    print("1. NOMBRE PRODUCTO   \n")
    print("2. PRECIO  \n")
    print("3. CANTIDAD  \n")
    print("4. CATEGORIA  \n")
    print("5. SALIR \n")
    while True:
        try:
            opcion = int(input("\nSelecciona una opción: (5 para salir)"))
            if opcion == 1:
                nuevo_nombre = input("Ingresa el nuevo nombre del producto: ")
                producto["Producto"] = nuevo_nombre
                print("Nombre actualizado correctamente.\n")
            elif opcion == 2:
                nuevo_precio = float(input("Ingresa el nuevo precio: "))
                producto["Precio"] = nuevo_precio
                print("Precio actualizado correctamente.\n")
            elif opcion == 3:
                nueva_cantidad = int(input("Ingresa la nueva cantidad: "))
                producto["Cantidad"] = nueva_cantidad
                print("Cantidad actualizada correctamente.\n")
            elif opcion == 4:
                nueva_categoria = input("Ingresa la nueva categoría: ")
                producto["Categoria"] = nueva_categoria
                print("Categoría actualizada correctamente.\n")
            elif opcion == 5:
                print("Saliendo sin realizar cambios.\n")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, selecciona una opción válida.")
        except opcion<0:
             print("Entrada no válida. Por favor, selecciona una opción válida.")

def fEliminar_producto(diccionario):
    actu = True
    while actu:
        try:
            codProd = int(input("ingrese el Codigo  del producto: "))
            if type(codProd)== int and codProd > 0:
                    if diccionario[codProd]["Estado"] != False: 
                        diccionario[codProd]["Estado"]=False
                        print("\n PRODUCTO ELIMINADO CON EXITO !")
                        actu = False
                    else:
                        print("\n NO EXISTE UN PRODCUTO CON ESE CODIGO, POR FAVOR INGRESE UN CODIGO VALIDO")
        except ValueError:
                print("\nIngrese un codigo Valido\n")
        except KeyError:
            print("\n NO EXISTE UN PRODCUTO CON ESE CODIGO, POR FAVOR INGRESE UN CODIGO VALIDO")

def fBuscar_producto(diccionario):
    actu = True
    while actu:
        try:
            codProd = int(input("ingrese el Codigo  del producto: "))
            if type(codProd)== int and codProd > 0:
                    if diccionario[codProd]["Estado"] != False: 
                         
                        print("\n%-6s|%-16s|%-15s|%-14s|%-14s"%("CODIGO","PRODUCTO","PRECIO","CANTIDAD","CATEGORIA") )
                        print("%-6d|%-16s | $%15.2f | %14d | %14s" %(codProd,
                                            diccionario[codProd]["Producto"],
                                            diccionario[codProd]["Precio"],
                                            diccionario[codProd]["Cantidad"],
                                            diccionario[codProd]["Categoria"] ) )
                        actu = False
                    else:
                        print("\n NO EXISTE UN PRODCUTO CON ESE CODIGO, POR FAVOR INGRESE UN CODIGO VALIDO")
        except ValueError:
                print("\nIngrese un codigo Valido\n")
        except KeyError:
            print("\n NO EXISTE UN PRODCUTO CON ESE CODIGO, POR FAVOR INGRESE UN CODIGO VALIDO")

def fReporte_bajo_stock(mi_lista,limite):
    print("\n--------------PRODUCTOS CON BAJO STOCK---------------- \n")
    print("%-6s|%-16s|%-15s|%-14s|%-14s\n"%("CODIGO","PRODUCTOS","PRECIOS","CANTIDAD","CATEGORIA") )
    BAND =0
    for codigo, producto in mi_lista.items():
       if producto["Estado"] == True and producto["Cantidad"]< limite :
            BAND =1
            print("%-6d|%-16s | $%15.2f | %14d | %14s" %(codigo,producto["Producto"],producto["Precio"],
                                            producto["Cantidad"],producto["Categoria"] ) )
    
    if BAND ==0:
        print("\n NO HAY PRODUCTOS CON BAJO STOCK !!!! ")



