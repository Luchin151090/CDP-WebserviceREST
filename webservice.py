from flask import jsonify
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return jsonify({'hola':'Bienvenido a Calculadora'})

@app.route('/suma/',methods=['POST'])
def sumar():
    suma = {
        "operando1": request.json['operando1'],
        "operando2": request.json['operando2']
    }
    sumita = request.json['operando1']+request.json['operando2']
    return jsonify({"suma es:":sumita})

@app.route('/resta/',methods=['POST'])
def resta():
    resta = {
        "operando1": request.json['operando1'],
        "operando2": request.json['operando2']
    }
    restar = request.json['operando1']-request.json['operando2']
    return jsonify({"resta es:":restar})

@app.route('/multi/',methods=['POST'])
def multiplicacion():
    multiplicacion = {
        "operando1": request.json['operando1'],
        "operando2": request.json['operando2']
    }
    multiplicar = request.json['operando1']*request.json['operando2']
    return jsonify({"multiplicacion es:":multiplicar})

@app.route('/divi/',methods=['POST'])
def division():
    division = {
        "operando1": request.json['operando1'],
        "operando2": request.json['operando2']
    }
    if(request.json['operando2']==0):
        return jsonify({"Division":"ERROR DIVISION 0"})
    else:
        divi = request.json['operando1']/request.json['operando2']
        return jsonify({"division es:":divi})

if __name__=="__main__":
    app.run(debug=True,port=5000)
