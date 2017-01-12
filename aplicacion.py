from flask import Flask, render_template, url_for, request
import socket, sys, random, time
app = Flask(__name__)

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
        return render_template('hi.html', puntos=num_puntos, valor=calcula_pi(num_puntos))

@app.route("/metecosas")
def metecosas():
    return render_template('metecosas.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')