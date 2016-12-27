from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hola Amiguitos!</h1>"

@app.route("/check")
def check():
    return "<h1 style='color:red'>Estamos en check!</h1>"

@app.route("/hi")
def hi():
    return "<h1 style='color:green'>Estamos en Hi!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')