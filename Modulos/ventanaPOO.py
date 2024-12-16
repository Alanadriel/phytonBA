from tkinter import *
from tkinter import ttk
from BaseDatos import controladorDB as CBD

ruta_dataBase = f"/home/alanm/Programas/Python/phytonBA/BaseDatos/Inventario.db" #ruta db linux

class Ventana(Frame):
    inventario = CBD.producto_db(ruta_dataBase)
    
    def __init__(self, master = None):
        super().__init__(master,width=800,height=600)
        self.master = master
        self.pack()
        self.crear_widgets()
        self.llenar_tabla_productos()

        self.master.protocol("WM_DELETE_WINDOW", self.on_close)


    def crear_widgets(self):
        #MARCO IZQUIERDO 
        frame_btns = Frame(self,bg="#bfdaff")
        frame_btns.place(x=0,y=0,width=200, height=599)

        # CONSTANTES ESPACIADO (X,Y)
        base_x = 10
        base_y =10
        espacio_y = 35

        # LABELS Y ENTRYS 
            #NOMBRE DEL PRODUCTO
        lbl_name = Label(frame_btns,text="Nombre del Producto")
        lbl_name.place(x=base_x,y= base_y)
        self.name_entry = Entry(frame_btns)
        self.name_entry.place(x= base_x,y= base_y +20 ,width=180)

            #DESCRIPCION DEL PRODUCTO 
        lbl_descrip = Label(frame_btns,text="Descripcion del Producto")
        lbl_descrip.place(x= base_x,y= base_y + espacio_y*2)
        self.descrip_entry = Entry(frame_btns)
        self.descrip_entry.place(x= base_x,y= base_y + espacio_y*2 +20,width=180 )

            #CANTIDAD 
        lbl_cant = Label(frame_btns,text="Cantidad del Producto")
        lbl_cant.place(x=base_x,y = base_y + espacio_y *4 )
        self.cant_entry = Entry(frame_btns)
        self.cant_entry.place(x=base_x ,y = base_y + espacio_y *4 +20, width=180)

            #PRECIO
        lbl_precio = Label(frame_btns,text="Precio del Producto")
        lbl_precio.place(x= base_x ,y= base_y +espacio_y*6)
        self.precio_entry = Entry(frame_btns)
        self.precio_entry.place(x = base_x,y = base_y + espacio_y*6 + 20,width=180)

            #CATEGORIA
        lbl_cat = Label(frame_btns,text="Categoria del Producto")
        lbl_cat.place(x=base_x,y=base_y + espacio_y*8)
        self.categ_entry = Entry(frame_btns)
        self.categ_entry.place(x = base_x,y= base_y + espacio_y*8 + 20,width=180)


        #BOTONES 
            #agregar producto
        btn_agregar = Button(frame_btns,text="Agregar",command= self.fagregarProd,bg="green", fg="white" )
        btn_agregar.place(x=base_x, y= base_y +espacio_y*10 ,width=80,height=30)

            #Eliminar producto
        btn_eliminar = Button(frame_btns,text="Eliminar",command= self.feliminarProd,bg="red", fg="white" )
        btn_eliminar.place(x=base_x+80, y=base_y +espacio_y*10,width=80,height=30)
            #Actualizar producto
        btn_actualizar = Button(frame_btns,text="Actualizar",command= self.factualizarProd,bg="blue", fg="white" )
        btn_actualizar.place(x=base_x, y=base_y +espacio_y*11,width=80,height=30)

        #GRILLA TABLA 
        self.grid = ttk.Treeview(self, columns=("colName","colDescrip","colCant","colPrecio","colCateg") )
        #CONFIGURAR LAS COLUMNAS
        self.grid.column("#0",width=50)
        self.grid.column("colName",width= 60 ,anchor="center")
        self.grid.column("colDescrip",width= 60 ,anchor="center")
        self.grid.column("colCant",width= 60 ,anchor="center")
        self.grid.column("colPrecio",width= 60 ,anchor="center")
        self.grid.column("colCateg",width= 60 ,anchor="center")
        #ENCABEZADOS
        self.grid.heading("#0",text="ID",anchor="center" )
        self.grid.heading("colName",text="NOMBRE",anchor="center" )
        self.grid.heading("colDescrip",text="DECRIPCION",anchor="center" )
        self.grid.heading("colCant",text="CANTIDAD",anchor="center" )
        self.grid.heading("colPrecio",text="PRECIO",anchor="center" )
        self.grid.heading("colCateg",text="CATEGORIA",anchor="center" )
        #POSICIONAR TABLA
        self.grid.place(x=204,y=0, width=600,height=599)

        #EVENTO CLICK EN LA TABLA
        self.grid.bind("<<TreeviewSelect>>",self.llenar_entry_producto )

    
    def llenar_entry_producto(self,event):
        # obtenemos los elementos de un producto de la tabla (grid)
         
        self.item_sel = self.grid.selection()[0]  # Obtener la fila seleccionada
        datos = self.grid.item(self.item_sel)["values"]
        self.limpiar_entrys()
        
        self.name_entry.insert(0,datos[0])
        self.descrip_entry.insert(0,datos[1])
        self.cant_entry.insert(0,datos[2])
        self.precio_entry.insert(0,datos[3])
        self.categ_entry.insert(0,datos[4])
    
    def limpiarTabla(self):
        #  borrar contendio de la tabla(grid)
        for item in self.grid.get_children():
            self.grid.delete(item)
    
    def limpiar_entrys(self):
        # borrar contenido de los entrys
        self.name_entry.delete(0,END)
        self.descrip_entry.delete(0,END)
        self.cant_entry.delete(0,END)
        self.precio_entry.delete(0,END)
        self.categ_entry.delete(0,END)


    def llenar_tabla_productos(self):
        # llenar el grid con los productos de la BD
        self.limpiarTabla()
        datos = self.inventario.obtener_productos_DB()
        for row in datos:
            self.grid.insert("",END,text=row[0],values=(row[1],row[2],row[3],row[4],row[5] ) )
        
    def fagregarProd(self):
        #BOTON PARA AGREGAR PRODUCTOS A LA TABLA
        nombre = self.name_entry.get()
        descrip = self.descrip_entry.get()
        cant = self.cant_entry.get()
        preci = self.precio_entry.get()
        categ = self.categ_entry.get()

        self.inventario.insertar_producto_DB(nombre,descrip,cant,preci,categ)
        self.limpiar_entrys()
        
        self.llenar_tabla_productos()

    def feliminarProd(self):
        # BOTON ELIMINAR PRODUCTOS DE LA TABLA
        id = int (self.grid.item(self.item_sel,'text') )
        self.inventario.eliminar_Producto_ID_DB( id )
        self.llenar_tabla_productos()
        self.limpiar_entrys()
        

    def factualizarProd(self):
        # BOTON ACTUALIZAR PRODUCTOS 
        nombre = self.name_entry.get()
        descrip = self.descrip_entry.get()
        cant = self.cant_entry.get()
        preci = self.precio_entry.get()
        categ = self.categ_entry.get()

        id = int (self.grid.item(self.item_sel,'text') )
        self.inventario.actualizar_producto_BD(id,nombre,descrip,cant,preci,categ)
        self.limpiar_entrys()
        
        self.llenar_tabla_productos()

    def on_close(self):
        # Cierra la conexión a la base de datos
        self.inventario.db.close()
        # Destruye la ventana principal
        self.master.destroy()

