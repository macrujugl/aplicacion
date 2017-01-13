from flask import Flask, render_template, url_for, request
from azure.storage.table import TableService, Entity
import socket, sys, random, time, math

app = Flask(__name__)

def busca_heroe(nombre):
    account_name=os.environ['AZURE_STORAGE_ACCOUNT']
    account_key=os.environ['AZURE_STORAGE_ACCESS_KEY']
    table_service = TableService(account_name, account_key)

    filter="PartitionKey eq "+"\'"+nombre+"\'"
    
    consulta=table_service.query_entities('heroes', filter)
    
    salida={}
    
    for heroe in consulta:
        for key in heroe.__dict__.keys():
            salida[key]=str(heroe.__dict__[key])
    
    salida['Nombre']=salida['PartitionKey']
    salida['Grupo']=salida['RowKey']
    del salida['etag']
    del salida['PartitionKey']
    del salida['RowKey']
    del salida['Timestamp']
    
    return salida



def sample(p):
    x, y = random.random(),random.random()
    return 1 if x*x + y*y < 1 else 0

def calcula_pi(p):
    return 4.0*(reduce(lambda a, b: a + b, map(sample,xrange(0, p))))/p

@app.route("/")
def hello():
    return render_template('hello.html')

@app.route("/check")
def check():
    machine_name=socket.gethostname()
    if machine_name[-1].isdigit():
        parity=int(machine_name[-1])%2
    else:
        parity=2
    
    return render_template('check.html',machine=machine_name,fondo=parity)

@app.route("/hi", methods=['GET', 'POST'])
def hi():
    if request.method=='GET':
        return "<h1 style='color:green'>Estamos en Hi!</h1>"
    else:
        num_puntos=int(request.form['primercampo'])
        start_time = time.time()
        valor=calcula_pi(num_puntos)
        tiempo = time.time()-start_time
        error=abs(math.pi-valor)

        return render_template('hi.html', puntos=num_puntos, valor=valor, tiempo=tiempo, error=error)

@app.route("/metecosas")
def metecosas():
    return render_template('metecosas.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')