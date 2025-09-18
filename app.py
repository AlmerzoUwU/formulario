import mysql.connector
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Conexión a la base de datos MySQL
def init_db():
    conn = mysql.connector.connect(
        host="yourusername.mysql.pythonanywhere-services.com",  # Cambia esto con el host que te dio PythonAnywhere
        user="yourusername",  # Tu nombre de usuario de PythonAnywhere
        password="yourpassword",  # Tu contraseña de MySQL
        database="mibasededatos"  # El nombre de tu base de datos en MySQL
    )
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id INT AUTO_INCREMENT PRIMARY KEY, 
                        nombre VARCHAR(255), 
                        apellido VARCHAR(255)
                      )''')
    conn.commit()
    conn.close()

# Ruta principal que muestra el formulario
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para recibir el formulario y agregar datos a la base de datos
@app.route('/submit', methods=['POST'])
def submit():
    nombre = request.form['nombre']
    apellido = request.form['apellido']

    # Guardar en la base de datos MySQL
    conn = mysql.connector.connect(
        host="yourusername.mysql.pythonanywhere-services.com",  # Cambia esto con el host que te dio PythonAnywhere
        user="yourusername",  # Tu nombre de usuario de PythonAnywhere
        password="yourpassword",  # Tu contraseña de MySQL
        database="mibasededatos"  # El nombre de tu base de datos en MySQL
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, apellido) VALUES (%s, %s)", (nombre, apellido))
    conn.commit()
    conn.close()

    return redirect(url_for('form_submitted'))

# Ruta para mostrar la página de éxito
@app.route('/form_submitted')
def form_submitted():
    return render_template('form_submitted.html')

# Ruta para ver la lista de usuarios registrados
@app.route('/usuarios')
def usuarios():
    conn = mysql.connector.connect(
        host="yourusername.mysql.pythonanywhere-services.com",  # Cambia esto con el host que te dio PythonAnywhere
        user="yourusername",  # Tu nombre de usuario de PythonAnywhere
        password="yourpassword",  # Tu contraseña de MySQL
        database="mibasededatos"  # El nombre de tu base de datos en MySQL
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conn.close()
    return render_template('lista_usuarios.html', usuarios=usuarios)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
