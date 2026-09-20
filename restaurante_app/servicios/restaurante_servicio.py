from modelos.producto import Producto
from modelos.usuario import Usuario

class RestauranteServicio:
    def __init__(self, archivo_servicio) -> None:
        self.archivo_servicio = archivo_servicio
        self.usuarios = []
        self.productos = []
        self.cargar_datos()

    def cargar_datos(self) -> None:
        usuarios_json = self.archivo_servicio.leer_json("usuarios.json")
        productos_json = self.archivo_servicio.leer_json("productos.json")

        self.usuarios = [
            Usuario(
                datos.get("identificacion", ""),
                datos.get("nombre", ""),
                datos.get("email", ""),
                datos.get("usuario", ""),
                datos.get("contrasena", "")
            )
            for datos in usuarios_json
        ]

        self.productos = [
            Producto(
                datos.get("nombre", ""),
                datos.get("codigo", ""),
                datos.get("precio", 0),
                datos.get("categoria", ""),
                datos.get("stock", 0)
            )
            for datos in productos_json
        ]

    def validar_acceso(self, usuario, contrasena):
        for usuario_registrado in self.usuarios:
            if (
                usuario_registrado.usuario == usuario
                and usuario_registrado.contrasena == contrasena
            ):
                return usuario_registrado
        return None

    def cantidad_usuarios(self):
        return len(self.usuarios)

    def cantidad_productos(self):
        return len(self.productos)

    def listar_usuarios(self):
        return self.usuarios

    def listar_productos(self):
        return self.productos

    def guardar_productos(self):
        datos = [
            {
                "nombre": producto.nombre,
                "codigo": producto.codigo,
                "precio": producto.precio,
                "categoria": producto.categoria,
                "stock": producto.stock,
            }
            for producto in self.productos
        ]
        self.archivo_servicio.escribir_json("productos.json", datos)
    def buscar_producto_por_codigo(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None

    def registrar_producto(self, nombre, codigo, precio, categoria, stock):
        nuevo_producto = Producto(nombre, codigo, precio, categoria, stock)

        if self.buscar_producto_por_codigo(nuevo_producto.codigo) is not None:
            raise ValueError("El codigo indicado ya corresponde a un producto registrado.")

        self.productos.append(nuevo_producto)
        self.guardar_productos()
        return nuevo_producto

    def actualizar_producto(self, nombre, codigo, precio, categoria, stock):
        producto_actualizado = self.buscar_producto_por_codigo(codigo)

        if producto_actualizado is None:
            raise ValueError("El codigo indicado no corresponde a ningun producto registrado.")

        datos_validados = Producto(nombre, codigo, precio, categoria, stock)
        producto_actualizado.nombre = datos_validados.nombre
        producto_actualizado.precio = datos_validados.precio
        producto_actualizado.categoria = datos_validados.categoria
        producto_actualizado.stock = datos_validados.stock
        self.guardar_productos()
        return producto_actualizado

    def eliminar_producto(self, codigo):
        producto_eliminado = self.buscar_producto_por_codigo(codigo)

        if producto_eliminado is None:
            raise ValueError("El codigo indicado no corresponde a ningun producto registrado.")

        self.productos.remove(producto_eliminado)
        self.guardar_productos()
        return producto_eliminado