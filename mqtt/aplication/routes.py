from aplication import app
from flask import render_template,redirect,url_for,flash,request
from aplication.models import Data,db
from aplication.forms import SearchForm
from aplication import app
import jyserver.Flask as jsf

@jsf.use(app)
class App:
    def __init__(self):
        self.data=""
    def deleteData(self,idElement):
        data=Data.query.filter_by(id=idElement).first()
        db.session.delete(data)
        db.session.commit()
    def insertData(self,message,topic,date,qos):
        objData=Data(data=message,topic=topic,date=date,qos=qos)
        db.session.add(objData)
        db.session.commit()

@app.route('/') 
def home_page():
    return App.render(render_template('base.html'))

@app.route('/database',methods=["POST","GET"])
def db_page():
    form=SearchForm()
    datas=Data.query.all()
    return App.render(render_template('database.html',form=form,items=datas))

@app.route('/search',methods=["POST","GET"])
def search_page():
    search_form=SearchForm()
    linesSearched=Data.query
    dataSearched=search_form.searched.data
    linesSearched = linesSearched.filter(Data.data.like('%' + dataSearched + '%'))
    linesSearched = linesSearched.order_by(Data.id).all()
    return App.render(render_template('search.html',items=linesSearched))
