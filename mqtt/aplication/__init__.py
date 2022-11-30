from flask import Flask#Import flask
app = Flask(__name__)#Cria aplicação
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/d_name'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345@localhost/datamqtt'
app.config['SECRET_KEY']='829de852066b68880f990c50'#Uma camada a mais de segurança em relação ao formulário


from aplication import routes#Importa as rotas(NECESSÁRIO)

