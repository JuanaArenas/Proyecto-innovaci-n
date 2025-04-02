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
@app.route('/productos', methods=['GET'])
def get_productos():
    productos = Producto.query.all()
    return jsonify([producto.to_dict() for producto in productos])

#RUTA PARA OBTENER UN PRODUCTO POR ID

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=5000")