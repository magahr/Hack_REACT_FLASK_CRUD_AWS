# CON LA BASE DE DATOS AWS BD formulario
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask_cors import CORS
from dotenv import load_dotenv
import psycopg2
import os

load_dotenv()

app = Flask(__name__) 

# Configuración de CORS para permitir solicitudes desde cualquier origen
CORS(app, resources={r"/*": {"origins": "*"}})

db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME') 

# Improved connection URL construction
db_url = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Creación del modelo de Formulario (modelo - tabla de la base de datos)
class Formulario(db.Model):
     nombre = db.Column(db.String(50), nullable = False)
     email = db.Column(db.String(50), nullable = False)
     edad = db.Column(db.Integer, nullable = False)
     id = db.Column(db.Integer, primary_key = True)
    
     def to_dist(self):
         return {
             'nombre': self.nombre,
             'email': self.email,
             'edad': self.edad,
             'id': self.id
         }

# Creación de la Base de Datos y su tabla
with app.app_context():
     db.create_all()
     try:  
        db.session.execute(text('SELECT 1'))
        print("Conexion a la base de datos exitosa")
     except Exception as e:
        print(f'Error al conectar a la base de datos: {e}')

@app.route("/")
def hello_world():
    return "<p> Hello, From AWS - My back and BD is in AWS - !</p>"

@app.route('/create-formulario', methods=['POST'])
def create_formulario():
    data = request.json
    new_formulario = Formulario(nombre=data['nombre'], edad=data['edad'], email=data['email']) 
    db.session.add(new_formulario)
    db.session.commit()
    return jsonify({'message': 'Usuario creado correctamente', 'data': new_formulario.to_dist()})

@app.route('/formularios', methods=['GET'])
def get_formularios():
    formularios = Formulario.query.all()
    return jsonify([formulario.to_dist() for formulario in formularios])

@app.route('/formularios/<int:formulario_id>', methods=['GET'])
def get_formulario_by_id(formulario_id):
    formulario = Formulario.query.get(formulario_id)
    if formulario:
        return jsonify(formulario.to_dist())
    return jsonify({'message': 'El usuario no ha sido encontrado'})

@app.route('/patch-formulario/<int:formulario_id>', methods=['PATCH'])
def update_one_formulario(formulario_id):
    data = request.json
    formulario = Formulario.query.get(formulario_id)
    if formulario:
       for key, value in data.items():
           setattr(formulario, key, value)
       db.session.commit()
       return jsonify({'message': 'Usuario actualizado parcialmente', 'data': formulario.to_dist()})
    return jsonify({'message': 'Usuario no encontrado'})

@app.route('/delete-formulario/<int:formulario_id>', methods=['DELETE'])
def delete_formulario_by_nombre(formulario_id):
    formulario = Formulario.query.get(formulario_id)
    if formulario:
        db.session.delete(formulario)
        db.session.commit()
        return jsonify({'message': f'Usuario con ID {formulario_id} eliminado'})
    else:
        return jsonify({'message': 'Usuario no encontrado'}), 404

# Asegúrate de que Flask escuche en todas las interfaces y el puerto 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
