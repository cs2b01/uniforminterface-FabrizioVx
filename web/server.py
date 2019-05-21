from flask import Flask,render_template, request, session, Response, redirect
from database import connector
from model import entities
import json

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/forms')
def users():
    db_session = db.getSession(engine)
    users = db_session.query(entities.Formato)
    data = users[:]
    #db_session1 =db.getSession(engine)
    #users1= db_session1.query(entities.Forms)
    #data1 = users1[:]


    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype = 'application/json')

#@app.route('/create_test_books', methods = ['GET'])
#def create_test_books():
    #db_session = db.getSession(engine)
    #book = entities.Book(name="HOLAAA", isbn="12345", title="HOLA HTML5")
    #db_session.add(book)
    #db_session.commit()


@app.route('/create_test_formate_tarea')
def create_test_formate():
    db_session = db.getSession(engine)
    formate = entities.Formato(Codigo="201907833",Nombre="Renzo",Apellido="Bustamante",Password="AARM&X86AMD12")
    db_session.add(formate)
    db_session.commit()
    return "Test Dictionary created!"





if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('0.0.0.0'))
