from flask import Flask, render_template, redirect, url_for
from cliente_dao import ClienteDAO
from cliente import Cliente
from cliente_forma import ClienteForma

app = Flask(__name__)

app.config['SECRET_KEY'] = 'llave_secreta' # Ejemplo

titulo_app = 'Zona Fit App'

@app.route('/') #url: http://localhost:5000/
@app.route('/index.html') #url: http://localhost:5000/index.html

def inicio():
    app.logger.debug('Entramos al path de inicio /')
    
    # Recuperamos los clientes de la BD
    clientes_db = ClienteDAO.seleccionar()
    # Creamos el objeto cliente form vacio
    cliente = Cliente()
    cliente_forma = ClienteForma(obj=cliente)
    
    return render_template('index.html', titulo=titulo_app, clientes=clientes_db,
                           forma=cliente_forma)

@app.route('/guardar', methods=['POST'])
def guardar():
    # Creamos los objetos de cliente vacios
    cliente = Cliente()
    cliente_forma = ClienteForma(obj=cliente)
    
    if cliente_forma.validate_on_submit():
        cliente_forma.populate_obj(cliente)

        ClienteDAO.insertar(cliente)
    else:
        print(cliente_forma.errors)
    return redirect(url_for('inicio'))

@app.route('/limpiar')
def limpiar():
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run(debug=True)