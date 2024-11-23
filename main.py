import funciones 
import os

otraLista = {
1: {"Producto": "Manzana" , "Precio": 500.25 , "Cantidad": 200,"Categoria": "Verduras","Estado": True },
2: {"Producto": "Pera" , "Precio": 54654.5654 , "Cantidad": 300,"Categoria":"Verduras","Estado":True },
3: {"Producto": "Tomate " , "Precio": 50.30, "Cantidad": 101,"Categoria": "Verduras","Estado":True},
4: {"Producto": "Zanahoria" , "Precio": 12.36 , "Cantidad": 502,"Categoria":"Verduras","Estado":True },
5: {"Producto": "Rucula" , "Precio": 10, "Cantidad": 130,"Categoria":"Verduras","Estado":True }
}



os.system('cls')
opcion = funciones.MenuOptions()
while(opcion != 7):
    if(opcion == 1):
        funciones.fagregarProds(otraLista)
        opcion = funciones.MenuOptions()
        os.system('cls')
    elif(opcion == 2):
        os.system('cls')
        funciones.fmostrarProductos(otraLista)
        opcion = funciones.MenuOptions()
    elif(opcion==3):
        funciones.factualizar_Producto(otraLista)
        opcion = funciones.MenuOptions()
        os.system('cls')
    elif(opcion == 4):
        funciones.fEliminar_producto(otraLista)
        opcion = funciones.MenuOptions()
        os.system('cls')
    elif(opcion == 5):
        funciones.fBuscar_producto(otraLista)
        opcion = funciones.MenuOptions()
    elif(opcion == 6):
        funciones.fReporte_bajo_stock(otraLista,100)
        opcion = funciones.MenuOptions()
        


