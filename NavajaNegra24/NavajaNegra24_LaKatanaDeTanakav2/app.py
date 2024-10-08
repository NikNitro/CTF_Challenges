from flask import Flask, render_template, redirect, request, url_for, send_from_directory
import jwt
import datetime
import os
import requests
from jwt.exceptions import InvalidTokenError
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.x509 import load_pem_x509_certificate

app = Flask(__name__)

# Ruta donde se almacena la clave privada y pública del servidor
PRIVATE_KEY_PATH = 'keys/private_key.pem'
PUBLIC_KEY_PATH = 'keys/public_key.pem'

# Usuario simulado
USERS = {
    'shinobi': 'kuro',  # Contraseña de Shinobi
    'Tanaka': 'clave_secreta_tanaka'
}

# Leer clave privada
def get_private_key():
    with open(PRIVATE_KEY_PATH, 'rb') as f:
        return serialization.load_pem_private_key(f.read(), password=None, backend=default_backend())

# Leer clave pública
def get_public_key():
    with open(PUBLIC_KEY_PATH, 'rb') as f:
        return f.read()

def get_public_key_from_jku(jku_url):
    """
    Obtiene la clave pública desde la URL proporcionada en el 'jku'.
    """
    try:
        response = requests.get(jku_url)
        if response.status_code == 200:
            public_key_pem = response.content.decode('utf-8')  # Asegúrate de que es un string
            # Cargar la clave pública directamente
            public_key = serialization.load_pem_public_key(public_key_pem.encode('utf-8'), backend=default_backend())
            return public_key
        else:
            return None
    except Exception as e:
        print(f"Error obteniendo la clave pública desde jku: {e}")
        return None

def decode_jwt(token):
    try:
        # Extraemos el header del JWT para obtener el 'jku'
        unverified_header = jwt.get_unverified_header(token)
        jku_url = unverified_header.get('jku')

        # Obtener la clave pública desde la URL del 'jku'
        public_key = get_public_key_from_jku(jku_url)

        if not public_key:
            return None, "Error: No se pudo obtener la clave pública desde la URL proporcionada en 'jku'."

        # Intentamos decodificar el token con la clave pública obtenida
        decoded_token = jwt.decode(token, public_key, algorithms=['RS256'])
        return decoded_token, None
    except InvalidTokenError:
        return None, "Error: Token inválido."
    except Exception as e:
        return None, f"Error desconocido: {str(e)}"

@app.route('/')
def index():
    token = request.cookies.get('jwt_token')
    if token:
        decoded_token, error = decode_jwt(token)
        if decoded_token:
            user = decoded_token.get('user')
            return render_template('index.html', logged_in=True, user=user)
    return render_template('index.html', logged_in=False)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Verifica el usuario y contraseña
        if USERS.get(username) == password:
            # Genera un token JWT para el usuario
            private_key = get_private_key()
            token = jwt.encode(
                {'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
                private_key,
                algorithm='RS256',
                headers={'jku': url_for('get_cert', _external=True)}
            )

            # Establecer la cookie con el JWT
            response = redirect(url_for('index'))
            response.set_cookie('jwt_token', token)
            return response
        else:
            return render_template('login.html', login_failed=True)

    return render_template('login.html', login_failed=False)

@app.route('/logout')
def logout():
    response = redirect(url_for('index'))
    response.delete_cookie('jwt_token')
    return response

@app.route('/obtener_katana')
def obtener_katana():
    token = request.cookies.get('jwt_token')
    if token:
        decoded_token, error = decode_jwt(token)

        if error:
            return error, 403

        # Si el token es válido, comprobamos el usuario
        user = decoded_token.get('user')
        if user == 'Tanaka':
            return render_template('katana.html', user=user, katana_granted=True)
        else:
            return render_template('katana.html', user=user, katana_granted=False)
    else:
        return redirect(url_for('login'))

# Endpoint para servir el certificado público
@app.route('/cert.pem')
def get_cert():
    """
    Sirve el certificado público que puede ser utilizado para verificar el JWT.
    """
    return send_from_directory(directory=os.path.abspath('keys'), path='public_key.pem')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8995)
