from flask import Flask, render_template, flash, request, url_for,redirect
import yagmail as yagmail
import utils
import os

app = Flask(__name__)
app.secret_key = "super secret key"

@app.route('/')
def inicio():
    return render_template("iniciar-sesion.html")

@app.route('/registro')
def index():
    return render_template("registro.html")

@app.route('/registro', methods=('GET','POST'))
def registro():
    try:
        if request.methods=='POST':
            user= request.form['usuario']
            password = request.form['contrasena']
            email = request.form['correo']
            error = None

            if not utils.isUsernameValid(user):
                error = "El usuario debe ser alfanumerico o incluir solo '.','_','-'"
                flash(error)
                return render_template('registro.html')

            if not utils.isPasswordValid(password):
                error = 'La contraseña debe contenir al menos una minúscula, una mayúscula, un número y 8 caracteres'
                flash(error)
                return render_template('registro.html')

            if not utils.isEmailValid(email):
                error = 'Correo invalido'
                flash(error)
                return render_template('registro.html')
            yag = yagmail.SMTP('pruebamintic2022', 'Jmd12345678') 
            yag.send(to=email, subject='Activa tu cuenta',
                     contents='Muchas gracias por elegirnos, por favor usa este link para activar tu cuenta ')
            flash('Hemos enviado un correo para activar tu cuenta')
            return render_template('iniciar-sesion.html')
        return render_template('registro.html')
    except Exception as e:
        print(e)
        return render_template('registro.html')

@app.route('/miCuenta')
def MiCuenta():
    return render_template("miCuenta.html")

@app.route('/busqueda')
def busqueda():
    return render_template("busqueda.html")

@app.route('/rec_contrasena')
def rec_contrasena():
    return render_template("recuperar-contraseña.html")

@app.route('/micuenta/ver_blog_propios')
def v_b_propios():
    return render_template("ver-blog-propios.html")

@app.route('/busqueda/ver_blog_publicos')
def v_b_publicos():
    return render_template("ver-blog-publicos.html")

@app.route('/micuenta/modificar_blog')
def modif_blog():
    return render_template("modificar-blog.html")

@app.route('/micuenta/agregar_blog')
def agregar_blog():
    return render_template("agregar-blog.html")

@app.route('/busqueda/ver_blog_publicos/comentar_blog')
def comentar_blog():
    return render_template("comentar-blog.html")

if __name__ == "__main__":
    app.run(debug = True, port=8000)