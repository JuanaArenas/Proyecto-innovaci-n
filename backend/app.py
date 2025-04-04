from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from  flask_cors import CORS
from config import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)
CORS(app)#PERMITE PETIVCIONES DESDE REACT

#CONFIGURAR EL QSlALCHEMY CON ORACLE CLOUD
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#CONFIGURAR EL QSlALCHEMY CON ORACLE CLOUD
db = SQLAlchemy(app)

#DEFINIR EL MODELO DE LA BASE DE DATOS
class Producto(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {	
            'id': self.id,
            'nombre': self.nombre,
            'precio': self.precio
        }
#crear  las tablas en la base de datos
with app.app_context():
    db.create_all()

#RUTA PARA OBTENER TODOS LOS PRODUCTOS
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

# RUTA PARA OBTENER TODOS LOS PRODUCTOS 
@app.route('/productos', methods=['GET'])
def get_productos():
    productos = Producto.query.all()
    return jsonify([p.to_dict() for p in productos])
    
# RUTA PARA  PARA OBTENER UN  PRODUCTO POR ID
@app.route('/productos/<int:id>', methods=['GET'])
def get_productos(id):
    producto = Producto.query.get(id)
    return jsonify([producto.to_dict() if producto else ('Producto no encontrado'), 404])	

if __name__ == '__main__':
    app.run(debug=True)


    