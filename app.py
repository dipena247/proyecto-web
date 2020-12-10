from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("iniciar-sesion.html")

@app.route('/registro')
def registro():
    return render_template("registro.html")

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

if __name__=='__main__':
    app.run(debug=True, port=5000)