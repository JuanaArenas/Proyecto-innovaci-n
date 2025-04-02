from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import SQLALCHEMY_DATABASE_URI
app = Flask(__name__)
CORS(app)#habilita CORS  para permitir peticiones desde React

# Configurar SQLAlchemy con Oracle Cloud
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Definir el modelo de la base de datos
class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre, "precio": self.precio}

# Crear las tablas en la base de datos
with app.app_context():
    db.create_all()

# Ruta para obtener todos los productos
@app.route('/productos', methods=['GET'])
def get_productos():
    productos = Producto.query.all()
    return jsonify([p.to_dict() for p in productos])

# Ruta para obtener un producto por ID
@app.route('/productos/<int:id>', methods=['GET'])
def get_producto(id):
    producto = Producto.query.get(id)
    return jsonify(producto.to_dict()) if producto else ('Producto no encontrado', 404)

# Ruta para crear un nuevo producto
@app.route('/productos', methods=['POST'])
def create_producto():
    data = request.json
    nuevo_producto = Producto(nombre=data['nombre'], precio=data['precio'])
    db.session.add(nuevo_producto)
    db.session.commit()
    return jsonify(nuevo_producto.to_dict()), 201

# Ruta para actualizar un producto
@app.route('/productos/<int:id>', methods=['PUT'])
def update_producto(id):
    producto = Producto.query.get(id)
    if not producto:
        return ('Producto no encontrado', 404)
    
    data = request.json
    producto.nombre = data['nombre']
    producto.precio = data['precio']
    db.session.commit()
    return jsonify(producto.to_dict())

# Ruta para eliminar un producto
@app.route('/productos/<int:id>', methods=['DELETE'])
def delete_producto(id):
    producto = Producto.query.get(id)
    if not producto:
        return ('Producto no encontrado', 404)
    
    db.session.delete(producto)
    db.session.commit()
    return ('', 204)

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0', port=5000)