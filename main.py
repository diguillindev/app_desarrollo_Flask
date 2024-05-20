from flask import Flask, request, render_template
import json

app = Flask(__name__, template_folder="templates")


def load_users_from_json():
    try:
        with open('users.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


users_db = load_users_from_json()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])

        precio_unitario = 9000
        total_sin_descuento = precio_unitario * cantidad

        # Calculando el descuento basado en la edad
        if edad >= 18 and edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        # Aplicando el descuento si corresponde
        total_con_descuento = total_sin_descuento * (1 - descuento)

        return render_template('ejercicio1.html',
                               nombre=nombre,
                               total_sin_descuento=total_sin_descuento,
                               total_con_descuento=total_con_descuento)

    return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['POST', 'GET'])
def login():
    error = None
    message = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if valid_login(username, password):
            if username == 'juan':
                message = f'Bienvenido administrador {username}'
            elif username == 'pepe':
                message = f'Bienvenido usuario {username}'
        else:
            error = 'Usuario o contraseña incorrectos'
        return render_template('ejercicio2.html', error=error, message=message)

    return render_template('ejercicio2.html')


def valid_login(username, password):
    if username in users_db:
        if users_db[username] == password:
            return True
    return False


if __name__ == '__main__':
    app.run()
