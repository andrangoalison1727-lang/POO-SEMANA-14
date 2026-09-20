# restaurante_app

**Estudiante:** Andrango Nieto Alison Dayana

## Contexto y objetivo

El proyecto `restaurante_app` corresponde a la Semana 14 de la asignatura Programación Orientada a Objetos y continúa con la interfaz gráfica desarrollada en la Semana 13.

En esta semana se trabaja con componentes y contenedores de Tkinter para organizar mejor la interfaz y se incorpora la gestión de productos desde la aplicación gráfica.

El objetivo es utilizar los componentes y contenedores de forma organizada, manteniendo la separación entre la interfaz, la lógica de negocio y el almacenamiento de datos.

## Mejoras realizadas

En esta versión se realizaron las siguientes mejoras:

* Se incorporó un menú lateral con las opciones Inicio, Productos, Usuarios, Ventas y Cerrar sesión.
* Se agregaron iconos para las opciones y acciones principales.
* Se organizaron los elementos mediante `Frame` y `LabelFrame`.
* Se incorporó un formulario para ingresar los datos de los productos.
* Se incorporó una tabla `Treeview` para mostrar los productos registrados.
* Se agregó una barra de desplazamiento para la tabla.
* Se incorporaron botones para las operaciones de productos.
* Se mantiene una barra de estado con la cantidad de productos y usuarios.

## Gestión de productos

Desde la sección **Productos** se pueden realizar las siguientes operaciones:

* **Registrar:** permite agregar un nuevo producto.
* **Cargar por código:** busca un producto existente y carga sus datos en el formulario.
* **Actualizar:** modifica los datos de un producto registrado.
* **Eliminar:** elimina un producto mediante su código.
* **Limpiar:** borra los datos ingresados en el formulario.

Las operaciones son realizadas mediante `RestauranteServicio`, manteniendo la lógica de negocio separada de la interfaz gráfica.

## Persistencia de datos

Los cambios realizados en los productos se guardan automáticamente en:

```text
datos/productos.json
```

`ArchivoServicio` se encarga de escribir los datos en el archivo JSON.

De esta manera, los productos registrados, actualizados o eliminados mantienen los cambios aunque la aplicación se cierre y vuelva a ejecutarse.

## Componentes y contenedores utilizados

En la interfaz se utilizaron principalmente:

* `Frame` para organizar las diferentes áreas.
* `LabelFrame` para agrupar el formulario y la tabla.
* `Label` para textos y títulos.
* `Entry` para ingresar datos.
* `ttk.Button` para ejecutar acciones.
* `Treeview` para mostrar los productos.
* `Scrollbar` para desplazarse por la tabla.
* `messagebox` para mostrar mensajes.

También se utilizan los gestores `pack()` y `grid()` para organizar los componentes.

## Comprobación del funcionamiento

Se ejecutó `main.py` y se comprobó el funcionamiento de las principales operaciones.

Se verificó que:

* El inicio de sesión permite acceder a la interfaz principal.
* El menú lateral funciona correctamente.
* Los productos registrados se muestran en la tabla.
* Se puede registrar un producto.
* Se puede cargar un producto mediante su código.
* Se puede actualizar un producto.
* Se puede eliminar un producto.
* Los cambios se reflejan en la tabla.
* Los cambios se guardan en `productos.json`.
* La información permanece después de volver a ejecutar la aplicación.
* El botón Inicio regresa al panel principal.
* La opción Usuarios muestra los usuarios registrados.
* La opción Ventas permanece como funcionalidad pendiente.

## Ejecución

Para ejecutar la aplicación:

```bash
python main.py
```

## Tecnologías utilizadas

* Python
* Programación Orientada a Objetos
* Tkinter
* JSON
* Visual Studio Code
* Git y GitHub

## Conclusión

En esta semana se mejoró la interfaz gráfica de `restaurante_app` mediante el uso de componentes y contenedores de Tkinter.

Además, se incorporó la gestión completa de productos desde la interfaz, incluyendo registro, búsqueda, actualización y eliminación, manteniendo la lógica en `RestauranteServicio` y la persistencia mediante archivos JSON.
