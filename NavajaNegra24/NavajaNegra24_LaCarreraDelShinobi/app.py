import os
import time
import threading
from flask import Flask, jsonify, redirect

app = Flask(__name__)

# Definir la ubicación del pergamino sagrado
FLAG_FILE = "/var/www/pergamino.txt"
FLAG_ACCESSIBLE = False

# Función que permite leer temporalmente el pergamino sagrado
def vigilar_pergamino():
    global FLAG_ACCESSIBLE
    time.sleep(2)  # Ventana de tiempo corta
    # El shinobi temporalmente se despista porque otro usuario quiere entrar
    os.chmod(FLAG_FILE, 0o644)  # Cambiar permisos temporalmente
    FLAG_ACCESSIBLE = True
    #time.sleep(0.001)  # Ventana de tiempo corta
    os.chmod(FLAG_FILE, 0o600)  # Reestablecer los permisos
    FLAG_ACCESSIBLE = False


@app.route("/leer_pergamino", methods=["GET"])
def leer_pergamino():
    # Simula una operación crítica del guardián que cambia los permisos
    threading.Thread(target=vigilar_pergamino).start()

    if FLAG_ACCESSIBLE and os.access(FLAG_FILE, os.R_OK):
        with open(FLAG_FILE, "r") as file:
            pergamino = file.read()
        return jsonify({"pergamino": pergamino})
    else:
        return jsonify({"error": "El guardián no te permite leer el pergamino."}), 403

# Ruta principal que redirige a /leer_pergamino
@app.route("/", methods=["GET"])
def home():
    return redirect("/leer_pergamino")
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8997)
