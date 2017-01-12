from flask import Flask, render_template, url_for, request
import socket
app = Flask(__name__)

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
        primero=request.form['primercampo']
        segundo=request.form['segundocampo']
        return render_template('hi.html',primero=primero,segundo=segundo)

@app.route("/metecosas")
def metecosas():
    return render_template('metecosas.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')