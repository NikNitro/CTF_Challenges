from flask import Flask, render_template, redirect, request, url_for, make_response
import jwt
import datetime

app = Flask(__name__)

# Clave secreta para JWT
JWT_SECRET = 'changeme'
ALGORITHMS = ['HS256', 'MD5']  # Algoritmos permitidos

# Usuarios simulados
USERS = {
    'shinobi': 'kuro',
    'Tanaka': 'Tanaka6251ff686774de7a322a31762684bb10'
}

# Función para generar un token JWT
def generate_jwt(username):
    expiration = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    return jwt.encode({'user': username, 'exp': expiration}, JWT_SECRET, algorithm='HS256')

# Función para decodificar el token JWT
def decode_jwt(token):
    return jwt.decode(token, JWT_SECRET, algorithms=ALGORITHMS)

@app.route('/')
def index():
    # Intentamos leer el token JWT desde las cookies
    token = request.cookies.get('jwt_token')
    user = None

    if token:
        try:
            # Intentamos decodificar el token JWT
            decoded = decode_jwt(token)
            user = decoded.get('user')
        except jwt.ExpiredSignatureError:
            return "El token ha expirado, por favor vuelve a iniciar sesión."
        except jwt.InvalidTokenError:
            return "Token inválido, por favor vuelve a iniciar sesión."
    
    return render_template('index.html', logged_in=bool(user))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Verifica el usuario y contraseña
        if USERS.get(username) == password:
            # Genera el token JWT
            token = generate_jwt(username)
            
            # Crea la respuesta con el token en una cookie
            response = make_response(redirect(url_for('index')))
            response.set_cookie('jwt_token', token)
            return response
        else:
            return render_template('login.html', login_failed=True)
    
    return render_template('login.html', login_failed=False)

@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('index')))
    response.set_cookie('jwt_token', '', expires=0)  # Eliminar la cookie
    return response

@app.route('/obtener_katana')
def obtener_katana():
    token = request.cookies.get('jwt_token')
    
    if not token:
        return redirect(url_for('login'))
    
    try:
        decoded = decode_jwt(token)
        user = decoded.get('user')
        
        # Comprobar si el usuario es "Tanaka"
        if user == 'Tanaka':
            return render_template('katana.html', user=user, katana_granted=True)
        else:
            return render_template('katana.html', user=user, katana_granted=False)
    except jwt.ExpiredSignatureError:
        return "El token ha expirado, por favor vuelve a iniciar sesión."
    except jwt.InvalidTokenError:
        return "Token inválido, por favor vuelve a iniciar sesión."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8996)
