import funciones 

productosList=[ ["Mazanas", 12.00 , 30],
                ["Peras", 9.50 , 15 ],
                ["Tomate", 15.50, 50],
                ["Zanahoria", 11.00 , 10],
                ["Algo", 45.00 , 48 ] ]



opcion = funciones.MenuOptions()
while(opcion != 3):
    if(opcion == 1):
        funciones.fagregarProds(productosList)
        opcion = funciones.MenuOptions()
    elif(opcion == 2):
        funciones.fmostrarProductos(productosList)
        opcion = funciones.MenuOptions()