from aplication import app
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy(app)#Cria DB

class Data(db.Model):#Cria classe
    id=db.Column(db.Integer(),primary_key=True)#Cria coluna
    data=db.Column(db.String(length=1024),nullable=True,unique=False)
    topic=db.Column(db.String(length=50),nullable=False,unique=False)
    date=db.Column(db.String(length=50),nullable=False,unique=False)
    qos=db.Column(db.Integer(),nullable=False,unique=False)
    def __repr__(self):# Define novo "identificador" para  objeto
        return f'dataNumber {self.data}'

from aplication import routes#Import the routes inside routes.py

