from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50))
    contrasena = db.Column(db.String(50))
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    saldo = db.Column(db.Numeric(asdecimal=False), default=0)    
    cedula = db.Column(db.Numeric,nullable=False, unique=True)
    telefono = db.Column(db.Numeric)
    email = db.Column(db.String(50))
    genero = db.Column(db.String(10))
    direccion = db.Column(db.String(80))
    rol = db.Column(db.String(20))
    


class UsuarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        include_relationships = True
        load_instance = True
    cedula = fields.Integer()
    telefono = fields.Integer()
