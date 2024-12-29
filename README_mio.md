# Hack_REACT_FLASK_CRUD

     Rutas en el trabajo:
          
          Repo:
          C:\Users\mhernandez.FOSPUCA\Documents\cursos\Ciclo08\Practica\hack\React\Hack_REACT_FLASK_CRUD_AWS




# Paso 1.- Clone el repo
    git clone  https://github.com/magahr/Hack_REACT_FLASK_CRUD_AWS.git

# Paso 2.-Entre en le directorio de repo 
   cd Hack_REACT_FLASK_CRUD

# Paso 3: crear el virtual 
    Con Bach:
        python  -m venv .venv
    
# Paso 4: activar el virtual env ubicando nuestra carpeta del virtual env creada anteriormente, en mi caso fue "venv"
    Desde la consola Bach:
        # source .venv/Scripts/activate
    Desde la consola de Cmder
        .venv\Scripts\activate
   
# Paso 5.-Cree (o colocar de otro proyecto del mismo lenguaje) el .gitignore y cloque a:
   # Environments
    .env
    .venv
    env/
    venv/
    ENV/
    env.bak/
    venv.bak/  

# crear la variable de entorno .env
   DB_USER=postgres
   DB_PASSWORD=postgres
   DB_HOST=formulariosrds.chwqcma4ef8n.us-east-2.rds.amazonaws.com
   DB_PORT=5432
   DB_NAME=formularios

   este es con la nueva BD
  DB_USER=postgres
  DB_PASSWORD=postgres
  DB_HOST=formularios02rds.chwqcma4ef8n.us-east-2.rds.amazonaws.com
  DB_PORT=5432
  DB_NAME=formularios

    
# Paso 6.- Salir de Visual CODE

# Paso 7.- Entrar a la carpeta del repo

# Paso 8.- Abrir Visual Code desde la carpeta del repo para que se vea .venv ignorado

# Paso 9.- instalar flsk con pip, en caso que no este instaldo
     pip install Flask
     pip list
 
# Paso 10.- instalar las librerias necesaria para conectar flask con una base de datos.
     ORM:
       Flask-SQAIchemy (extension que facilita el uso de SQLAIchemy con Flask)
       
     POSTGRESS: (Adaptador de Postgress para python):
       
     Comando con pip, instalar los dos:
        pip install Flask-SQLAlchemy
        pip install psycopg2 (desde la consola de cmder)
        pip install flask-cors  
        pip install python-dotenv

     Comando para verificar que se instalo:
        pip list

# Paso 11: instalar o crear uno nuevo las dependencias necesarias las cuales dejare en un archivo requirements.txt
    Si ya esta creado, para actualizar una ves que ya se ha bajado el repo:
       # pip install -requirements.txt

    Si no está creado, o se quiere actualizar:
       # pip freeze > requirements.txt

# Paso 12: Crear una nueva rama para trabajar desde alli
     git checkout -b feature/flask-con-base-de-datos

# Paso 13 : Levantar el servidor con el siguiente comando
    Con una aplicación:
    # flask --app hello run
    Con debug:
      flask run --debug

# Paso 14 : Creacion de una BASE DE DATOS
    -Entrar en la consola de postgres
       psql -U postgres (usuario)
          password postgres
       \l (lista la BD)
    -Crear la BASE DE DATOS
       
-- Table: public.formulario

-- DROP TABLE IF EXISTS public.formulario;

CREATE TABLE IF NOT EXISTS public.formulario
(
    id integer NOT NULL DEFAULT nextval('formulario_id_seq'::regclass),
    nombre character varying(50) COLLATE pg_catalog."default" NOT NULL,
    edad integer NOT NULL,
    email character varying(50) COLLATE pg_catalog."default",
    CONSTRAINT formulario_pkey PRIMARY KEY (id)
   
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.formulario
    OWNER to postgres;

OTRA FORMA:

CREATE TABLE formulario
(
    id serial PRIMARY KEY,
    nombre VARCHAR (50) UNIQUE NOT NULL,
    edad integer NOT NULL,
    email VARCHAR (50) NOT NULL
)

 

# Paso 15: Configuración de la Base de Datos
   - Importar los modulos correspondientes
     from flask import Flask, jsonify, request
     from flask_sqlalchemy import SQLAlchemy
     from sqlalchemy import text
     
   - buscar la configuracion del servidor en pgadmin,
    sobre el servidor boton derecho - ajustas de conexion,
    URL y seleccionar la url la palabra que va despues de
    jdbc..(no lo consegui ver video clase30 0:48:50)

   - #app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myuser:mypassword@localhost:5432/mydatabase'

    Variables :
      app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/estudiantes_grupo_8'

      app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

      db = SQLAlchemy(app)

     Definición del modelo de datos (modelo=tabla de bd):
     modelo de estudiante.
     
     class student(db.Model):

# Paso 17 - guardar los curl 
     
     curl -X GET http://localhost:5000/students
     curl -X POST http://localhost:5000/create-student \

     curl -X GET http://localhost:5000/students/1

     curl -X PATCH http://localhost:5000/patch-student/1   \

     curl -X DELETE "http//localhost:5000/delete-student?name=Juan"

     -H "Content-Type: application/json" \
     -d '{"name": "Juan", "age": 20, "major" : "Ingenieria"}'


# Paso 16: Probar algunos de los endpoints ya creados, los cuales puedes conseguir yendo directamente al archivo hello.py 

# Paso 17: Al bajar el proyecto en aws en el servidor AWS

sudo apt update
sudo apt install python3
sudo apt install python3-pip
sudo apt install python3.12-venv -y
ls /opt
cd /opt
ls
sudo git clone https://github.com/magahr/Hack_REACT_FLASK_CRUD_AWS.git
sudo chmod 755 Hack_REACT_FLASK_CRUD_AWS/
ls  -la
cd Hack_REACT_FLASK_CRUD_AWS/
ls -la
sudo python3 -m venv venv
source venv/bin/activate 
sudo venv/bin/python3 -m pip install -r requirements.txt




Control de cambio

1.- git commit -m "16-11-2024 - Starting with aws"
1.- git commit -m "16-11-2024 - Changing everythin with conecting with aws"
2.- git commit -m "17-11-2024 - Conecting with AWS and testing the API"
3.- git commit -m "15-12-2024 - Testing my backend with flask in AWS"
4.- git commit -m "15-12-2024 - Updating the name of requirements.txt"
5.- git commit -m "29-12-2024 - Updating CORS"

