import sqlite3 as sql

#FUNCIONES RELACIONADAS CON LA BASE DE DATOS

ruta = f"C:\\PROYECTOS\\Python\\PYTHONBA\\BaseDatos\\Inventario.db" #RUTA DB

def crear_DB(nombre):
    conn = sql.connect(nombre) # "Inventario.db"
    conn.commit()
    conn.close()

def crear_Tablas_DB():
    conn = sql.connect(ruta)
    c = conn.cursor()
    c.execute(
        """CREATE TABLE PRODUCTOS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE TEXT NOT NULL,
        DESCRIPCION TEXT,
        CANTIDAD INTEGER NOT NULL,
        PRECIO FLOAT NOT NULL,
        CATEGORIA TEXT NOT NULL
        ) """)
    conn.commit()
    conn.close()

def insertar_FILA_DB(nombr,descripcion,cant,precio,cat):
    conn = sql.connect(ruta)
    c = conn.cursor()

    instruccion = """
        INSERT INTO PRODUCTOS (NOMBRE, DESCRIPCION, CANTIDAD, PRECIO , CATEGORIA)
        VALUES (?, ?, ?, ?, ?)
    """
    valores = (nombr, descripcion, cant, precio, cat)

    c.execute(instruccion,valores)
    conn.commit()
    conn.close()

def leer_DB():
    conn = sql.connect(ruta)
    c = conn.cursor()
    instrucccion = f"SELECT * FROM PRODUCTOS WHERE ESTADO=1"
    c.execute(instrucccion)
    datos = c.fetchall()

    conn.close()
    return datos

def consultar_DB_ID(id):
    conn = sql.connect(ruta)
    c = conn.cursor()
    instrucccion = f"SELECT * FROM PRODUCTOS WHERE ID= {id} AND ESTADO=1"
    c.execute(instrucccion)
    dato = c.fetchone()
    conn.close()
    if dato:
        return dato
    else:
        return -1
    
def agregar_Column_Estado_DB():
    #FUNCION PARA AGREGAR COLUMNA DE ESTADOS, PRODUCTO VALIDO=1 
    conn = sql.connect(ruta)
    c = conn.cursor()

    instruccion = f"ALTER TABLE PRODUCTOS ADD COLUMN ESTADO INTEGER DEFAULT 1;"

    c.execute(instruccion)
    conn.commit()
    conn.close()

def ocultar_Producto_ID_DB(id):
    #FUNCION DE "ELIMINACION" DE PRODUCTO, ASIGNAMOS ESTADO=0 (PRODUCTO INVALIDO)
    conn = sql.connect(ruta)
    c = conn.cursor()
    try:
        instrucccion = f"UPDATE PRODUCTOS SET ESTADO=0 WHERE id = {id} AND ESTADO=1"
        c.execute(instrucccion)
        if c.rowcount == 0:
            print(f"No se encontró ningún producto con ID {id}.")
        else:
            conn.commit()
            print("Producto Eliminado correctamente.")
    except sql.Error as e:
        print(f"Error al intentar modificar el estado del producto: {e}")
    finally:    
        conn.close()

def bajoStock_BD(bajoStock):
    conn = sql.connect(ruta)
    c = conn.cursor()
    instrucccion = f"SELECT * FROM PRODUCTOS WHERE CANTIDAD<{bajoStock} AND ESTADO=1"
    c.execute(instrucccion)
    dato = c.fetchall()
    conn.close()
    if dato:
        return dato
    else:
        return -1
    
def actualizar_fila_BD(id,nombr,descripcion,cant,precio,cat):
    conn = sql.connect(ruta)
    c = conn.cursor()

    instruccion = f"""
        UPDATE PRODUCTOS SET NOMBRE=?, DESCRIPCION=?, CANTIDAD=?, PRECIO=? , CATEGORIA=?
        WHERE ID=? AND ESTADO=1
    """
    valores = (nombr, descripcion, cant, precio, cat,id)

    c.execute(instruccion,valores)
    conn.commit()
    conn.close()


 


#crear_BaseDatos()
#crearTablas()
#insertarAtabla_prueba(2,"Alan","prueba",3,5.5,"Humano")
#leerBaseDatos()
#consultarProd_xID(3)

#insertar_FILA_DB("Don satur","dons satur grasa",3,3.5,"galletitas")

#agregar_Column_Estado_DB()