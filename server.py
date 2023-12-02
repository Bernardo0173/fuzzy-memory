from flask import Flask, redirect, url_for, request
from ModeladoCiudad import *
import json

# Indicar el número de peatones
numPeatones = 50
numCoches = 300

model = SimulacionCiudad(numPeatones, numCoches)


app = Flask(__name__)


@app.route('/tc2008b', methods=['GET'])
def tc2008b():
    user = request.args.get('name')
    return f"welcome {user}"


@app.route('/obtenerDatos', methods=['GET'])
def obtenerDatos():
    datos = model.getDatos()
    datosJSON = json.dumps(datos)
    model.step()
    return datosJSON


if __name__ == '__main__':
    app.run(debug=True)
