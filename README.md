# restaurante_app

**Estudiante:** Andrango Nieto Alison Dayana

## Contexto y objetivo

El proyecto `restaurante_app` corresponde a la Semana 14 de la asignatura Programación Orientada a Objetos y continúa con la interfaz gráfica desarrollada en la Semana 13.

En esta semana se trabaja con componentes, contenedores y gestores de geometría de Tkinter para mejorar la organización de la interfaz. También se incorpora la gestión de productos mediante operaciones de registro, carga, actualización y eliminación, manteniendo la lógica de negocio dentro de `RestauranteServicio` y la persistencia mediante archivos JSON.

## Estructura del proyecto

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── assets/
│   ├── home.png
│   ├── users.png
│   ├── products.png
│   ├── logout.png
│   ├── add.png
│   ├── search.png
│   ├── edit.png
│   ├── delete.png
│   └── clean.png
├── main.py
└── README.md
```

La estructura mantiene la separación entre datos, modelos, servicios, interfaz y punto de entrada de la aplicación.

## Mejoras realizadas en la interfaz

A partir de la versión gráfica anterior se reorganizó la interfaz principal mediante diferentes contenedores y componentes.

Se incorporó un menú lateral con las opciones:

* Inicio.
* Productos.
* Usuarios.
* Ventas.
* Cerrar sesión.

También se agregaron iconos para mejorar la identificación visual de las opciones y acciones.

En la sección de productos se organizaron las áreas de formulario y presentación de información, permitiendo trabajar con los datos de manera más clara.

## Componentes y contenedores utilizados

En la interfaz se utilizaron componentes de Tkinter y ttk como:

* `Frame`, para organizar las diferentes áreas de la ventana.
* `LabelFrame`, para agrupar el formulario y la lista de productos.
* `Label`, para mostrar títulos y textos.
* `Entry`, para ingresar los datos de los productos.
* `ttk.Button`, para ejecutar las acciones mediante `command=`.
* `Treeview`, para mostrar los productos registrados en una tabla.
* `Scrollbar`, para facilitar la visualización de la tabla.
* `messagebox`, para mostrar mensajes de información y errores.

Para organizar los componentes se utilizaron los gestores de geometría `pack()` y `grid()`.

## Gestión de productos

La sección de Productos permite realizar las operaciones solicitadas en la actividad.

### Registrar

Permite ingresar un nuevo producto mediante los campos de código, nombre, precio, categoría y stock.

La información se envía a `RestauranteServicio`, donde se valida y se registra el producto.

### Cargar por código

Permite buscar un producto que ya se encuentra registrado utilizando su código.

Cuando el producto existe, sus datos se cargan automáticamente en el formulario para poder revisarlos o modificarlos.

### Actualizar

Permite modificar los datos de un producto existente. La operación se realiza mediante `RestauranteServicio` y después se actualiza la información mostrada en la tabla.

### Eliminar

Permite eliminar un producto mediante su código. Después de la operación, la tabla y el formulario se actualizan.

### Limpiar

Permite borrar los datos ingresados en los campos del formulario.

## Persistencia y responsabilidades

Los productos se mantienen en:

```text
datos/productos.json
```

Las operaciones de registro, actualización y eliminación guardan los cambios mediante `ArchivoServicio`.

La interfaz no realiza directamente la lectura o escritura de los archivos JSON. Las operaciones son solicitadas a `RestauranteServicio`, manteniendo separadas las responsabilidades de la interfaz, la lógica de negocio y el almacenamiento.

## Actualización de la interfaz

Después de realizar operaciones sobre los productos, la tabla se actualiza para mostrar inmediatamente los cambios realizados.

La barra de estado también muestra la cantidad de productos y usuarios registrados.

De esta manera, el usuario puede observar el resultado de las operaciones sin necesidad de reiniciar la aplicación.

## Flujo de la aplicación

```text
Inicio
  ↓
LoginView
  ↓
Validación mediante RestauranteServicio
  ↓
MainView
  ↓
Inicio | Productos | Usuarios | Ventas
              ↓
          Productos
              ↓
Registrar | Cargar | Actualizar | Eliminar
              ↓
      RestauranteServicio
              ↓
      productos.json
              ↓
     Actualización de la tabla
```

El inicio de sesión y el flujo general de la Semana 13 se mantienen en esta versión.

## Comprobación del funcionamiento

Se ejecutó `main.py` y se comprobó el funcionamiento de las principales opciones de la aplicación.

Se verificó que:

* El inicio de sesión funciona correctamente.
* La interfaz principal se muestra después del acceso.
* El botón Inicio permite regresar al panel principal.
* La sección Usuarios muestra la información registrada.
* La sección Productos muestra el formulario y la tabla.
* Se puede registrar un nuevo producto.
* Se puede cargar un producto existente mediante su código.
* Se puede actualizar la información de un producto.
* Se puede eliminar un producto.
* La tabla se actualiza después de las operaciones.
* Los cambios se guardan en `productos.json`.
* Los cambios permanecen después de cerrar y volver a ejecutar la aplicación.
* La opción Ventas permanece como funcionalidad pendiente.
* La aplicación mantiene la separación entre interfaz, servicios y datos.

## Ejecución

Para ejecutar la aplicación se debe ingresar a la carpeta `restaurante_app` y ejecutar:

```bash
python main.py
```

También puede ejecutarse directamente desde Visual Studio Code u otro entorno de desarrollo compatible con Python.

## Tecnologías utilizadas

* Python.
* Programación Orientada a Objetos.
* Tkinter.
* Tkinter ttk.
* JSON.
* Visual Studio Code.
* Git y GitHub.

## Conclusión

En esta semana se evolucionó la interfaz gráfica de `restaurante_app` mediante el uso de componentes, contenedores y gestores de geometría de Tkinter.

Además, se incorporó la gestión de productos desde la interfaz mediante las operaciones de registrar, cargar, actualizar y eliminar. Estas operaciones se mantienen delegadas a `RestauranteServicio` y los cambios se conservan mediante `ArchivoServicio` en `productos.json`.

Con estas mejoras, la aplicación mantiene su arquitectura modular y presenta una interfaz más organizada para consultar información y gestionar los productos.
