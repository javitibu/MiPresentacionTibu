#--------------------------------------------------------------------
# Instalar con pip install Flask
from flask import Flask, request, jsonify, render_template
#from flask import request

# Instalar con pip install flask-cors
from flask_cors import CORS

# Instalar con pip install mysql-connector-python
import mysql.connector

# Si es necesario, pip install Werkzeug
from werkzeug.utils import secure_filename

# No es necesario instalar, es parte del sistema standard de Python
import os
import time
#--------------------------------------------------------------------



app = Flask(__name__)
CORS(app)  # Esto habilitará CORS para todas las rutas

#--------------------------------------------------------------------
class Catalogo:
    #----------------------------------------------------------------
    # Constructor de la clase
    def __init__(self, host, user, password, database):
        # Primero, establecemos una conexión sin especificar la base de datos
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        self.cursor = self.conn.cursor()

        # Intentamos seleccionar la base de datosz
        try:
            self.cursor.execute(f"USE {database}")
        except mysql.connector.Error as err:
            # Si la base de datos no existe, la creamos
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE {database}")
                self.conn.database = database
            else:
                raise err

        # Una vez que la base de datos está establecida, creamos la tabla si no existe
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
            codigo INT PRIMARY KEY,
            apellido VARCHAR(255) NOT NULL,
            nombre VARCHAR(255) NOT NULL,
            correo VARCHAR(255) NOT NULL,
            telefono VARCHAR(255) NOT NULL,                                             
            comentario VARCHAR(255) NOT NULL,
            edad VARCHAR(255) NOT NULL,
            cv VARCHAR(255))
                            ''')
        self.conn.commit()

        # Cerrar el cursor inicial y abrir uno nuevo con el parámetro dictionary=True
        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)
        
    #----------------------------------------------------------------
    def agregar_producto(self, codigo, apellido, nombre, correo, telefono, comentario, edad, cv):
        # Verificamos si ya existe un producto con el mismo código
        self.cursor.execute(f"SELECT * FROM productos WHERE codigo = {codigo}")
        producto_existe = self.cursor.fetchone()
        if producto_existe:
            return False

        sql = "INSERT INTO productos (codigo, apellido, nombre, correo, telefono, comentario, edad, cv) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (codigo, apellido, nombre, correo, telefono, comentario, edad, cv)

        self.cursor.execute(sql, valores)        
        self.conn.commit()
        return True

    #----------------------------------------------------------------
    def consultar_producto(self, codigo):
        # Consultamos un producto a partir de su código
        self.cursor.execute(f"SELECT * FROM productos WHERE codigo = {codigo}")
        return self.cursor.fetchone()

    #----------------------------------------------------------------
    def modificar_producto(self, codigo, nuevo_apellido, nuevo_nombre, nuevo_correo, nuevo_telefono, nueva_edad, nuevo_comentario, nuevo_cv):
        sql = "UPDATE productos SET apellido = %s, nombre = %s, correo = %s, telefono = %s, comentario = %s, edad = %s, cv = %s WHERE codigo = %s"
        valores = (nuevo_apellido, nuevo_nombre, nuevo_correo, nuevo_telefono, nuevo_comentario, nueva_edad, nuevo_cv, codigo)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0




    #----------------------------------------------------------------
    def listar_productos(self):
        self.cursor.execute("SELECT * FROM productos")
        productos = self.cursor.fetchall()
        return productos

    #----------------------------------------------------------------
    def eliminar_producto(self, codigo):
        # Eliminamos un producto de la tabla a partir de su código
        self.cursor.execute(f"DELETE FROM productos WHERE codigo = {codigo}")
        self.conn.commit()
        return self.cursor.rowcount > 0

    #----------------------------------------------------------------
    def mostrar_producto(self, codigo):
        # Mostramos los datos de un producto a partir de su código
        producto = self.consultar_producto(codigo)
        if producto:
            print("-" * 40)
            print(f"Codigo: {producto['codigo']}")
            print(f"Apellido: {producto['apellido']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Correo {producto['correo']}")
            print(f"Telefono: {producto['telefono']}")
            print(f"Comentario: {producto['comentario']}")
            print(f"Edad: {producto['edad']}")
            print(f"CV: {producto['cv']}")
            print("-" * 40)
        else:
            print("Producto no encontrado.")


#--------------------------------------------------------------------
# Cuerpo del programa
#--------------------------------------------------------------------
# Crear una instancia de la clase Catalogo
catalogo = Catalogo(host='localhost', user='root', password='', database='miapp')

catalogo.agregar_producto(1, "Jorge1", "Roman1", "Jorge1@gmail.com", 22176781, "quiero trabajar1", 23, "jorgeroman1.pdf")
catalogo.agregar_producto(2, "Jorge2", "Roman2", "Jorge2@gmail.com", 22276782, "quiero trabajar2", 24, "jorgeroman2.pdf")
catalogo.agregar_producto(6, "Jorge3", "Roman3", "Jorge3@gmail.com", 22376783, "quiero trabajar3", 25, "jorgeroman3.pdf")

# Carpeta para guardar las imagenes.
RUTA_DESTINO = './static/imagenes/'

#--------------------------------------------------------------------
@app.route("/productos", methods=["GET"])
def listar_productos():
    productos = catalogo.listar_productos()
    return jsonify(productos)

#--------------------------------------------------------------------
@app.route("/productos/<int:codigo>", methods=["GET"])
def mostrar_producto(codigo):
    producto = catalogo.consultar_producto(codigo)
    if producto:
        return jsonify(producto), 201
    else:
        return "Producto no encontrado", 404


#--------------------------------------------------------------------
@app.route("/productos", methods=["POST"])
def agregar_producto():
    #Recojo los datos del form
    codigo = request.form['codigo']
    apellido = request.form['apellido']
    nombre = request.form['nombre']
    correo = request.form['correo']
    telefono = request.form['telefono']
    comentario = request.form['comentario']  
    edad = request.form['edad']
    cv = request.form['cv']

    # Me aseguro que el producto exista
    producto = catalogo.consultar_producto(codigo)

    if catalogo.agregar_producto(codigo,apellido, nombre, correo, telefono, comentario, edad, cv):
        return jsonify({"mensaje": "Producto agregado"}), 201
    else:
        return jsonify({"mensaje": "Producto ya existe"}), 400

#--------------------------------------------------------------------
@app.route("/productos/<int:codigo>", methods=["PUT"])
def modificar_producto(codigo):
    # Recojo los datos del formulario
    nuevo_apellido = request.form.get("apellido")
    nuevo_nombre = request.form.get("nombre")
    nuevo_correo = request.form.get("correo")
    nuevo_telefono = request.form.get("telefono")
    nueva_edad = request.form.get("edad")
    nuevo_cv = request.form.get("cv")
    nuevo_comentario = request.form.get("comentario")  # Nuevo campo comentario

    if catalogo.modificar_producto(codigo, nuevo_apellido, nuevo_nombre, nuevo_correo, nuevo_telefono, nueva_edad, nuevo_comentario, nuevo_cv):
        return jsonify({"mensaje": "Producto modificado"}), 200
    else:
        return jsonify({"mensaje": "Producto no encontrado"}), 403



#--------------------------------------------------------------------
@app.route("/productos/<int:codigo>", methods=["DELETE"])
def eliminar_producto(codigo):
    # Luego, elimina el producto del catálogo
    if catalogo.eliminar_producto(codigo):
        return jsonify({"mensaje": "Producto eliminado"}), 200
    else:
        return jsonify({"mensaje": "Error al eliminar el producto"}), 500
    

#--------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
