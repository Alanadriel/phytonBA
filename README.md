Título: Sistema de Inventario con SQLite
Descripción:
Este proyecto Python implementa un sencillo sistema de inventario utilizando SQLite como base de datos. El programa permite agregar, consultar, eliminar y generar reportes de productos almacenados.

Funcionalidades:
Agregar productos: Permite ingresar nuevos productos a la base de datos, especificando nombre, descripción, cantidad, precio y categoría.

Consultar productos: Muestra una lista completa de todos los productos registrados.

Buscar productos por ID: Permite buscar un producto específico por su ID.

Eliminar productos: Marca un producto como eliminado (soft delete) al cambiar su estado a 0.

Reporte de productos con bajo stock: Genera un reporte de los productos cuya cantidad está por debajo de un umbral establecido.

Menú de opciones: Presenta un menú interactivo para navegar entre las diferentes funcionalidades.

Estructura del Proyecto:
main.py: Contiene la lógica principal del programa, incluyendo el bucle principal y la interacción con el usuario.

Modulos/funcionesMBD.py: Contiene las funciones relacionadas con la base de datos, como crear la base de datos, crear tablas, insertar, leer, actualizar y eliminar registros.

Tecnologías Utilizadas:
Python: Lenguaje de programación principal.
SQLite: Sistema de gestión de bases de datos.
os: Módulo de Python para interactuar con el sistema operativo.


ID: Identificador único del producto (autoincremental).
NOMBRE: Nombre del producto.
DESCRIPCION: Descripción detallada del producto.
CANTIDAD: Cantidad disponible en el inventario.
PRECIO: Precio unitario del producto.
CATEGORIA: Categoría a la que pertenece el producto.
ESTADO: Indica si el producto está activo (1) o eliminado (0).

Consideraciones:
Mejora: Se podrían agregar funcionalidades como edición de productos, búsqueda por otros criterios (nombre, categoría), exportación de datos a diferentes formatos, etc.


Seguridad: Si se trata de un sistema de producción, se deben considerar aspectos de seguridad como la protección de la base de datos y la autenticación de usuarios.
Autor:
    Alan Martin

Fecha:
    05/12/2024