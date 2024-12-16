import sqlite3 as sql

#FUNCIONES RELACIONADAS CON LA BASE DE DATOS
#RUTA DB windows C:\\PROYECTOS\\Python\\PYTHONBA\\BaseDatos\\Inventario.db
ruta_dataBase = f"/home/alanm/Programas/Python/phytonBA/BaseDatos/Inventario.db" #ruta db linux

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
        CATEGORIA TEXT NOT NULL,
        ESTADO INTEGER DEFAULT 1
        ) """)
    conn.commit()
    conn.close()

class BASEDATOS:
    def __init__(self,ruta_db):
        self.conn =sql.connect(ruta_db)
        self.c = self.conn.cursor()

    def execute(self,query,parametros = None):
        if parametros:
            self.c.execute(query,parametros)
        else:
            self.c.execute(query)
        self.conn.commit()


    def close(self):
        self.conn.close()


class producto_db:
    def __init__(self,ruta_db):
        self.db = BASEDATOS(ruta_db) 


    def insertar_producto_DB(self,nombr,descripcion,cant,precio,cat):
        query = """
            INSERT INTO PRODUCTOS (NOMBRE, DESCRIPCION, CANTIDAD, PRECIO , CATEGORIA)
            VALUES (?, ?, ?, ?, ?)
        """
        valores = (nombr, descripcion, cant, precio, cat)
        self.db.execute(query,valores)

    def obtener_productos_DB(self):
        query = f"SELECT * FROM PRODUCTOS WHERE ESTADO=1"
        self.db.execute(query)
        return self.db.c.fetchall()


    def consultar_producto_ID(self,id):
        query = f"SELECT * FROM PRODUCTOS WHERE ID= {id} AND ESTADO=1"
        self.db.execute(query)
        return self.db.c.fetchone()
    

    def eliminar_Producto_ID_DB(self,id):
        #FUNCION DE "ELIMINACION" DE PRODUCTO, ASIGNAMOS ESTADO=0 (PRODUCTO INVALIDO)
        query = f"UPDATE PRODUCTOS SET ESTADO=0 WHERE id = {id} AND ESTADO=1"
        self.db.execute(query)

    def actualizar_producto_BD(self,id,nombr,descripcion,cant,precio,cat):
       
        query = f"""
            UPDATE PRODUCTOS SET NOMBRE=?, DESCRIPCION=?, CANTIDAD=?, PRECIO=? , CATEGORIA=?
            WHERE ID=? AND ESTADO=1
        """
        valores = (nombr, descripcion, cant, precio, cat,id)
        self.db.execute(query,valores)
        


    def get_ultimoProducto(self):
        
        query = f"SELECT * FROM productos ORDER BY id DESC LIMIT 1"
        self.db.execute(query)
        return self.db.c.fetchone()
