from flask import Flask, render_template, url_for
import socket
app = Flask(__name__)

@app.route("/")
def hello():

    machine_name=socket.gethostname()
    
    if machine_name[-1].isdigit():
        parity=int(machine_name[-1])%2
    else:
        parity=2
    
    return "<h1 style='color:blue'>Hola Amiguitos!</h1>"

@app.route("/check")
def check():
    return render_template('check.html',machine=machine_name)

@app.route("/hi")
def hi():
    return "<h1 style='color:green'>Estamos en Hi!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')