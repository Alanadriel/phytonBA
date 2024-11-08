import funciones 
import os

otraLista = [
                {"Producto": "Manzanas" , "Precio": 500.25 , "Cantidad": 20 },
                {"Producto": "Peras" , "Precio": 54654.5654 , "Cantidad": 3 },
                {"Producto": "Tomate " , "Precio": 50.30, "Cantidad": 8000 },
                {"Producto": "Zanahoria" , "Precio": 12.36 , "Cantidad": 5464 },
                {"Producto": "Rucula" , "Precio": 10, "Cantidad": 13 }
            ]

os.system('cls')
opcion = funciones.MenuOptions()
while(opcion != 3):
    if(opcion == 1):
        funciones.fagregarProds(otraLista)
        opcion = funciones.MenuOptions()
        os.system('cls')
    elif(opcion == 2):
        os.system('cls')
        funciones.fmostrarProductos(otraLista)
        opcion = funciones.MenuOptions()

