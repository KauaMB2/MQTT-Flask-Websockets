from aplication import app#Get the var "app" inside aplication/__init__.py

#Checks if the run.py file has executed directly and not imporeted
if __name__=='__main__':
    app.run(debug=True)#Liga o servidor