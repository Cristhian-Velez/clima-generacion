from flask import Flask, request, jsonify, Response
import pandas as pd
import io

app = Flask(__name__)

# Base de datos temporal
usuarios = []


# -------------------------------
# 1. GET: Mostrar listado de usuarios
# -------------------------------
@app.get("/usuarios")
def listar_usuarios():
    return jsonify({
        "total": len(usuarios),
        "usuarios": usuarios
    })


# -------------------------------
# 2. GET: Mostrar formulario simple
# -------------------------------
@app.get("/frontend")
def frontend():
    return """
    <h1>Registrar usuario</h1>

    <form action="/registrar" method="post">
        Nombre: <input type="text" name="nombre"><br><br>
        Teléfono: <input type="text" name="telefono"><br><br>
        Cédula: <input type="text" name="cedula"><br><br>
        Correo: <input type="text" name="correo"><br><br>

        <button type="submit">Registrar</button>
    </form>

    <br><h2>Usuarios registrados</h2>
    <a href="/usuarios">Ver lista en JSON</a>
    """


# -------------------------------
# 3. POST: Registrar usuario
# -------------------------------
@app.post("/registrar")
def registrar():
    nombre = request.form.get("nombre")
    telefono = request.form.get("telefono")
    cedula = request.form.get("cedula")
    correo = request.form.get("correo")

    usuario = {
        "nombre": nombre,
        "telefono": telefono,
        "cedula": cedula,
        "correo": correo
    }

    usuarios.append(usuario)

    return """
    <h2>Usuario registrado correctamente</h2>
    <a href="/frontend">Volver</a>
    """


# -------------------------------
# 4. DELETE: Eliminar usuario por posición
# -------------------------------
@app.get("/eliminar/<int:pos>")
def eliminar(pos):
    if pos < 0 or pos >= len(usuarios):
        return "<p>Posición no válida</p>"

    usuarios.pop(pos)
    return "<p>Usuario eliminado</p><a href='/frontend'>Volver</a>"


# -------------------------------
# 5. PUT: Actualizar usuario por posición
# -------------------------------
@app.post("/actualizar/<int:pos>")
def actualizar(pos):
    if pos < 0 or pos >= len(usuarios):
        return "<p>Posición no válida</p>"

    nombre = request.form.get("nombre")
    telefono = request.form.get("telefono")
    cedula = request.form.get("cedula")
    correo = request.form.get("correo")

    usuarios[pos] = {
        "nombre": nombre,
        "telefono": telefono,
        "cedula": cedula,
        "correo": correo
    }

    return "<p>Usuario actualizado</p><a href='/frontend'>Volver</a>"


if __name__ == "__main__":
    app.run(debug=True)